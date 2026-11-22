"""Experimentos E2 reproducibles sobre agregación SNIIV local.
Ejecutar: python -m experimentos.e2_estadistica
No consulta APIs ni modifica los datos originales.
"""
import itertools
import json
import platform
import random
import time
from datetime import UTC, datetime
from pathlib import Path

import pandas as pd
from scipy import stats
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.stattools import durbin_watson

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'resultados' / 'estadistica_e2'
SEED = 20261122
REPETICIONES = 3
CICLOS = 30


def fuente():
    archivos = sorted(p for p in (ROOT / 'data/bronce/sniiv_registro').glob('registro_*.json') if not p.name.endswith('.metadata.json'))
    if not archivos:
        raise FileNotFoundError('No hay capturas SNIIV en Bronce')
    ruta = archivos[-1]
    datos = pd.DataFrame(json.loads(ruta.read_text(encoding="utf-8")))
    columnas = ['municipio', 'año', 'mes', 'segmento', 'viviendas']
    if not set(columnas).issubset(datos.columns):
        raise ValueError('La fuente SNIIV no tiene las columnas requeridas')
    datos = datos[columnas].copy()
    datos['viviendas'] = pd.to_numeric(datos['viviendas'], errors='raise')
    return datos, ruta


def procesar(df, tamano, categoria, ordenar, sort_group, ciclos=CICLOS):
    """Procesamiento local idéntico en significado; factores afectan estrategia, no valores."""
    salida = None
    for _ in range(ciclos):
        partes = []
        for inicio in range(0, len(df), tamano):
            bloque = df.iloc[inicio:inicio + tamano].copy()
            if categoria:
                bloque['municipio'] = bloque['municipio'].astype('category')
            if ordenar:
                bloque = bloque.sort_values(['municipio', 'año', 'mes'], kind='stable')
            partes.append(bloque)
        conjunto = pd.concat(partes, ignore_index=True)
        salida = conjunto.groupby(['municipio', 'año'], observed=True, sort=sort_group)['viviendas'].sum()
    return salida.sort_index()


def medir(df, factores, referencia):
    inicio = time.perf_counter_ns()
    resultado = procesar(df, factores['tamano'], factores['categoria'], factores['ordenar'], factores['sort_group'])
    duracion = (time.perf_counter_ns() - inicio) / 1e6
    if not resultado.equals(referencia):
        raise AssertionError('El tratamiento cambió los resultados agregados; experimento inválido')
    return duracion


def configuracion(a, b, c, d='-'):
    return {'tamano': 128 if a == '-' else 512,
            'categoria': b == '+', 'ordenar': c == '+', 'sort_group': d == '+'}


def tabla_anova(df, formula, etiqueta):
    modelo = ols(formula, data=df.rename(columns={'A':'factor_a','B':'factor_b','C':'factor_c','D':'factor_d'})).fit()
    tabla = anova_lm(modelo, typ=2).reset_index().rename(columns={'index': 'efecto'})
    tabla.to_csv(OUT / f'anova_{etiqueta}.csv', index=False)
    residuos = modelo.resid
    diagnostico = {'modelo': etiqueta, 'n': len(df), 'r2': float(modelo.rsquared),
                   'residuos_shapiro_p': float(stats.shapiro(residuos).pvalue) if len(residuos) >= 3 else None,
                   'levene_p': float(stats.levene(*(g['tiempo_ms'].to_numpy() for _,g in df.groupby(['A','B','C'] if etiqueta == '2_3' else ['A','B'] if etiqueta == '3_2' else ['A','B','C','D'], dropna=False))).pvalue),
                   'durbin_watson_orden_ejecucion': float(durbin_watson(pd.Series(residuos,index=df.index).loc[df.sort_values('orden_ejecucion').index])),
                   'advertencia': 'Shapiro, Levene y Durbin-Watson son diagnósticos orientativos; revisar residuos y orden de corrida'}
    (OUT / f'diagnostico_{etiqueta}.json').write_text(json.dumps(diagnostico, indent=2), encoding='utf-8')
    return tabla, diagnostico


