# Validación de calidad – SNIIV Registro de Vivienda

## 1. Identificación de la fuente

- **Fuente:** Sistema Nacional de Información e Indicadores de Vivienda (SNIIV).
- **Institución:** Secretaría de Desarrollo Agrario, Territorial y Urbano (SEDATU).
- **Conjunto:** Registro de Vivienda.
- **Tipo de captura:** Automatizada mediante API.
- **URL:** https://sniiv.sedatu.gob.mx/api/CuboAPI/GetRegistro/2010,2026/06/000/anio,mes,estado,municipio,segmento

## 2. Resultados de captura

- Registros obtenidos: 2,140.
- Columnas: 8.
- Municipios identificados: 8.
- Periodo histórico: 2010–2026.
- Periodos año-mes únicos: 200.

## 3. Resultados de calidad

| Indicador | Resultado |
|---|---:|
| Valores faltantes | 0 |
| Registros duplicados | 0 |
| Total de registros | 2,140 |
| Total de columnas | 8 |
| Municipios | 8 |

## 4. Cobertura geográfica

Municipios encontrados:

- Armería
- Colima
- Comala
- Coquimatlán
- Cuauhtémoc
- Manzanillo
- Tecomán
- Villa de Álvarez

## 5. Cobertura temporal

- 2010–2025: 12 meses por año.
- 2026: 8 meses disponibles.
- Total: 200 combinaciones únicas de año y mes.

La cobertura global supera el mínimo de 36 periodos históricos solicitado para E0. La cobertura específica por municipio y segmento queda pendiente de análisis.

## 6. Almacenamiento y reproducibilidad

Los datos originales se almacenan en `data/bronce/sniiv_registro/`.

La captura se ejecuta mediante GitHub Actions y la calidad se revisa con `extractores/validar_registro.py`.

## 7. Conclusión

La fuente presenta una estructura consistente en la captura analizada, sin valores faltantes ni registros duplicados. Su cobertura temporal permite utilizarla como insumo inicial para el observatorio inmobiliario de Colima.

La validación corresponde exclusivamente al archivo analizado y no garantiza que futuras capturas mantengan las mismas características.
