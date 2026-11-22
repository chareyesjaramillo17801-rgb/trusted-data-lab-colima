"""Validacion espacial reproducible de municipios de Colima.

Los puntos son derivados de poligonos oficiales INEGI.
No representan ubicaciones de viviendas.
"""
from pathlib import Path

import geopandas as gpd

ROOT = Path(__file__).resolve().parents[1]


def validar_cruce_espacial(ruta_geojson=None):
    """Comprobar correspondencia espacial de los municipios mediante sjoin."""
    ruta = Path(ruta_geojson) if ruta_geojson else ROOT / "data/oro/municipios_colima.geojson"
    municipios = gpd.read_file(ruta)

    if municipios.crs is None:
        raise ValueError("El GeoJSON no tiene sistema de coordenadas definido")
    if municipios["cvegeo"].isna().any() or municipios["cvegeo"].duplicated().any():
        raise ValueError("Claves municipales nulas o duplicadas")
    if municipios.geometry.isna().any() or municipios.geometry.is_empty.any():
        raise ValueError("Geometrias municipales nulas o vacias")
    if not municipios.geometry.is_valid.all():
        raise ValueError("Existen geometrias municipales invalidas")
    if len(municipios) != 10:
        raise ValueError("Se esperaban exactamente 10 municipios de Colima")

    puntos = gpd.GeoDataFrame(
        {"cvegeo_origen": municipios["cvegeo"].to_numpy()},
        geometry=municipios.geometry.representative_point().to_numpy(),
        crs=municipios.crs,
    )

    poligonos = municipios[["cvegeo", "geometry"]].copy()

    cruce = gpd.sjoin(
        puntos,
        poligonos,
        how="left",
        predicate="within",
    )

    if len(cruce) != 10:
        raise ValueError("El cruce espacial produjo un numero inesperado de relaciones")
    if cruce["cvegeo"].isna().any():
        raise ValueError("Hay puntos sin municipio asociado")
    if not (cruce["cvegeo_origen"] == cruce["cvegeo"]).all():
        raise ValueError("El cruce espacial no coincide con las claves municipales")

    return cruce


if __name__ == "__main__":
    resultado = validar_cruce_espacial()
    print(f"Cruce espacial validado: {len(resultado)} municipios")
    print(resultado[["cvegeo_origen", "cvegeo"]].to_string(index=False))
