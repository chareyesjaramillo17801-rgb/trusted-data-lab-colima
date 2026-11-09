# TRUSTED DATA LAB – Ficha de entrega E0

**Fecha de corte:** 9 de noviembre de 2026  
**Proyecto:** Observatorio inmobiliario de Colima  
**Repositorio:** trusted-data-lab-colima

## 1. Identificación del proyecto

**Nombre:** TRUSTED DATA LAB.

**Descripción:** Observatorio inmobiliario orientado a recopilar, organizar, validar y analizar información del mercado de vivienda en Colima.

El proyecto contempla dos líneas:

- Mercado inmobiliario general: registros de vivienda, índices de precios y tendencias.
- Vivienda en renta para estudiantes: necesidades de búsqueda, información de precios, ubicación y disponibilidad.

## 2. Pregunta central

¿Cómo ha evolucionado el mercado de vivienda en el estado de Colima, considerando los registros de vivienda y los índices de precios disponibles, y cómo puede transformarse esta información en conocimiento útil para el sector inmobiliario y para comprender las necesidades de vivienda en renta de la población estudiantil?

**Estado:** Documentada.

## 3. Cliente potencial

Se consideran como clientes potenciales:

- Asesores y agentes inmobiliarios.
- Agencias inmobiliarias.
- Desarrolladores de vivienda.
- Inversionistas inmobiliarios.
- Administradores y propietarios de inmuebles.

La hipótesis comercial es que estos perfiles podrían utilizar información histórica, comparaciones territoriales y análisis de tendencias para respaldar decisiones comerciales.

**Estado:** Perfiles identificados; necesidad y disposición de pago pendientes de validar mediante entrevista.

## 4. Preguntas analíticas

### E1 – Pronóstico

¿Es posible pronosticar la evolución del índice de precios de vivienda de Manzanillo y Villa de Álvarez utilizando su comportamiento histórico trimestral?

### E2 – Experimento

¿La presentación de información inmobiliaria mediante gráficas comparativas, en lugar de tablas numéricas, mejora la rapidez y precisión con la que los usuarios interpretan las tendencias del mercado?

### E3 – Análisis multivariado

¿Qué relación existe entre los registros de vivienda, los índices de precios, los periodos y los segmentos de vivienda en los municipios de Colima que cuentan con información comparable en ambas fuentes?

**Estado:** Tres preguntas documentadas.

## 5. Fuentes de información

### Fuente 1: SNIIV – Registro de Vivienda

- Institución: SEDATU.
- Formato capturado: JSON.
- Registros analizados: 2,140.
- Columnas: 8.
- Municipios identificados: 8.
- Periodos mensuales distintos: 200.
- Valores faltantes: 0.
- Registros duplicados: 0.
- Documentación: `docs/validacion_sniiv.md`.
- Capturas: `data/bronce/sniiv_registro/`.

### Fuente 2: SHF – Índice de Precios de la Vivienda

- Institución: Sociedad Hipotecaria Federal.
- Formato original: XLSX.
- Registros analizados: 10,406.
- Columnas: 7.
- Registros correspondientes a Colima: 258.
- Municipios identificados: Manzanillo y Villa de Álvarez.
- Periodos por municipio: 86.
- Filas completamente duplicadas: 0.
- Claves dimensionales duplicadas: 0.
- Valores faltantes en la columna Índice para Colima: 0.
- Documentación: `docs/validacion_shf.md`.
- Archivo original: `data/bronce/shf/Indice_SHF_datos_abiertos_2_trim_2026.xlsx`.

**Estado:** Dos fuentes incorporadas y documentadas.

## 6. Captura automatizada

Se configuró GitHub Actions mediante el workflow:

`.github/workflows/captura.yml`

El workflow contempla:

- Ejecución manual.
- Ejecución programada diaria.
- Configuración del entorno Python.
- Instalación de dependencias.
- Ejecución del extractor SNIIV.
- Ejecución condicional de extractores adicionales.
- Almacenamiento de capturas en Bronce y envío de cambios al repositorio.

El archivo SHF se incorporó manualmente al repositorio. Su inspección y validación se ejecutaron mediante GitHub Actions; esto no significa que su descarga ya esté automatizada.

