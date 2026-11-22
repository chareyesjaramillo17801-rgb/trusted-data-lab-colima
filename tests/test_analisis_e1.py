
"""Prueba de analisis E1 con preservacion del linaje E2."""

from pipeline.analisis_e1 import ROOT, run
from pipeline.linaje_analitico_e2 import agregar_linaje


def test_analisis_complementario_con_datos_reales():
    # Confirmar que existen los datos preparados.
    assert (ROOT / "data/plata/shf_colima.parquet").exists()

    # Ejecutar el analisis estadistico original de E1.
    reporte = run()

    assert "sniiv_faltantes" in reporte

    # Restaurar el linaje E2 despues de regenerar los CSV.
    agregar_linaje()

    # Verificar que los productos existen.
    pronosticos = ROOT / "data/oro/pronosticos_exploratorios.csv"
    diagnostico = ROOT / "data/oro/diagnostico_ampliado.csv"

    assert pronosticos.exists()
    assert diagnostico.exists()
