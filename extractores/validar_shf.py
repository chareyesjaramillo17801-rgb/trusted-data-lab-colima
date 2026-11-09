
from pathlib import Path
from collections import Counter
from openpyxl import load_workbook

ARCHIVO = Path(
    "data/bronce/shf/Indice_SHF_datos_abiertos_2_trim_2026.xlsx"
)


def main():
    if not ARCHIVO.exists():
        raise FileNotFoundError(f"No se encontró: {ARCHIVO}")

    libro = load_workbook(
        ARCHIVO,
        read_only=True,
        data_only=True
    )

    hoja = libro.active
    filas = hoja.iter_rows(values_only=True)
    encabezados = next(filas)

    datos = [
        dict(zip(encabezados, fila))
        for fila in filas
        if any(valor is not None for valor in fila)
    ]

    # Registros del estado de Colima
    colima = [
        r for r in datos
        if str(r.get("Estado", "")).strip().lower() == "colima"
    ]

    # Duplicados de filas completas
    filas_completas = [
        tuple(r.get(c) for c in encabezados)
        for r in colima
    ]

    duplicados_exactos = (
        len(filas_completas) - len(set(filas_completas))
    )

    # Duplicados por combinación de dimensiones
    claves = [
        (
            r.get("Año"),
            r.get("Trimestre"),
            r.get("Estado"),
            r.get("Municipio"),
            r.get("Global")
        )
        for r in colima
    ]

    conteo_claves = Counter(claves)
    duplicados_clave = sum(
        cantidad - 1
        for cantidad in conteo_claves.values()
        if cantidad > 1
    )

    # Periodos disponibles en Colima
    periodos_colima = sorted({
        (r["Año"], r["Trimestre"])
        for r in colima
        if r.get("Año") is not None
        and r.get("Trimestre") is not None
    })

    municipios = sorted({
        str(r["Municipio"]).strip()
        for r in colima
        if r.get("Municipio") not in (None, "")
    })

    print("=" * 65)
    print("VALIDACIÓN DE CALIDAD - SHF")
    print("=" * 65)

    print(f"Registros totales del archivo: {len(datos)}")
    print(f"Registros de Colima: {len(colima)}")

    print("\nDUPLICADOS:")
    print(f"Filas completamente duplicadas: {duplicados_exactos}")
    print(f"Claves dimensionales duplicadas: {duplicados_clave}")

    print("\nCOBERTURA POR MUNICIPIO:")

    for municipio in municipios:
        registros = [
            r for r in colima
            if str(r.get("Municipio", "")).strip() == municipio
        ]

        periodos = sorted({
            (r["Año"], r["Trimestre"])
            for r in registros
            if r.get("Año") is not None
            and r.get("Trimestre") is not None
        })

        faltantes = sorted(set(periodos_colima) - set(periodos))

        print(f"\nMunicipio: {municipio}")
        print(f"  Registros: {len(registros)}")
        print(f"  Periodos disponibles: {len(periodos)}")
        print(f"  Periodos faltantes respecto a Colima: {len(faltantes)}")

        if faltantes:
            print(f"  Detalle de faltantes: {faltantes}")

    print("\nVALORES FALTANTES EN REGISTROS DE COLIMA:")

    for columna in encabezados:
        faltantes = sum(
            1 for r in colima
            if r.get(columna) is None
        )
        print(f"  {columna}: {faltantes}")

    libro.close()

    print("\nVALIDACIÓN TERMINADA")
    print("=" * 65)


if __name__ == "__main__":
    main()
