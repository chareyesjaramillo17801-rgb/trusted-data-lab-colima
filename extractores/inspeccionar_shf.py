
from pathlib import Path
from openpyxl import load_workbook


ARCHIVO = Path(
    "data/bronce/shf/Indice_SHF_datos_abiertos_2_trim_2026.xlsx"
)


def main():
    if not ARCHIVO.exists():
        raise FileNotFoundError(
            f"No se encontró el archivo: {ARCHIVO}"
        )

    libro = load_workbook(
        ARCHIVO,
        read_only=True,
        data_only=True
    )

    print("=" * 65)
    print("INSPECCIÓN DE ARCHIVO SHF")
    print("=" * 65)
    print(f"Archivo: {ARCHIVO.name}")
    print(f"Hojas encontradas: {len(libro.sheetnames)}")

    for nombre in libro.sheetnames:
        hoja = libro[nombre]

        print("\n" + "-" * 65)
        print(f"HOJA: {nombre}")
        print(f"Filas aproximadas: {hoja.max_row}")
        print(f"Columnas aproximadas: {hoja.max_column}")

        filas_mostradas = 0

        for fila in hoja.iter_rows(values_only=True):
            if any(valor is not None for valor in fila):
                print(fila)
                filas_mostradas += 1

            if filas_mostradas >= 6:
                break

    libro.close()

    print("\nINSPECCIÓN TERMINADA")
    print("=" * 65)


if __name__ == "__main__":
    main()
