# TRUSTED DATA LAB – Revisión ética y legalidad de fuentes

## 1. Objetivo

Documentar las condiciones de acceso, consulta, atribución y utilización de las fuentes de información empleadas por TRUSTED DATA LAB.

La revisión busca asegurar que la recopilación y el tratamiento de datos se realicen de manera responsable y respetando las condiciones publicadas por las instituciones responsables.

## 2. Fuente SNIIV – SEDATU

**Fuente oficial:** https://sniiv.sedatu.gob.mx/Reporte/Datos_abiertos

**API utilizada:** Servicio de consulta del Registro de Vivienda.

**Revisión de condiciones:**

La ficha de metadatos del portal de datos abiertos del SNIIV establece:

- Acceso público a través de internet.
- Restricciones de uso: ninguna, siempre que se mencione la fuente.
- Disponibilidad de información en formatos abiertos.
- Existencia de APIs para consultar información del sistema.

**Medidas adoptadas:**

- Identificar a SEDATU y al SNIIV como fuente de los datos.
- Conservar los archivos originales de las capturas.
- Documentar la fecha de consulta.
- No modificar los datos originales almacenados en Bronce.
- Evitar realizar solicitudes innecesarias al servicio.
- Reconocer la fuente institucional en los análisis y resultados publicados.

## 3. Fuente SHF – Sociedad Hipotecaria Federal

**Publicación oficial:** https://www.gob.mx/shf/documentos/indice-shf-de-precios-de-la-vivienda-en-mexico-2025-a-2026

**Conjunto utilizado:** Índice SHF de precios de la vivienda, datos abiertos, segundo trimestre de 2026.

**Revisión de condiciones:**

La SHF publica los índices de precios de vivienda y archivos descargables de datos abiertos mediante su portal institucional.

La publicación consultada permite identificar el archivo y la nota metodológica correspondiente. No se identificó en la página revisada una licencia específica que permita afirmar que cualquier modalidad de reutilización está autorizada sin condiciones.

**Medidas adoptadas:**

- Identificar a la Sociedad Hipotecaria Federal como fuente.
- Conservar el archivo original descargado.
- Documentar el periodo y la fecha de consulta.
- Mantener la información original en la zona Bronce.
- Consultar la nota metodológica antes de interpretar los indicadores.
- Reconocer la fuente en los análisis y resultados.
- No atribuir a la fuente información que no contiene.

## 4. Revisión de robots.txt

Se realizaron consultas directas a los archivos robots.txt de los dominios institucionales.

### SNIIV – SEDATU

URL consultada: https://sniiv.sedatu.gob.mx/robots.txt

**Resultado:** el servidor respondió que la página no se encuentra disponible.

No fue posible recuperar el contenido del archivo. Por lo tanto, no se puede determinar mediante esta consulta qué directrices establece para los rastreadores.

La imposibilidad de consultar el archivo no se interpreta como autorización ni prohibición de extracción.

### SHF – Portal gob.mx

URL consultada: https://www.gob.mx/robots.txt

**Resultado:** archivo accesible.

Se observaron los siguientes grupos de agentes:

- Googlebot.
- googlebot-image.
- googlebot-mobile.
- AdsBot-Google.

En los grupos observados, la directiva `Disallow:` aparece vacía.

Esto indica que no se especifican rutas prohibidas para esos agentes en los grupos consultados. No implica autorización general para cualquier rastreador ni sustituye las condiciones de uso de la información.

### Conclusión de la revisión

La consulta de robots.txt pudo realizarse parcialmente:

- SNIIV: archivo no encontrado.
- gob.mx: archivo accesible, con directivas observadas para determinados agentes.

Se conservará esta limitación en la documentación y se respetarán las condiciones de uso publicadas por las instituciones responsables.

## 5. Tratamiento responsable de la información

TRUSTED DATA LAB utilizará inicialmente información estadística y agregada proveniente de fuentes institucionales.

Se adoptan las siguientes medidas:

- No recopilar datos personales innecesarios.
- No intentar identificar personas a partir de registros agregados.
- No publicar información privada de propietarios, inquilinos o entrevistados.
- Solicitar consentimiento antes de grabar entrevistas.
- Utilizar las respuestas de entrevistas únicamente para los fines académicos informados.
- Mantener una distinción entre datos oficiales, resultados calculados e hipótesis del proyecto.
- Documentar las limitaciones de cobertura y calidad.

## 6. Consideraciones para la automatización

La captura automatizada deberá:

- Consultar únicamente los recursos necesarios.
- Evitar solicitudes excesivas o repetitivas.
- Conservar la procedencia de los datos.
- Registrar errores de conexión y respuestas inesperadas.
- No intentar evadir controles de acceso.
- Respetar las condiciones publicadas por las instituciones.

## 7. Limitaciones de la revisión

Esta revisión documental no constituye una opinión jurídica ni sustituye la consulta directa con las instituciones responsables.

La licencia o las condiciones específicas de reutilización de los datos SHF y el contenido de los archivos robots.txt deberán verificarse cuando se tenga acceso directo a ellos.

Antes de ampliar la extracción automatizada o redistribuir conjuntos de datos, se revisarán nuevamente las condiciones aplicables.

## 8. Conclusión

TRUSTED DATA LAB utiliza fuentes institucionales que publican información estadística del sector vivienda.

Para SNIIV se identificó una condición explícita de uso que requiere mencionar la fuente. Para SHF se identificó la publicación institucional de datos abiertos, pero queda pendiente confirmar las condiciones específicas de reutilización.

Se documentaron las medidas de atribución, conservación de datos originales, tratamiento responsable y limitación de solicitudes automatizadas.

La revisión de robots.txt queda pendiente de verificación directa.
