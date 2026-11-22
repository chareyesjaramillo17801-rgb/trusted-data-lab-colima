
"""Pruebas de trazabilidad de productos analiticos E2."""

import json
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
ORO = ROOT / "data" / "oro"
PLATA = ROOT / "data" / "plata"

PRODUCTOS = {
    "comparacion_modelos.csv": (78, 8),
    "pronosticos_exploratorios.csv": (86, 0),
    "diagnostico_ampliado.csv": (86, 0),
}


def test_linaje_analitico_e2():
    shf = pd.read_parquet(PLATA / "shf_colima.parquet")
    anio = "A\u00f1o"

    for nombre, (n_train, n_test) in PRODUCTOS.items():
        df = pd.read_csv(ORO / nombre)

        assert not df.empty, nombre

        for _, fila in df.iterrows():
            municipio = fila["municipio"]

            datos = (
                shf.loc[shf["Municipio"].eq(municipio)]
                .sort_values([anio, "Trimestre"])
            )

            assert len(datos) == 86, (nombre, municipio)

            entrenamiento = json.loads(
                fila["ids_bronce_entrenamiento"]
            )
            prueba = json.loads(
                fila["ids_bronce_prueba"]
            )

            ids_esperados = datos[
                "id_fila_bronce"
            ].astype(str).tolist()

            assert len(entrenamiento) == n_train
            assert len(prueba) == n_test
            assert entrenamiento + prueba == ids_esperados

            assert fila["origen_bronce"] == (
                datos["origen_bronce"].iloc[0]
            )
            assert fila["sha256_bronce"] == (
                datos["sha256_bronce"].iloc[0]
            )
            assert fila["fecha_ingesta_utc"] == (
                datos["fecha_ingesta_utc"].iloc[0]
            )

            assert len(set(entrenamiento + prueba)) == 86
