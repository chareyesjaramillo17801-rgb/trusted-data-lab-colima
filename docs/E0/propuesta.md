# Propuesta E0 — Observatorio inmobiliario de Colima

**Estado:** borrador de trabajo; validar con entrevista y datos antes de entregar como definitivo.

## 1. Ficha del observatorio
- **Nombre:** Observatorio inmobiliario de Colima: precios y acceso a la vivienda.
- **Sector:** vivienda / mercado inmobiliario.
- **Región:** estado de Colima, México.
- **Pregunta central provisional:** ¿Cómo ha evolucionado el mercado de vivienda en el estado de Colima y qué relación existe entre los precios, la oferta habitacional y el financiamiento, para identificar tendencias y oportunidades inmobiliarias?
- **Cliente potencial por validar:** agentes inmobiliarios, desarrolladores de vivienda, valuadores o cámaras del sector. No se afirma que alguno haya aceptado pagar.

## 2. Necesidad y validación del cliente
Pendiente de entrevista real de al menos 15 minutos. Registrar:
- Fecha y duración:
- Perfil/sector de la persona (sin publicar datos personales):
- Cinco o más preguntas:
- Respuestas y hallazgos:
- Qué decisión tomaría con esta información:
- Qué valor económico tendría y bajo qué condiciones pagaría:

## 3. Tres preguntas analíticas
- **E1 — Pronóstico:** ¿Cuál será la evolución del índice SHF de precios de vivienda de Colima durante los siguientes cuatro trimestres, según el mejor modelo validado por MAE, RMSE y MAPE?
- **E2 — Experimento:** ¿Qué combinación de frecuencia de captura, formato de almacenamiento y estrategia de procesamiento reduce el tiempo de actualización del observatorio sin aumentar errores? (Experimento de ingeniería por ejecutar; no presentar resultados antes de correrlo).
- **E3 — Multivariado:** ¿Existen diferencias entre los municipios de Colima en el volumen y composición de vivienda registrada, considerando variables numéricas comparables construidas a partir de Registro e Inventario? La viabilidad depende de comprobar cinco variables numéricas y grupos suficientes.

## 4. Fuentes y plan de recopilación
### SNIIV — Registro de Vivienda
- Portal: https://sniiv.sedatu.gob.mx/
- API utilizada como punto de partida: `https://sniiv.sedatu.gob.mx/api/CuboAPI/GetRegistro/2010,2026/06/000/anio,mes,estado,municipio,segmento`
- Frecuencia del indicador: mensual.
- Formato: JSON.
- Captura: `python -m extractores.registro_sniiv`.
- Antes de análisis: comprobar esquema, cobertura por municipio/mes/segmento y cambios de definición.

### SNIIV — Inventario de Vivienda
- Portal: https://sniiv.sedatu.gob.mx/
- Recurso descargable: pendiente de identificar y configurar URL directa oficial.
- Formato descrito en el archivo previo: CSV.
- Variables reportadas en el avance anterior: año, mes, entidad, municipio, avance de obra, valor, UMA, tipo y viviendas.
- No se automatiza hasta confirmar el enlace oficial, licencia y términos.

### SHF — Índice de Precios de la Vivienda
- Portal: https://www.gob.mx/shf
- Publicaciones: https://www.gob.mx/shf/documentos/indice-shf-de-precios-de-la-vivienda-en-mexico-2005-2018?state=published
- Publicaciones 2020–2024: https://www.gob.mx/shf/documentos/indice-shf-de-precios-de-la-vivienda-en-mexico-2020-2024
- Publicaciones 2025–2026: https://www.gob.mx/shf/documentos/indice-shf-de-precios-de-la-vivienda-en-mexico-2025-a-2026
- Frecuencia: trimestral.
- Formato y URL directa del archivo abierto: por verificar antes de automatizar.

## 5. Ética y legalidad
Se priorizan APIs y archivos públicos oficiales. No se recopilan datos personales. Para cualquier scraping se debe revisar el `robots.txt`, términos de uso y licencia del recurso, identificar el extractor y respetar al menos un segundo entre peticiones al mismo dominio. La consulta a la API no sustituye la revisión de condiciones de uso. Registrar fecha de consulta y conservar respuesta original y metadatos.

## 6. Arquitectura y almacenamiento
- Bronce: respuestas originales y metadatos, sin sobrescribir capturas previas.
- Plata: datos tipados, normalizados y validados (pendiente).
- Oro: indicadores agregados y diccionario de datos (pendiente).
- Cuarentena: registros que fallen validaciones, conservando motivo (pendiente).

## 7. Riesgos y decisiones pendientes
1. La serie SHF de Colima debe verificarse en continuidad y comparabilidad; revisar cambios de año base.
2. Registro e Inventario tienen frecuencias y conceptos distintos; no unirlos directamente sin definir unidad temporal y claves.
3. La pregunta central depende de la disponibilidad real de la variable de financiamiento; si no hay fuente comparable, quitar financiamiento de la pregunta.
4. La serie histórica debe contar con al menos 36 periodos válidos y documentados.
