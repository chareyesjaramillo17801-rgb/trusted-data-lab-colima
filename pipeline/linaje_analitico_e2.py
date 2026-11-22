
"""Trazabilidad de productos analiticos SHF de la capa Oro."""

import json
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
PLATA = ROOT / "data" / "plata"
ORO = ROOT / "data" / "oro"

PRODUCTOS = (
    "comparacion_modelos.csv",
    "pronosticos_exploratorios.csv",
    "diagnostico_ampliado.csv",
)

COLUMNAS_LINAJE = (
    "ids_bronce_entrenamiento",
    "ids_bronce_prueba",
    "origen_bronce",
    "sha256_bronce",
    "fecha_ingesta_utc",
    "metodo_fecha_ingesta",
    "cantidad_registros_shf",
    "tipo_linaje",
)


def _serializar_ids(datos):
    return json.dumps(
        datos["id_fila_bronce"].astype(str).tolist(),
        ensure_ascii=False,
    )


def _referencias(datos, nombre):
    if nombre == "comparacion_modelos.csv":
        entrenamiento = datos.iloc[:-8]
        prueba = datos.iloc[-8:]
        tipo = "entrenamiento_y_prueba"
    else:
        entrenamiento = datos
        prueba = datos.iloc[0:0]
        tipo = "serie_completa"

    if entrenamiento.empty:
        raise ValueError("No hay registros de entrenamiento")

    for columna in (
        "origen_bronce",
        "sha256_bronce",
        "fecha_ingesta_utc",
        "metodo_fecha_ingesta",
    ):
        if datos[columna].isna().any():
            raise ValueError(f"Linaje incompleto: {columna}")

        if datos[columna].nunique() != 1:
            raise ValueError(
                f"Hay multiples valores para {columna}"
            )

    return {
        "ids_bronce_entrenamiento": _serializar_ids(entrenamiento),
        "ids_bronce_prueba": _serializar_ids(prueba),
        "origen_bronce": datos["origen_bronce"].iloc[0],
        "sha256_bronce": datos["sha256_bronce"].iloc[0],
        "fecha_ingesta_utc": datos["fecha_ingesta_utc"].iloc[0],
        "metodo_fecha_ingesta": datos["metodo_fecha_ingesta"].iloc[0],
        "cantidad_registros_shf": len(datos),
        "tipo_linaje": tipo,
    }


def agregar_linaje():
    shf = pd.read_parquet(PLATA / "shf_colima.parquet")
    anio = "A\u00f1o"

    requeridas = {
        "Municipio",
        anio,
        "Trimestre",
        "id_fila_bronce",
        "origen_bronce",
        "sha256_bronce",
        "fecha_ingesta_utc",
        "metodo_fecha_ingesta",
    }

    faltantes = requeridas - set(shf.columns)
    if faltantes:
        raise ValueError(
            f"Faltan columnas SHF: {sorted(faltantes)}"
        )

    referencias_por_municipio = {}

    for municipio in ("Manzanillo", "Villa de Álvarez"):
        datos = (
            shf.loc[shf["Municipio"].eq(municipio)]
            .sort_values([anio, "Trimestre"])
        )

        if len(datos) != 86:
            raise ValueError(
                f"{municipio}: se esperaban 86 periodos; "
                f"se encontraron {len(datos)}"
            )

        if datos.duplicated([anio, "Trimestre"]).any():
            raise ValueError(
                f"{municipio}: periodos duplicados"
            )

        if datos["id_fila_bronce"].isna().any():
            raise ValueError(
                f"{municipio}: identificadores Bronce faltantes"
            )

        referencias_por_municipio[municipio] = datos

    resultados = {}

    # Preparar todos los archivos antes de escribir alguno.
    for nombre in PRODUCTOS:
        ruta = ORO / nombre

        if not ruta.exists():
            raise FileNotFoundError(ruta)

        df = pd.read_csv(ruta)

        if "municipio" not in df.columns:
            raise ValueError(
                f"{nombre}: falta columna municipio"
            )

        referencias = []

        for municipio in df["municipio"]:
            if municipio not in referencias_por_municipio:
                raise ValueError(
                    f"{nombre}: municipio desconocido {municipio}"
                )

            datos = referencias_por_municipio[municipio]
            referencias.append(_referencias(datos, nombre))

        df = df.drop(
            columns=list(COLUMNAS_LINAJE),
            errors="ignore",
        )

        # Eliminar columna de la version preliminar.
        df = df.drop(
            columns=["ids_bronce_entrenamiento"],
            errors="ignore",
        )

        resultado = pd.concat(
            [
                df.reset_index(drop=True),
                pd.DataFrame(referencias),
            ],
            axis=1,
        )

        resultados[nombre] = resultado

    for nombre, resultado in resultados.items():
        resultado.to_csv(
            ORO / nombre,
            index=False,
            encoding="utf-8-sig",
        )

        print(
            f"{nombre}: {len(resultado)} filas "
            "con linaje diferenciado"
        )


if __name__ == "__main__":
    agregar_linaje()
