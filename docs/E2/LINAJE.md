# Linaje y trazabilidad de datos — E2

**Proyecto:** TRUSTED DATA LAB — Observatorio inmobiliario de Colima

## 1. Objetivo

Documentar la procedencia de los registros utilizados en los productos de la capa Oro, desde los archivos originales de la capa Bronce, pasando por los procesos de limpieza y validación de Plata.

La trazabilidad permite identificar las fuentes de información, verificar su integridad y conocer qué observaciones históricas contribuyeron a cada resultado.

## 2. Arquitectura de datos

El procesamiento sigue tres capas:

- **Bronce:** conserva las respuestas originales de SNIIV e INEGI y el archivo Excel SHF.
- **Plata:** contiene datos normalizados, validados y enriquecidos con metadatos de procedencia.
- **Oro:** contiene productos analíticos, agregaciones, comparaciones y geometrías municipales.

Los registros rechazados por las validaciones se almacenan en la zona de cuarentena.

## 3. Campos de trazabilidad

| Campo | Descripción |
|---|---|
| `id_fila_bronce` | Identificador de una observación en su archivo original |
| `ids_filas_bronce` | Lista JSON de observaciones contribuyentes a un agregado |
| `origen_bronce` | Ruta relativa del archivo de origen |
| `sha256_bronce` | Huella SHA-256 del archivo Bronce |
| `fecha_ingesta_utc` | Fecha registrada de captura o referencia temporal disponible |
| `metodo_fecha_ingesta` | Método utilizado para determinar la fecha |
| `id_registro_oro` | Identificador del resultado derivado en Oro |

Para SNIIV, los identificadores corresponden a posiciones de la lista JSON original. Para SHF, corresponden a filas del archivo Excel original.

**Advertencia:** cuando `metodo_fecha_ingesta` tiene el valor `mtime_archivo_no_verificado`, la fecha procede de la modificación del archivo y no demuestra cuándo se descargó originalmente.

## 4. Linaje de los productos Oro

### 4.1. Índice SHF

**Archivo:** `data/oro/indice_shf_colima.parquet`

Contiene 258 registros de Colima con identificadores de fila Bronce, archivo de origen, hash SHA-256 y fecha registrada.

Incluye registros municipales y agregados estatales, conservando su nivel geográfico.

### 4.2. Registros trimestrales SNIIV

**Archivo:** `data/oro/registros_trimestrales.parquet`

Contiene 383 agregados trimestrales. Cada resultado conserva `ids_filas_bronce`, una lista JSON con los identificadores de todas las observaciones SNIIV que contribuyeron al agregado.

### 4.3. Comparación municipal

**Archivo:** `data/oro/comparacion_municipal.parquet`

Contiene 131 registros que relacionan agregados trimestrales SNIIV con el índice SHF cuando existe correspondencia municipal y temporal.

Mantiene dos ramas de trazabilidad:

- **SNIIV:** identificadores de observaciones contribuyentes, archivo de origen, hash y fecha.
- **SHF:** identificador de la observación vinculada, archivo de origen, hash y fecha.

No se atribuyen indicadores estatales a municipios individuales.

### 4.4. Variables analíticas SNIIV

**Archivo:** `data/oro/variables_analiticas_sniiv.parquet`

Contiene 2,140 observaciones enriquecidas con variables analíticas, conservando los identificadores y metadatos de procedencia de SNIIV.

### 4.5. Geometrías municipales INEGI

**Archivo:** `data/oro/municipios_colima.geojson`

Contiene geometrías de los 10 municipios de Colima obtenidas del servicio geográfico del INEGI.

Cada entidad conserva referencias al archivo Bronce, identificador de origen, huella SHA-256 y fecha registrada.

Las geometrías se utilizan para la representación cartográfica y la interacción territorial del dashboard.

## 5. Linaje de productos estadísticos

Se incorporó el módulo `pipeline/linaje_analitico_e2.py`, que añade referencias SHF a los CSV analíticos.

### 5.1. Comparación de modelos

**Archivo:** `data/oro/comparacion_modelos.csv`

Contiene 8 resultados de evaluación.

Cada resultado conserva:

