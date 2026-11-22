# Ficha de entrega E2 — TRUSTED DATA LAB

**Proyecto:** Observatorio inmobiliario de Colima
**Entrega:** E2 — Integración especializada, ética y trazabilidad
**Estado:** implementación local validada; pendiente cierre documental, publicación y tag `e2`.

## 1. Integración de fuente especializada

Se integró el Marco Geoestadístico del INEGI mediante su servicio web de información vectorial municipal.

- **Fuente:** Instituto Nacional de Estadística y Geografía (INEGI).
- **Endpoint:** https://gaia.inegi.org.mx/wscatgeo/v2/geo/mgem/06
- **Procesamiento:** `pipeline/geoespacial_e2.py`.
- **Captura:** archivo original conservado en `data/bronce/inegi/`.
- **Producto Oro:** `data/oro/municipios_colima.geojson`.
- **Resultado:** 10 municipios de Colima con geometrías geográficas.
- **Visualización:** sección interactiva del mapa en `dashboard/app.py`.

El mapa permite explorar los municipios, seleccionar polígonos y consultar indicadores disponibles. La cartografía proviene del servicio oficial del INEGI; los indicadores dependen de la cobertura real de SNIIV y SHF.

## 2. Integración y calidad de datos

La ejecución del pipeline produjo los siguientes resultados:

| Indicador | Resultado |
|---|---:|
| Registros SNIIV procesados | 2,140 |
| Registros SNIIV válidos | 2,140 |
| Registros SNIIV rechazados | 0 |
| Registros SHF Colima procesados | 258 |
| Registros SHF válidos | 258 |
| Registros SHF rechazados | 0 |
| Comparaciones municipales Oro | 131 |
| Municipios con geometría INEGI | 10 |

Las diferencias de cobertura entre fuentes se mantienen explícitas. Los municipios con geometría disponible no necesariamente tienen indicadores SHF municipales.

## 3. Trazabilidad Bronce → Plata → Oro

Se incorporó linaje por registro en los productos principales de Oro, incluyendo identificadores de origen, rutas de archivos Bronce, huellas SHA-256 y fechas de ingesta registradas.

Los agregados SNIIV conservan las listas de registros contribuyentes. Las comparaciones municipales conservan referencias separadas para SNIIV y SHF.

También se incorporó trazabilidad a los productos analíticos:

- `comparacion_modelos.csv`: 8 resultados, con referencias a 78 periodos de entrenamiento y 8 de prueba por resultado.
- `pronosticos_exploratorios.csv`: 8 resultados, con referencias a los 86 periodos históricos de cada municipio.
- `diagnostico_ampliado.csv`: 2 resultados, con referencias a los 86 periodos históricos de cada municipio.

Los módulos `pipeline/linaje_analitico_e2.py` y `pipeline/ejecutar_analisis.py` permiten regenerar los resultados analíticos junto con sus referencias.

**Limitación:** la fecha de ingesta SHF se obtuvo de la fecha de modificación del archivo, no de metadatos de captura verificados. Los identificadores documentan la procedencia de los datos históricos; no constituyen por sí solos un registro completo de parámetros y versiones de ejecución de cada modelo.

La descripción técnica se encuentra en `docs/E2/LINAJE.md`.

## 4. Ética y legalidad

Se elaboró `docs/etica-datos.md`, que documenta fuentes, minimización de datos personales, sesgos, límites de interpretación y trazabilidad.

**Pendiente de cierre:** registrar los resultados verificables de la revisión de licencias, términos de uso y archivos `robots.txt` de las fuentes.

## 5. Evidencias de validación

- Captura y procesamiento geoespacial: 10 municipios obtenidos.
- Mapa interactivo: probado localmente con selección de municipios y navegación.
- Pipeline de calidad: ejecutado con 2,140 registros SNIIV válidos y 258 SHF válidos.
- Linaje analítico: comprobadas las particiones de entrenamiento y prueba y la correspondencia con identificadores SHF.
- Ruff: verificaciones aprobadas.
- Pytest: 11 pruebas aprobadas, según la última ejecución reportada.
- Publicación actualizada del dashboard: pendiente de comprobar.
- Commit final E2: pendiente.
- Tag `e2`: pendiente.
- URL de entrega: pendiente.

## 6. Limitaciones

Los registros SNIIV no representan anuncios de vivienda disponibles en renta. El índice SHF no representa precios de renta ni precios individuales de inmuebles.

Los pronósticos son exploratorios y están condicionados a los datos y supuestos de los modelos. No deben presentarse como predicciones garantizadas.

La cobertura SHF municipal utilizada para los análisis corresponde a Manzanillo y Villa de Álvarez; los registros SHF estatales no deben atribuirse al municipio de Colima.

## 7. Cierre

La implementación técnica local y las pruebas se encuentran realizadas. La entrega E2 se considerará cerrada después de documentar las verificaciones legales pendientes, comprobar la publicación final, registrar el commit y crear el tag `e2`.