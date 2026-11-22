
"""Ejecuta los analisis estadisticos y agrega linaje E2."""

from pipeline.analisis_e1 import run
from pipeline.estadistica import analizar
from pipeline.linaje_analitico_e2 import agregar_linaje


def principal():
    print("1/3 Generando comparacion de modelos...")
    analizar()

    print("2/3 Generando pronosticos y diagnosticos...")
    run()

    print("3/3 Incorporando linaje analitico E2...")
    agregar_linaje()

    print("Analisis y linaje E2 completados.")


if __name__ == "__main__":
    principal()
