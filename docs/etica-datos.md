# Declaración de ética y legalidad — TRUSTED DATA LAB (E2)

**Proyecto:** Observatorio inmobiliario de Colima
**Fecha de revisión:** 22 de noviembre de 2026
**Uso:** académico y exploratorio.

## 1. Fuentes de información

El observatorio integra tres fuentes institucionales:

| Fuente | Información utilizada | Finalidad |
|---|---|---|
| SNIIV / SEDATU | Registros históricos de vivienda | Análisis de actividad habitacional |
| Sociedad Hipotecaria Federal (SHF) | Índice de precios de la vivienda | Análisis de tendencias históricas |
| INEGI | Marco Geoestadístico municipal | Visualización territorial |

No se utilizan publicaciones privadas de renta ni datos personales de propietarios.

## 2. Condiciones de uso y atribución

### INEGI

Se consultó la documentación oficial del Servicio Web del Catálogo Único de Claves Geoestadísticas:

https://www.inegi.org.mx/servicios/catalogounico.html

La documentación describe el consumo programático de información geográfica en formato GeoJSON.

También se revisaron los términos de libre uso:

https://www.inegi.org.mx/inegi/terminos.html

Estos permiten copiar, adaptar, publicar y utilizar comercialmente información del INEGI, bajo condiciones que incluyen conservar metadatos, otorgar atribución y no presentar los productos derivados como avalados oficialmente por el Instituto.

**Atribución utilizada:** Fuente: INEGI, Marco Geoestadístico, Servicio Web del Catálogo Único de Claves Geoestadísticas.

El observatorio y sus análisis son desarrollos independientes y no representan una postura oficial del INEGI.

### SHF

Se utiliza el archivo de datos abiertos del Índice SHF de Precios de la Vivienda, correspondiente al segundo trimestre de 2026.

Publicación institucional:

https://www.gob.mx/shf/documentos/indice-shf-de-precios-de-la-vivienda-en-mexico-2025-a-2026

Se reconoce a Sociedad Hipotecaria Federal como fuente de los datos. La denominación «datos abiertos» identifica la publicación institucional, pero no se interpreta como autorización ilimitada para cualquier forma de redistribución.

**Fundamento normativo de reutilización:** se revisaron los Lineamientos en materia de Datos Abiertos de la Administración Pública Federal, publicados en el Diario Oficial de la Federación:

https://sidof.segob.gob.mx/notas/docFuente/5767742

Su artículo 1 incluye a las instituciones nacionales de crédito; el artículo 5, fracción X, establece la atribución de la fuente como requisito de libre uso de los datos abiertos; y el artículo 6 contempla su acceso, reutilización y redistribución.

El Índice SHF se encuentra publicado institucionalmente como recurso de datos abiertos. Por ello, se documenta su utilización bajo este marco general, conservando la atribución a Sociedad Hipotecaria Federal, la procedencia y las transformaciones realizadas.

**Limitación:** no se identificó una licencia individual explícita en el archivo Excel consultado. No se atribuye al archivo una licencia específica que no haya sido verificada.

### SNIIV / SEDATU

Se utiliza una API institucional para obtener registros históricos de vivienda. Se conservan las respuestas originales y metadatos de procedencia.

Se consultó la página oficial de datos abiertos del SNIIV:

https://sniiv.sedatu.gob.mx/Reporte/Datos_abiertos

En los metadatos del conjunto **Registro de Vivienda**, SEDATU establece acceso público por internet y señala que su utilización no tiene restricciones siempre que se mencione la fuente.

La captura utilizada en este proyecto procede de la API SNIIV Registro de Vivienda, con respuesta HTTP 200 y 2,140 registros, según los metadatos Bronce del 13 de noviembre de 2026.

**Atribución:** Fuente: SEDATU, Sistema Nacional de Información e Indicadores de Vivienda (SNIIV), Registro de Vivienda.

No se asigna una licencia Creative Commons específica porque no se identificó una denominación de licencia en los metadatos consultados.

## 3. Revisión de robots.txt

**Fecha de consulta:** 22 de noviembre de 2026.
**Método:** solicitudes HTTP mediante PowerShell `Invoke-WebRequest`.