def correr():
    OUT.mkdir(parents=True, exist_ok=True)
    df, ruta = fuente()
    referencia = procesar(df, 512, False, False, False, ciclos=1)
    rng = random.Random(SEED)
    planes = []
    # 2^3 completo: A tamaño, B categoría, C orden; D fijo (groupby sort=False)
    for a,b,c in itertools.product('-+', repeat=3):
        for replica in range(1, REPETICIONES + 1):
            planes.append(('factorial_2_3', replica, a,b,c,'-',configuracion(a,b,c)))
    # Diseño 3x2: tamaño de lote 64,256,1024; categoría activada/desactivada
    for tamano, b in itertools.product((64,256,1024), '-+'):
        for replica in range(1, REPETICIONES + 1):
            planes.append(('factorial_3_2', replica, str(tamano),b,'-','-',
                           {'tamano':tamano,'categoria':b=='+','ordenar':False,'sort_group':False}))
    # Diseño 2^4 completo y fracción regular D=ABC, generador I=ABCD.
    for a,b,c,d in itertools.product('-+', repeat=4):
        for replica in range(1, REPETICIONES + 1):
            planes.append(('factorial_2_4', replica,a,b,c,d,configuracion(a,b,c,d)))
    rng.shuffle(planes)
    registros = []
    for numero, (diseno, replica,a,b,c,d, factores) in enumerate(planes, start=1):
        tiempo_ms = medir(df, factores, referencia)
        registros.append({'orden_ejecucion':numero,'diseno':diseno,'replica':replica,
                          'A':a,'B':b,'C':c,'D':d,'tiempo_ms':tiempo_ms,**factores})
    datos = pd.DataFrame(registros)
    datos.to_csv(OUT/'corridas_aleatorizadas.csv', index=False)
    d23 = datos.query("diseno == 'factorial_2_3'").copy()
    _t23, _diag23 = tabla_anova(d23, 'tiempo_ms ~ C(factor_a)*C(factor_b)*C(factor_c)', '2_3')
    d32 = datos.query("diseno == 'factorial_3_2'").copy()
    _t32, _diag32 = tabla_anova(d32, 'tiempo_ms ~ C(factor_a)*C(factor_b)', '3_2')
    d24 = datos.query("diseno == 'factorial_2_4'").copy()
    _t24, _diag24 = tabla_anova(d24, 'tiempo_ms ~ C(factor_a)*C(factor_b)*C(factor_c)*C(factor_d)', '2_4')
    fraccion = d24.loc[d24.apply(lambda r: ('+' if sum(x=='-' for x in (r.A,r.B,r.C))%2==0 else '-') == r.D,axis=1)].copy()
    # D=ABC en codificación ±1; fracción de 8 tratamientos, 3 réplicas.
    fraccion.to_csv(OUT/'fraccion_2_4_menos_1.csv', index=False)
    _tabla_fr, _diag_fr = tabla_anova(fraccion, 'tiempo_ms ~ C(factor_a)+C(factor_b)+C(factor_c)+C(factor_d)', 'fraccion')
    medias = d23.groupby(['A','B','C'],as_index=False)['tiempo_ms'].mean().sort_values('tiempo_ms')
    medias.to_csv(OUT/'medias_tratamientos_2_3.csv',index=False)
    ganador = medias.iloc[0]
    mejor = configuracion(ganador.A, ganador.B, ganador.C)
    base = configuracion('-', '-', '-')
    # Corridas nuevas, independientes de las de selección, intercaladas y aleatorizadas.
    confirmar = [('base',base),('mejor',mejor)] * 5
    rng.shuffle(confirmar)
    confirma = pd.DataFrame([{'orden':i,'tratamiento':nombre,'tiempo_ms':medir(df, conf, referencia)}
                            for i,(nombre,conf) in enumerate(confirmar,1)])
    confirma.to_csv(OUT/'confirmacion.csv',index=False)
    promedio = confirma.groupby('tratamiento')['tiempo_ms'].mean()
    mejora = float(100*(promedio['base']-promedio['mejor'])/promedio['base'])
    resumen = {'fuente':str(ruta.relative_to(ROOT)), 'filas_fuente':len(df),
               'fecha_ejecucion_utc':datetime.now(UTC).isoformat(),
               'semilla':SEED,'replicas_por_tratamiento':REPETICIONES,'ciclos_por_corrida':CICLOS,
               'python':platform.python_version(),'pandas':pd.__version__,
               'tratamiento_ganador_2_3':{k:str(ganador[k]) for k in ('A','B','C')},
               'confirmacion_media_base_ms':float(promedio['base']),
               'confirmacion_media_mejor_ms':float(promedio['mejor']),
               'mejora_porcentual_confirmada':mejora,
               'interpretacion':'Una mejora negativa significa que el tratamiento seleccionado no mejoró en confirmación.',
               'alias_fraccion':['I=ABCD','A=BCD','B=ACD','C=ABD','D=ABC','AB=CD','AC=BD','AD=BC'],
               'nota':'Diseño experimental de ingeniería; tiempos de una máquina, no precios de vivienda.'}
    (OUT/'resumen.json').write_text(json.dumps(resumen,ensure_ascii=False,indent=2),encoding='utf-8')
    lineas = ['# Experimentos E2 — Análisis Estadístico','',
              f'**Fuente:** `{resumen["fuente"]}` ({len(df)} registros).',
              f'**Ejecución UTC:** {resumen["fecha_ejecucion_utc"]}.',
              f'**Aleatorización:** semilla {SEED}; tres réplicas por tratamiento.',
              f'**Respuesta:** milisegundos de {CICLOS} ciclos de agregación SNIIV local.',
              '**Integridad:** cada tratamiento produjo la misma agregación que la referencia.', '',
              '## Diseño 2³', 'A: tamaño 128/512; B: categoría no/sí; C: ordenación no/sí; agrupación con sort=False.',
              f'Mejor media observada: A={ganador.A}, B={ganador.B}, C={ganador.C}.',
              'ANOVA e interacciones: `anova_2_3.csv`; diagnóstico: `diagnostico_2_3.json`.', '',
              '## Diseño 3×2', 'Tamaño de lote 64/256/1024 y conversión a categoría no/sí; ANOVA con interacción en `anova_3_2.csv`.', '',
              '## Diseño 2⁴ completo y fracción 2^(4−1)',
              'D: ordenamiento interno de groupby no/sí. Fracción regular D=ABC, relación definitoria I=ABCD.',
              'Alias: A=BCD; B=ACD; C=ABD; D=ABC; AB=CD; AC=BD; AD=BC.',
              'La fracción de resolución IV confunde interacciones de dos factores entre sí; no permite distinguirlas.',
              'Resultados: `anova_2_4.csv`, `fraccion_2_4_menos_1.csv`, `anova_fraccion.csv`.', '',
              '## Confirmación independiente',
              f'Media base: {promedio["base"]:.3f} ms; media seleccionada: {promedio["mejor"]:.3f} ms.',
              f'Cambio confirmado: {mejora:.2f}% (positivo = más rápido).',
              'La selección del mejor tratamiento puede sobreajustarse al ruido; la confirmación no garantiza mejora.', '',
              '## Limitaciones',
              'Una sola computadora y una captura histórica; tiempos afectados por carga del sistema y cachés.',
              'Revisar normalidad de residuos y homogeneidad antes de interpretar significancia ANOVA.',
              'No se ha realizado bloqueo por hora o máquina; el orden de las corridas sí fue aleatorizado.',
              'Las métricas son de rendimiento del procesamiento, no estimaciones del mercado inmobiliario.',
              'Las corridas reales y la salida del equipo que las ejecutó son la evidencia principal.']
    (OUT/'INFORME.md').write_text('\n'.join(lineas)+'\n',encoding='utf-8')
    print(json.dumps({'corridas':len(datos),'fraccion':len(fraccion),'confirmacion':len(confirma),
                      'mejora_confirmada_pct':round(mejora,2),'salida':str(OUT)},ensure_ascii=False,indent=2))

if __name__=='__main__':
    correr()
