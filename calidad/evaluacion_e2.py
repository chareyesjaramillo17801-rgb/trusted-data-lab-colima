"""Evaluacion reproducible E2 de productos Oro, sin modificar los datos."""
from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
ORO = ROOT / 'data' / 'oro'
SALIDA = ROOT / 'resultados' / 'calidad_e2'

FUENTES = {
    'registros_trimestrales': ('registros_trimestrales.parquet', ['id_fila_bronce']),
    'indice_shf_colima': ('indice_shf_colima.parquet', ['id_fila_bronce']),
    'comparacion_municipal': ('comparacion_municipal.parquet', []),
    'variables_analiticas_sniiv': ('variables_analiticas_sniiv.parquet', []),
    'comparacion_modelos': ('comparacion_modelos.csv', []),
    'pronosticos_exploratorios': ('pronosticos_exploratorios.csv', []),
    'diagnostico_ampliado': ('diagnostico_ampliado.csv', []),
}


def porcentaje(numerador: int, denominador: int) -> float | None:
    return round(100 * numerador / denominador, 2) if denominador else None


def analizar(nombre: str, archivo: str, claves_sugeridas: list[str]) -> dict:
    ruta = ORO / archivo
    if not ruta.is_file():
        return {'producto': nombre, 'archivo': str(ruta.relative_to(ROOT)), 'estado': 'ausente'}
    datos = pd.read_parquet(ruta) if ruta.suffix == '.parquet' else pd.read_csv(ruta)
    filas, columnas = datos.shape
    celdas = filas * columnas
    no_nulas = int(datos.notna().sum().sum())
    # Se reporta la completitud general, sin equiparar nulos estructurales con errores.
    duplicados_completos = int(datos.duplicated().sum()) if columnas else 0
    claves = [c for c in claves_sugeridas if c in datos.columns]
    duplicados_clave = int(datos.duplicated(subset=claves).sum()) if claves else None
    columnas_linaje = [c for c in datos.columns if c in {
        'id_fila_bronce', 'origen_bronce', 'sha256_bronce',
        'fecha_ingesta_utc', 'metodo_fecha_ingesta',
        'ids_bronce_entrenamiento', 'ids_bronce_prueba',
    }]
    if 'origen_bronce' in datos.columns and 'sha256_bronce' in datos.columns:
        filas_linaje = int(datos[['origen_bronce', 'sha256_bronce']].notna().all(axis=1).sum())
    else:
        filas_linaje = None
    nulos = {str(k): int(v) for k, v in datos.isna().sum().items() if v > 0}
    return {
        'producto': nombre, 'archivo': str(ruta.relative_to(ROOT)), 'estado': 'evaluado',
        'filas': filas, 'columnas': columnas, 'completitud_celdas_pct': porcentaje(no_nulas, celdas),
        'filas_duplicadas_completas': duplicados_completos,
        'unicidad_filas_completas_pct': porcentaje(filas - duplicados_completos, filas),
        'claves_evaluadas': claves, 'duplicados_clave': duplicados_clave,
        'columnas_linaje': columnas_linaje,
        'filas_con_origen_y_hash': filas_linaje,
        'trazabilidad_origen_hash_pct': porcentaje(filas_linaje, filas) if filas_linaje is not None else None,
        'nulos_por_columna': nulos,
    }


def ejecutar() -> dict:
    SALIDA.mkdir(parents=True, exist_ok=True)
    evaluaciones = [analizar(n, a, k) for n, (a, k) in FUENTES.items()]
    reporte = {
        'ejecutado_utc': datetime.now(UTC).isoformat(),
        'alcance': 'mediciones descriptivas de productos Oro existentes',
        'advertencias': [
            'La completitud global incluye nulos estructurales; revisar cada columna antes de atribuir defectos.',
            'Unicidad de fila completa no prueba unicidad de la clave de negocio.',
            'La presencia de origen/hash no demuestra por si sola integridad criptografica del linaje.',
            'ISO/IEC 25010 no se acredita solo con estas metricas de datos.',
        ],
        'productos': evaluaciones,
    }
    (SALIDA / 'metricas_iso25012.json').write_text(json.dumps(reporte, ensure_ascii=False, indent=2), encoding='utf-8')
    tabla = pd.DataFrame([{k: v for k, v in r.items() if k not in ('nulos_por_columna', 'columnas_linaje', 'claves_evaluadas')} for r in evaluaciones])
    tabla.to_csv(SALIDA / 'metricas_iso25012.csv', index=False, encoding='utf-8-sig')
    lineas = [
        '# Resultados de calidad de datos — E2', '',
        f"Ejecucion UTC: {reporte['ejecutado_utc']}", '',
        '## Medicion ISO/IEC 25012 (seleccion de atributos)', '',
        '| Producto | Filas | Completitud de celdas | Unicidad de filas | Origen y hash |',
        '|---|---:|---:|---:|---:|',
    ]
    for r in evaluaciones:
        if r['estado'] != 'evaluado':
            lineas.append(f"| {r['producto']} | Archivo ausente | — | — | — |")
            continue
        fmt = lambda v: f'{v}%' if v is not None else 'No evaluable'
        lineas.append(f"| {r['producto']} | {r['filas']} | {fmt(r['completitud_celdas_pct'])} | {fmt(r['unicidad_filas_completas_pct'])} | {fmt(r['trazabilidad_origen_hash_pct'])} |")
    lineas += ['', '## Limites de interpretacion', ''] + [f'- {a}' for a in reporte['advertencias']]
    (SALIDA / 'RESUMEN.md').write_text('\n'.join(lineas) + '\n', encoding='utf-8')
    return {'productos': len(evaluaciones), 'evaluados': sum(x['estado'] == 'evaluado' for x in evaluaciones), 'salida': str(SALIDA)}


if __name__ == '__main__':
    print(json.dumps(ejecutar(), ensure_ascii=False, indent=2))
