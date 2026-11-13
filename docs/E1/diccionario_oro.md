# Diccionario de datos — Oro

- `registros_trimestrales.parquet`: `municipio` (texto), `año` (entero), `trimestre` (1-4), `viviendas` (suma de registros SNIIV mensuales por municipio y trimestre).
- `indice_shf_colima.parquet`: columnas originales SHF y `nivel_geografico` (`estatal` o `municipal`), `fecha` (inicio del trimestre).
- `comparacion_municipal.parquet`: `municipio`, `año`, `trimestre`, `viviendas`, `indice_shf` (índice, no precio monetario). Solo intersección de periodos y municipios presentes en ambas fuentes.
- `reporte_calidad.json`: procedencia y conteos de aceptados/rechazados.
