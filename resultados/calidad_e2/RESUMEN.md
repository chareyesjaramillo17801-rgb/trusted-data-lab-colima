# Resultados de calidad de datos — E2

Ejecucion UTC: 2026-11-22T23:26:53.795183+00:00

## Medicion ISO/IEC 25012 (seleccion de atributos)

| Producto | Filas | Completitud de celdas | Unicidad de filas | Origen y hash |
|---|---:|---:|---:|---:|
| registros_trimestrales | 383 | 100.0% | 100.0% | 100.0% |
| indice_shf_colima | 258 | 91.11% | 100.0% | 100.0% |
| comparacion_municipal | 131 | 100.0% | 100.0% | No evaluable |
| variables_analiticas_sniiv | 2140 | 100.0% | 100.0% | 100.0% |
| comparacion_modelos | 8 | 93.75% | 100.0% | 100.0% |
| pronosticos_exploratorios | 8 | 96.88% | 100.0% | 100.0% |
| diagnostico_ampliado | 2 | 100.0% | 100.0% | 100.0% |

## Limites de interpretacion

- La completitud global incluye nulos estructurales; revisar cada columna antes de atribuir defectos.
- Unicidad de fila completa no prueba unicidad de la clave de negocio.
- La presencia de origen/hash no demuestra por si sola integridad criptografica del linaje.
- ISO/IEC 25010 no se acredita solo con estas metricas de datos.
