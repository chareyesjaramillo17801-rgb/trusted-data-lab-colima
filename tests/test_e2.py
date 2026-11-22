import json

import pandas as pd

from pipeline.ejecutar import vinculos_agregacion
from pipeline.geoespacial_e2 import features_de_respuesta


def test_geojson_rechaza_respuesta_no_geojson():
    assert features_de_respuesta({'error': 'sin datos'}) == []


def test_geojson_acepta_featurecollection():
    f = {'type': 'Feature', 'properties': {}, 'geometry': {'type': 'Point', 'coordinates': [-103, 19]}}
    assert features_de_respuesta({'type': 'FeatureCollection', 'features': [f]}) == [f]


def test_linaje_agregado_conserva_todos_los_ids():
    datos = pd.DataFrame({'municipio': ['Colima', 'Colima'], 'año': [2024, 2024],
                          'trimestre': [1, 1], 'id_fila_bronce': ['sniiv:8', 'sniiv:3']})
    resultado = vinculos_agregacion(datos, ['municipio', 'año', 'trimestre'])
    assert json.loads(resultado.loc[0, 'ids_filas_bronce']) == ['sniiv:3', 'sniiv:8']

def test_cruce_espacial_municipios_colima():
    from pipeline.cruce_espacial_e2 import validar_cruce_espacial

    resultado = validar_cruce_espacial()

    assert len(resultado) == 10
    assert resultado["cvegeo"].notna().all()
    assert (resultado["cvegeo_origen"] == resultado["cvegeo"]).all()
    assert resultado["cvegeo"].nunique() == 10