| Dirección consultada | Resultado | Observaciones |
|---|---|---|
| https://www.inegi.org.mx/robots.txt | HTTP 200 | Contiene reglas generales `User-agent: *`; incluye `Allow: /servicios` y restricciones sobre rutas específicas de catálogo y metadatos |
| https://gaia.inegi.org.mx/robots.txt | HTTP 404 | No se encontró el archivo en la dirección consultada |
| https://www.gob.mx/robots.txt | HTTP 200 | Se observaron reglas dirigidas a robots de Google, con campos `Disallow` vacíos |
| https://sniiv.sedatu.gob.mx/robots.txt | HTTP 404 | No se encontró el archivo en la dirección consultada |

El archivo `robots.txt` de `www.inegi.org.mx` no se considera aplicable automáticamente al subdominio `gaia.inegi.org.mx`.

Un resultado HTTP 404 no constituye por sí mismo una autorización ni una prohibición de acceso automatizado.

La revisión de `robots.txt` tampoco sustituye los términos legales de cada fuente.

## 4. Acceso responsable

La integración geográfica utiliza un endpoint documentado por el INEGI y una consulta específica para obtener los municipios de Colima.

El proyecto no implementa rastreo masivo de páginas web para recopilar anuncios particulares.

Las capturas originales se conservan en Bronce, junto con los metadatos disponibles para comprobar su procedencia.

Se deben respetar las condiciones de uso, evitar solicitudes excesivas y revisar cambios en los servicios institucionales.

## 5. Privacidad y minimización

No se publican nombres, teléfonos, direcciones particulares ni información que identifique a propietarios o arrendatarios.

Las geometrías utilizadas representan municipios, no domicilios individuales.

La información de entrevistas, cuando se documenta, debe mantenerse anonimizada y limitarse a los hallazgos necesarios para el análisis.

## 6. Sesgos y limitaciones

- Los registros SNIIV no representan toda la oferta inmobiliaria ni la disponibilidad actual de viviendas en renta.
- El índice SHF mide variaciones de precios de vivienda y no equivale a precios monetarios de alquiler.
- La cobertura municipal de SHF es diferente de la cobertura geográfica del INEGI.
- La ausencia de datos no se interpreta como ausencia de actividad inmobiliaria.
- Las comparaciones territoriales no demuestran relaciones causales.
- Los pronósticos son exploratorios y están sujetos a incertidumbre y errores de estimación.

## 7. Trazabilidad e integridad

Los productos de Oro conservan referencias a registros Bronce, rutas de origen, hashes SHA-256 y fechas registradas.

Los agregados documentan sus observaciones contribuyentes y los productos estadísticos conservan referencias a las series históricas utilizadas.

Cuando la fecha de ingesta procede de la modificación del archivo SHF, se identifica expresamente como no verificada.

La documentación técnica se encuentra en `docs/E2/LINAJE.md`.

## 8. Riesgos y medidas de mitigación

| Riesgo | Medida |
|---|---|
| Interpretar índices como precios de renta | Incluir advertencias metodológicas |
| Atribuir datos estatales a municipios | Conservar el nivel geográfico original |
| Pérdida de procedencia | Mantener identificadores, rutas y hashes |
| Exposición de información personal | Utilizar datos agregados y evitar identificadores personales |
| Cambios en servicios externos | Documentar URL, fecha de consulta y resultados |
| Reutilización sin atribución | Reconocer expresamente las instituciones fuente |

## 9. Estado de cumplimiento

**Verificado:** documentación de la API geográfica del INEGI; términos generales de libre uso del INEGI; condiciones publicadas para Registro de Vivienda del SNIIV; publicación institucional del Índice SHF como datos abiertos; fundamento normativo federal aplicable a datos abiertos; consultas HTTP a cuatro direcciones `robots.txt`; y trazabilidad técnica local.

**Limitaciones documentadas:** no se identificó una licencia individual específica del archivo SHF. Las respuestas HTTP 404 de `robots.txt` no se interpretan como permisos ni prohibiciones. Las condiciones de acceso deberán revisarse nuevamente si cambian los servicios o se amplía la extracción.

Esta declaración documenta las comprobaciones efectuadas, sin constituir una certificación jurídica.
## 10. Alcance del cruce espacial E2

La comprobación `pipeline/cruce_espacial_e2.py` genera puntos representativos de polígonos oficiales y verifica con `gpd.sjoin()` que correspondan a los municipios de origen. Estos puntos **no representan inmuebles, domicilios ni casos individuales**. La validación no autoriza inferir distribución intramunicipal de precios o rentas.
