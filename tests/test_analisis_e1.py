from pipeline.analisis_e1 import run


def test_analisis_complementario_con_datos_reales():
    # Se ejecuta tras el pipeline en CI; confirma que los artefactos se generan.
    from pipeline.analisis_e1 import ROOT
    assert (ROOT/'data/plata/shf_colima.parquet').exists()
    reporte = run()
    assert 'sniiv_faltantes' in reporte
    assert (ROOT/'data/oro/pronosticos_exploratorios.csv').exists()
