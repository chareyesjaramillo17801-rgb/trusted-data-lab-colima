
"""Funciones de limpieza para la capa Plata de TRUSTED DATA LAB."""

import unicodedata

import pandas as pd


def normalizar_texto(valor):
    """Normaliza espacios y Unicode, conservando los acentos."""
    if pd.isna(valor):
        return pd.NA

    texto = unicodedata.normalize("NFC", str(valor))
    texto = " ".join(texto.strip().split())

    return texto if texto else pd.NA


def normalizar_columnas_texto(df, columnas):
    """Normaliza columnas sin modificar el DataFrame original."""
    resultado = df.copy()

    for columna in columnas:
        if columna not in resultado.columns:
            raise KeyError(f"Columna inexistente: {columna}")

        resultado[columna] = resultado[columna].map(normalizar_texto)

    return resultado
