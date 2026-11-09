import json
import unicodedata
from pathlib import Path
from collections import Counter


CARPETA = Path("data/bronce/sniiv_registro")


def normalizar(texto):
    texto = str(texto).strip().lower()
    texto = unicodedata.normalize("NFD", texto)
    return "".join(
        caracter for caracter in texto
        if unicodedata.category(caracter) != "Mn"
    ).replace("_", "").replace(" ", "")


def buscar_registros(objeto):
    """Encuentra la lista de registros dentro de la respuesta JSON."""
    candidatos = []

    def recorrer(elemento):
        if isinstance(elemento, list):
            if elemento and all(isinstance(x, dict) for x in elemento):
                candidatos.append(elemento)
            for item in elemento:
                recorrer(item)

        elif isinstance(elemento, dict):
            for valor in elemento.values():
                recorrer(valor)

    recorrer(objeto)

    if not candidatos:
        raise ValueError("No se encontró una lista de registros en el JSON.")

    return max(candidatos, key=len)


def buscar_columna(columnas, posibles_nombres):
    for columna in columnas:
        if normalizar(columna) in posibles_nombres:
            return columna
    return None


def main():
    archivos = sorted(
        CARPETA.glob("*.json"),
        key=lambda archivo: archivo.name,
        reverse=True
    )

    if not archivos:
        raise FileNotFoundError(
            f"No se encontraron archivos JSON en {CARPETA}"
        )

    archivo = archivos[0]
    print("=" * 60)
    print("VALIDACIÓN DE CALIDAD - SNIIV REGISTRO")
    print("=" * 60)
    print(f"Archivo analizado: {archivo.name}")

    with archivo.open("r", encoding="utf-8") as entrada:
        contenido = json.load(entrada)

    registros = buscar_registros(contenido)

    if not registros:
        raise ValueError("El archivo no contiene registros.")

    columnas = sorted({
        columna
        for registro in registros
        for columna in registro.keys()
    })

    print(f"\nTotal de registros: {len(registros)}")
    print(f"Total de columnas: {len(columnas)}")
    print(f"Columnas: {', '.join(columnas)}")

    # Valores faltantes
    nulos = Counter()
    for registro in registros:
        for columna in columnas:
            valor = registro.get(columna)
            if valor is None or (
                isinstance(valor, str) and not valor.strip()
            ):
                nulos[columna] += 1

    total_nulos = sum(nulos.values())
    print(f"\nValores faltantes: {total_nulos}")

    for columna in columnas:
        print(f"  {columna}: {nulos[columna]}")

    # Registros duplicados
    registros_serializados = [
        json.dumps(
            registro,
            sort_keys=True,
            ensure_ascii=False
        )
        for registro in registros
    ]
    duplicados = len(registros_serializados) - len(
        set(registros_serializados)
    )
    print(f"\nRegistros duplicados: {duplicados}")

    # Identificación de columnas geográficas y temporales
    columna_municipio = buscar_columna(
        columnas, {"municipio", "nombremunicipio"}
    )
    columna_anio = buscar_columna(
        columnas, {"anio", "year"}
    )
    columna_mes = buscar_columna(
        columnas, {"mes", "month"}
    )

    if columna_municipio:
        municipios = Counter(
            str(r[columna_municipio]).strip()
            for r in registros
            if r.get(columna_municipio) not in (None, "")
        )
        print("\nMUNICIPIOS ENCONTRADOS:")
        for municipio, cantidad in sorted(municipios.items()):
            print(f"  {municipio}: {cantidad}")
        print(f"Total de municipios: {len(municipios)}")
    else:
        print("\nNo se identificó la columna de municipio.")

    if columna_anio:
        anios = sorted({
            str(r[columna_anio])
            for r in registros
            if r.get(columna_anio) not in (None, "")
        })
        print(f"\nAños disponibles: {', '.join(anios)}")

    if columna_mes:
        meses = sorted({
            str(r[columna_mes])
            for r in registros
            if r.get(columna_mes) not in (None, "")
        })
        print(f"Meses disponibles: {', '.join(meses)}")

    print("\nVALIDACIÓN TERMINADA.")
    print("=" * 60)


if __name__ == "__main__":
    main()