- `ids_bronce_entrenamiento`: 78 observaciones históricas utilizadas para ajustar el modelo evaluado.
- `ids_bronce_prueba`: 8 observaciones utilizadas para evaluar sus predicciones.
- Archivo Bronce, SHA-256 y fecha registrada.
- `tipo_linaje`: `entrenamiento_y_prueba`.

Las cantidades se contrastaron con `periodos_entrenamiento` y `periodos_prueba`.

### 5.2. Pronósticos exploratorios

**Archivo:** `data/oro/pronosticos_exploratorios.csv`

Contiene 8 resultados correspondientes a horizontes futuros de los municipios analizados.

Cada fila conserva los 86 identificadores históricos SHF utilizados para el ajuste final del modelo.

El periodo pronosticado no es una observación real de Bronce. Las referencias corresponden a los datos históricos que sustentan el pronóstico.

La selección del modelo y las métricas de validación utilizan también una partición histórica de entrenamiento y prueba.

### 5.3. Diagnóstico ampliado

**Archivo:** `data/oro/diagnostico_ampliado.csv`

Contiene 2 resultados municipales.

Cada fila conserva las referencias a los 86 periodos históricos utilizados para los diagnósticos de la serie completa.

Las métricas de validación de modelos proceden de la evaluación histórica y deben distinguirse de las estadísticas calculadas sobre toda la serie.

## 6. Reproducibilidad

Los principales módulos utilizados son:

- `pipeline/ejecutar.py`: procesa SNIIV y SHF desde Bronce y genera productos de Plata y Oro.
- `pipeline/geoespacial_e2.py`: integra la fuente geográfica del INEGI.
- `pipeline/estadistica.py`: genera la comparación de modelos.
- `pipeline/analisis_e1.py`: genera pronósticos y diagnósticos.
- `pipeline/linaje_analitico_e2.py`: incorpora trazabilidad a los productos estadísticos.
- `pipeline/ejecutar_analisis.py`: coordina la generación estadística y la incorporación posterior del linaje.

Para regenerar los productos estadísticos y su trazabilidad:

```powershell
python -m pipeline.ejecutar_analisis
```

La regeneración de los CSV mediante los módulos estadísticos individuales puede sobrescribir las columnas añadidas de linaje. Por ello, el procedimiento reproducible documentado utiliza el ejecutor completo.

## 7. Validación

Se realizaron comprobaciones de:

- Correspondencia entre identificadores de SHF en Plata y Oro.
- Ausencia de periodos duplicados en las series municipales analizadas.
- Partición de 78 observaciones de entrenamiento y 8 de prueba.
- Referencias a 86 observaciones para pronósticos y diagnósticos.
- Existencia de rutas de origen, hashes y fechas registradas.
- Regeneración de los resultados analíticos y posterior incorporación del linaje.
- Ejecución de pruebas automáticas mediante `pytest`.

La prueba `tests/test_linaje_analitico_e2.py` compara los identificadores registrados en los CSV con los de SHF en Plata.

## 8. Limitaciones

La trazabilidad documentada identifica observaciones y archivos fuente. No sustituye un registro completo de ejecución con versiones de librerías, parámetros, semillas, configuraciones y huellas de cada artefacto generado.

Las fechas de ingesta no verificadas se mantienen explícitamente identificadas.

Los resultados estadísticos no representan observaciones futuras reales ni garantías de comportamiento del mercado inmobiliario.
## 9. Aclaración sobre metadatos SHF (revisión E2)

El archivo Bronce `data/bronce/shf/Indice_SHF_datos_abiertos_2_trim_2026.metadata.json` contiene `retrieved_date: 2026-11-09` y declara que corresponde a la **incorporación al proyecto**, sin hora exacta de descarga. El pipeline actual **no utiliza** ese campo al construir `fecha_ingesta_utc`: utiliza `mtime_archivo_no_verificado` como fecha de referencia. Ambos datos deben distinguirse; no debe inferirse una hora UTC de captura a partir de la fecha de incorporación.

La operación `pipeline/cruce_espacial_e2.py` verifica la correspondencia de puntos representativos derivados de los polígonos municipales INEGI mediante `gpd.sjoin(predicate="within")`. No agrega registros inmobiliarios nuevos ni puntos de viviendas.
