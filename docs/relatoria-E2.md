# Relatoría E2 — TRUSTED DATA LAB

**Proyecto:** Observatorio inmobiliario de Colima
**Entrega:** E2 — Integración especializada, ética y trazabilidad
**Modalidad:** Trabajo individual
**Estado:** implementación técnica validada localmente; cierre documental y publicación pendientes.

## 1. Objetivo de la entrega

Ampliar el observatorio inmobiliario de Colima mediante la integración de una fuente de información especializada, fortalecer la trazabilidad de los datos desde Bronce hasta Oro y documentar las consideraciones éticas y legales relacionadas con su utilización.

Se eligió la alternativa geoespacial para incorporar información territorial oficial y mejorar la exploración de los indicadores inmobiliarios.

## 2. Actividades realizadas

### 2.1. Integración del Marco Geoestadístico del INEGI

Se incorporó información geográfica municipal del estado de Colima mediante el servicio web oficial del INEGI.

Se desarrolló el módulo `pipeline/geoespacial_e2.py`, encargado de procesar la información geográfica y generar el producto `data/oro/municipios_colima.geojson`.

**Resultado:** se obtuvieron 10 municipios con geometrías válidas, conservando referencias a la captura original en Bronce.

### 2.2. Desarrollo del mapa interactivo

Se incorporó una sección cartográfica en `dashboard/app.py`.

El mapa permite visualizar los límites municipales, acercar y alejar la vista, explorar calles mediante OpenStreetMap y seleccionar municipios directamente sobre sus polígonos.

Al seleccionar un municipio, se actualiza la información disponible en el panel.

La visualización se probó localmente. La publicación actualizada en Streamlit Cloud permanece pendiente de comprobación.

### 2.3. Fortalecimiento del linaje de datos

Se verificó la trazabilidad de los productos principales de Oro, incluyendo registros SHF, agregados SNIIV, comparaciones municipales y variables analíticas.

Se conservaron identificadores de observaciones originales, rutas Bronce, hashes SHA-256 y fechas registradas.

Para los agregados se conservaron los identificadores de las observaciones contribuyentes.

### 2.4. Incorporación de linaje analítico

Se identificó que los archivos CSV de modelos, pronósticos y diagnósticos no conservaban referencias a las observaciones históricas utilizadas.

Se desarrolló `pipeline/linaje_analitico_e2.py` para incorporar dichas referencias.

Los resultados fueron:

| Producto | Resultados | Referencias históricas |
|---|---:|---|
| Comparación de modelos | 8 | 78 entrenamiento y 8 prueba |
| Pronósticos exploratorios | 8 | 86 observaciones por resultado |
| Diagnóstico ampliado | 2 | 86 observaciones por resultado |

Se verificó que los identificadores registrados correspondieran a los datos SHF de Plata.

### 2.5. Automatización de análisis

Se creó `pipeline/ejecutar_analisis.py` para coordinar la ejecución de los modelos estadísticos y la posterior incorporación de su linaje.

Esto permite regenerar los productos analíticos siguiendo un orden definido, sin modificar las fórmulas originales de los modelos.

### 2.6. Validación automatizada

Se incorporó `tests/test_linaje_analitico_e2.py` para comprobar la correspondencia de los identificadores Bronce con los registros históricos SHF.

Durante las pruebas se detectó que una prueba existente de E1 regeneraba los CSV y sobrescribía las columnas de trazabilidad.

Se corrigió la interacción entre las pruebas E1 y E2 para conservar el linaje después de la regeneración.

**Resultado reportado:** verificaciones de Ruff correctas y 11 pruebas automatizadas aprobadas.

## 3. Problemas encontrados y soluciones

| Problema | Solución |
|---|---|
| Incompatibilidad al escribir GeoJSON mediante componentes geoespaciales del entorno local | Se utilizó una serialización GeoJSON compatible con el entorno |
| Mapa con fondo cartográfico que solicitaba clave de API | Se configuró OpenStreetMap |
| Selección municipal inicialmente separada del mapa | Se implementó selección interactiva mediante clic en polígonos |
| CSV estadísticos sin trazabilidad | Se incorporaron identificadores de observaciones históricas |
| Pérdida de linaje durante las pruebas E1 | Se ajustó la secuencia de regeneración y restauración del linaje |
| Problemas de codificación de la columna `Año` en comandos PowerShell | Se utilizaron secuencias Unicode en las comprobaciones |

## 4. Decisiones técnicas

Se conservaron las capas Bronce, Plata y Oro y la zona de cuarentena establecidas previamente.

No se modificaron los cálculos estadísticos de E1 para agregar trazabilidad.

Se mantuvieron separados los registros municipales y estatales de SHF para evitar comparaciones geográficas incorrectas.

La cartografía utiliza geometrías oficiales del INEGI, sin inventar límites municipales ni coordenadas.

Los registros SNIIV y el índice SHF se presentan como indicadores históricos, no como inventario de inmuebles disponibles para renta.

## 5. Consideraciones éticas

El proyecto utiliza información pública institucional y evita incorporar datos personales de propietarios, arrendatarios o entrevistados en la visualización.

Se reconocen las diferencias de cobertura entre fuentes, los límites de interpretación de los indicadores y los supuestos de los pronósticos.

La declaración se encuentra en `docs/etica-datos.md`.

La revisión específica de términos, licencias y `robots.txt` debe cerrarse con evidencia verificable antes de la entrega final.

## 6. Resultados alcanzados

- Integración geográfica de 10 municipios de Colima.
- Mapa municipal interactivo probado localmente.
- Procesamiento validado de 2,140 registros SNIIV y 258 SHF.
- Generación de 131 comparaciones municipales.
- Trazabilidad de los productos principales de Oro.
- Referencias históricas incorporadas a modelos, diagnósticos y pronósticos.
- Pruebas automatizadas aprobadas.

## 7. Limitaciones y trabajo pendiente

La cobertura municipal de SHF es limitada y no debe confundirse con la cobertura territorial del mapa.

Las fechas SHF basadas en la modificación del archivo no equivalen a fechas de captura verificadas.

Los resultados estadísticos son exploratorios y no garantizan valores futuros.

Antes del cierre E2 se requiere completar la evidencia de condiciones de uso de las fuentes, verificar la publicación final del dashboard, registrar el commit y crear el tag `e2`.

## 8. Conclusión

La entrega E2 amplió el observatorio con una dimensión geoespacial y fortaleció la capacidad de rastrear los resultados hasta sus fuentes originales.

La incorporación del mapa interactivo facilita la exploración territorial, mientras que la trazabilidad de los productos analíticos permite revisar qué observaciones históricas sustentan los indicadores y pronósticos.

La implementación local fue validada mediante ejecución y pruebas automatizadas. El cierre definitivo depende de completar las verificaciones documentales y la publicación final.