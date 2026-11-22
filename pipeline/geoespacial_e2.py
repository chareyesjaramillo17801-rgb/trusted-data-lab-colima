"""Captura verificable del Marco Geoestadístico INEGI y capa municipal E2.
Ejecutar: python -m pipeline.geoespacial_e2
"""
import hashlib
import json
from datetime import UTC, datetime
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[1]
URL = 'https://gaia.inegi.org.mx/wscatgeo/v2/geo/mgem/06'


def features_de_respuesta(payload):
    """Aceptar únicamente GeoJSON real; no generar polígonos artificiales."""
    if isinstance(payload, dict) and payload.get('type') == 'FeatureCollection':
        return payload.get('features', [])
    if isinstance(payload, dict) and payload.get('type') == 'Feature':
        return [payload]
    if isinstance(payload, list):
        salida = []
        for item in payload:
            salida.extend(features_de_respuesta(item))
        return salida
    if isinstance(payload, dict):
        for clave in ('features', 'datos', 'data', 'resultado'):
            if clave in payload:
                return features_de_respuesta(payload[clave])
    return []


def ejecutar():
    destino = ROOT / 'data/bronce/inegi'
    destino.mkdir(parents=True, exist_ok=True)
    respuesta = requests.get(URL, timeout=90, headers={'User-Agent': 'TRUSTED-DATA-LAB-academico/1.0'})
    respuesta.raise_for_status()
    contenido = respuesta.content
    payload = respuesta.json()
    fecha = datetime.now(UTC).isoformat()
    nombre = 'municipios_colima_' + datetime.now(UTC).strftime('%Y%m%dT%H%M%SZ') + '.json'
    archivo = destino / nombre
    archivo.write_bytes(contenido)
    meta = {'url': URL, 'captured_at_utc': fecha, 'status_code': respuesta.status_code,
            'sha256': hashlib.sha256(contenido).hexdigest(), 'archivo': str(archivo.relative_to(ROOT))}
    (destino / (archivo.stem + '.metadata.json')).write_text(json.dumps(meta, indent=2), encoding='utf-8')
    features = features_de_respuesta(payload)
    if not features:
        raise ValueError('La respuesta se guardó en Bronce, pero no se reconocieron polígonos GeoJSON; inspeccionar formato INEGI.')
    import geopandas as gpd
    registros = []
    for i, feature in enumerate(features):
        props = feature.get('properties') or {}
        clave = str(props.get('cvegeo') or props.get('CVEGEO') or '').zfill(5)
        if not clave.startswith('06') or len(clave) != 5:
            raise ValueError(f'Clave municipal inesperada en fila {i}: {clave}')
        if not feature.get('geometry'):
            raise ValueError(f'Sin geometría en fila {i}')
        registros.append({'cvegeo': clave, 'municipio_inegi': props.get('nomgeo') or props.get('NOMGEO'),
                          'id_fila_bronce': f'inegi:{i}', 'origen_bronce': meta['archivo'],
                          'sha256_bronce': meta['sha256'], 'fecha_ingesta_utc': fecha,
                          'geometry': feature['geometry']})
    from shapely.geometry import shape
    frame = gpd.GeoDataFrame([{**r, 'geometry': shape(r['geometry'])} for r in registros], crs='EPSG:4326')
    if frame['cvegeo'].duplicated().any() or frame.geometry.is_empty.any() or frame.geometry.isna().any():
        raise ValueError('Claves repetidas o geometrías vacías en fuente INEGI')
    if len(frame) != 10:
        raise ValueError(f'Se esperaban 10 municipios de Colima; recibidos {len(frame)}. Revisar fuente.')
    salida = ROOT / 'data/oro/municipios_colima.geojson'
    salida.parent.mkdir(parents=True, exist_ok=True)
    salida.write_text(frame.to_json(), encoding='utf-8')
    print(json.dumps({'fuente': URL, 'municipios': len(frame), 'oro': str(salida.relative_to(ROOT)), 'sha256': meta['sha256']}, ensure_ascii=False, indent=2))
    return frame


if __name__ == '__main__':
    ejecutar()