**Estado:** Automatización de captura SNIIV configurada; descarga automática SHF pendiente.

## 7. Calidad de datos

Se realizaron validaciones para las dos fuentes:

- Estructura y columnas.
- Registros totales.
- Valores faltantes.
- Duplicados.
- Cobertura temporal.
- Cobertura geográfica.

Los resultados están documentados en:

- `docs/validacion_sniiv.md`
- `docs/validacion_shf.md`

**Estado:** Validaciones iniciales realizadas y documentadas.

## 8. ### Entrevista a cliente potencial

**Estado:** Realizada.

- Perfil: persona que busca vivienda en renta.
- Ubicación: Tecomán, Colima.
- Fecha: 9 de noviembre de 2026.
- Hora: 12:07 p. m.
- Duración aproximada: 15 minutos.
- Modalidad: mensajería escrita.
- Preguntas respondidas: 8.
- Autorización para uso académico: confirmada.
- Evidencia: `docs/entrevista_cliente.md`.

**Principales hallazgos:**
- Dificultad para encontrar viviendas que cumplan con el presupuesto y características deseadas.
- Publicaciones de inmuebles que no están realmente disponibles.
- Necesidad de información confiable, fotografías y teléfonos de contacto.
- Importancia de mantener la disponibilidad actualizada y ofrecer una plataforma segura.

**Limitación:** Se cuenta con una entrevista exploratoria. Es necesario realizar más entrevistas para validar si estas necesidades se repiten en otros usuarios.

## 9. Ética y legalidad

Pendiente documentar la revisión de:

- Términos y condiciones de uso de las fuentes.
- Políticas de acceso y reutilización.
- Archivos robots.txt cuando correspondan.
- Condiciones de atribución y uso de los datos.

**Estado:** Pendiente de revisión y documentación.

## 10. PSP – Registro de tiempos y defectos

Se llevará un registro de actividades, duración real y defectos encontrados durante el desarrollo.

| Actividad | Tiempo invertido | Defectos o incidencias |
|---|---|---|
| Configuración del repositorio | Pendiente de registrar | Pendiente |
| Captura SNIIV | Pendiente de registrar | Pendiente |
| Validación SNIIV | Pendiente de registrar | Pendiente |
| Incorporación de SHF | Pendiente de registrar | Pendiente |
| Inspección y validación SHF | Pendiente de registrar | Pendiente |
| Documentación E0 | Pendiente de registrar | Pendiente |

No se asignan tiempos estimados como si fueran mediciones reales. Los datos se completarán con base en el trabajo efectivamente realizado.

**Estado:** Registro PSP por completar.

## 11. Organización del repositorio

Archivos de documentación previstos:

- `docs/planteamiento_e0.md`
- `docs/validacion_sniiv.md`
- `docs/validacion_shf.md`
- `docs/ficha_e0.md`

Código y datos:

- `extractores/`
- `data/bronce/`
- `.github/workflows/captura.yml`

## 12. Estado general de E0

| Requisito | Estado |
|---|---|
| Pregunta central | Documentada |
| Cliente potencial | Identificado, pendiente de validación |
| Tres preguntas analíticas | Documentadas |
| Dos fuentes de información | Incorporadas |
| Serie histórica mínima de 36 periodos | Cumplida |
| Validación inicial de calidad | Realizada |
| Captura automatizada | SNIIV configurada |
| Entrevista real de 15 minutos | Pendiente |
| Ética y legalidad | Pendiente |
| PSP | Pendiente de completar |
| Ficha E0 | En documentación |
| Etiqueta `e0` en GitHub | Pendiente |

## 13. Conclusión

TRUSTED DATA LAB cuenta con una estructura inicial de observatorio, dos fuentes de información inmobiliaria y procesos de captura y validación implementados.

Los datos disponibles permiten estudiar registros de vivienda y evolución de índices de precios en Colima. La línea de vivienda en renta para estudiantes se plantea como una aplicación complementaria que requiere información adicional y validación con usuarios reales.

La entrega E0 se considerará completa únicamente después de reunir las evidencias pendientes y verificar los requisitos de la rúbrica.
