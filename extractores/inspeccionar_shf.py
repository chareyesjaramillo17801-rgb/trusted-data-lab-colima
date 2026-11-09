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

    print("=" * 65)
    print("ANÁLISIS DE COBERTURA - SHF")
    print("=" * 65)

    print(f"Total de registros: {len(datos)}")

    estados = Counter(
        str(r["Estado"]).strip()
        for r in datos
        if r.get("Estado") not in (None, "")
    )

    print("\nESTADOS ENCONTRADOS:")
    for estado, cantidad in sorted(estados.items()):
        print(f"  {estado}: {cantidad}")

    municipios = Counter(
        str(r["Municipio"]).strip()
        for r in datos
        if r.get("Municipio") not in (None, "")
    )

    print(f"\nTotal de municipios identificados: {len(municipios)}")

    colima = [
        r for r in datos
        if str(r.get("Estado", "")).strip().lower() == "colima"
    ]

    print(f"\nREGISTROS DEL ESTADO DE COLIMA: {len(colima)}")

    if colima:
        municipios_colima = sorted({
            str(r["Municipio"]).strip()
            for r in colima
            if r.get("Municipio") not in (None, "")
        })

        print("\nMUNICIPIOS DE COLIMA:")
        for municipio in municipios_colima:
            print(f"  {municipio}")

        periodos = sorted({
            (r["Año"], r["Trimestre"])
            for r in colima
            if r.get("Año") is not None
            and r.get("Trimestre") is not None
        })

        print(f"\nPeriodos año-trimestre de Colima: {len(periodos)}")

        por_anio = Counter(anio for anio, trimestre in periodos)

        print("\nPERIODOS POR AÑO:")
        for anio in sorted(por_anio):
            print(f"  {anio}: {por_anio[anio]} trimestres")

    else:
        print("No se encontraron registros con Estado = Colima.")

    print("\nVALORES FALTANTES:")
    for columna in encabezados:
        faltantes = sum(
            1 for r in datos
            if r.get(columna) is None
        )
        print(f"  {columna}: {faltantes}")

    libro.close()

    print("\nANÁLISIS TERMINADO")
    print("=" * 65)


if __name__ == "__main__":
    main()
