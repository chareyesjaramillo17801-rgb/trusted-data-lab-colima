# Ficha de entrega E0 – TRUSTED DATA LAB

## 1. Identificación del proyecto

- **Proyecto:** TRUSTED DATA LAB
- **Entrega:** E0 – Planteamiento, fuentes y captura inicial
- **Área:** Análisis de datos y observatorio inmobiliario.
- **Ámbito geográfico:** Estado de Colima, México.
- **Fecha de actualización:** 9 de noviembre de 2026.

## 2. Pregunta central

¿Cómo ha evolucionado el mercado de vivienda en el estado de Colima, considerando los registros de vivienda y los índices de precios disponibles, y cómo puede transformarse esta información en conocimiento útil para el sector inmobiliario y para comprender las necesidades de vivienda en renta de la población estudiantil?

## 3. Objetivo general

Desarrollar un observatorio inmobiliario para recopilar, organizar, validar y analizar información sobre el comportamiento del mercado de vivienda en Colima, utilizando fuentes oficiales de datos y explorando las necesidades de información de las personas que buscan vivienda en renta.

## 4. Enfoque del proyecto

El proyecto contempla dos enfoques complementarios:

1. **Mercado inmobiliario general:** análisis de registros de vivienda e índices de precios para identificar tendencias y comportamientos del mercado.
2. **Vivienda en renta para estudiantes:** exploración de las dificultades y necesidades de las personas que buscan vivienda, con énfasis en información confiable, características, precios y disponibilidad.

La información de las fuentes oficiales actuales no permite conocer directamente la disponibilidad de inmuebles en renta. Por ello, esta línea requiere información complementaria.

## 5. Clientes potenciales y usuarios

### Clientes potenciales

- Asesores y agentes inmobiliarios.
- Agencias inmobiliarias.
- Desarrolladores inmobiliarios.
- Inversionistas.
- Administradores y propietarios de inmuebles.

**Necesidad identificada:** contar con información organizada y analizada que facilite la comprensión del comportamiento del mercado inmobiliario y apoye la toma de decisiones.

**Estado de validación comercial:** pendiente. Todavía es necesario entrevistar a posibles clientes del sector inmobiliario y comprobar su interés y disposición de pago.

### Usuarios potenciales

- Personas que buscan vivienda en renta.
- Estudiantes universitarios.
- Personas interesadas en comprar una vivienda.
- Investigadores y estudiantes que requieren información inmobiliaria.

## 6. Preguntas analíticas para las siguientes entregas

### E1 – Pronóstico

¿Es posible pronosticar la evolución del índice de precios de vivienda de Manzanillo y Villa de Álvarez utilizando su comportamiento histórico trimestral?

### E2 – Experimento

¿La presentación de información inmobiliaria mediante gráficas comparativas, en lugar de tablas numéricas, mejora la rapidez y precisión con la que los usuarios interpretan las tendencias del mercado?

- Variable independiente: formato de presentación (gráficas o tablas).
- Variables dependientes: tiempo de interpretación y precisión de las respuestas.

### E3 – Análisis multivariado

¿Qué relación existe entre los registros de vivienda, los índices de precios, los periodos y los segmentos de vivienda en los municipios de Colima que cuentan con información comparable en ambas fuentes?

## 7. Fuentes de información

### Fuente 1. SNIIV – Registro de Vivienda

- **Institución:** Secretaría de Desarrollo Agrario, Territorial y Urbano (SEDATU).
- **Fuente:** Sistema Nacional de Información e Indicadores de Vivienda (SNIIV).
- **Recurso:** Registro de Vivienda.
- **Consulta:** API de SNIIV.
- **Ubicación en el repositorio:** `data/bronce/sniiv_registro/`.
- **Captura:** automatizada mediante extractor de Python y GitHub Actions.

**Resultados de validación:**

- 2,140 registros.
- 8 columnas.
- 8 municipios de Colima.
- 17 años disponibles (2010–2026).
- 200 periodos año-mes únicos.
- 0 valores faltantes.
- 0 registros duplicados.
- Cobertura de 12 meses por año entre 2010 y 2025.
- 8 meses disponibles para 2026.

**Documentación:** `docs/validacion_sniiv.md`.

### Fuente 2. SHF – Índice de Precios de la Vivienda

- **Institución:** Sociedad Hipotecaria Federal (SHF).
- **Recurso:** Índice SHF de Precios de la Vivienda.
- **Archivo:** `Indice_SHF_datos_abiertos_2_trim_2026.xlsx`.
- **Ubicación en el repositorio:** `data/bronce/shf/`.
- **Captura:** incorporación manual del archivo oficial.

**Resultados de validación:**

- 10,406 registros.
- 7 columnas.
- 258 registros correspondientes a Colima.
- 86 periodos trimestrales disponibles para Manzanillo.
- 86 periodos trimestrales disponibles para Villa de Álvarez.
- Cobertura desde 2005 hasta el segundo trimestre de 2026.
- 0 filas completamente duplicadas.
- 0 duplicados según la clave dimensional utilizada en la validación.
- Índice sin valores faltantes en los registros de Colima.

Los valores vacíos de las columnas Global y Municipio corresponden a registros de otros niveles o categorías y no se consideran automáticamente errores.

**Documentación:** `docs/validacion_shf.md`.

## 8. Captura y almacenamiento de datos

Se implementó una estructura de almacenamiento por zonas:

- **Bronce:** conservación de los datos originales.
- **Plata:** destinada al procesamiento y transformación.
- **Oro:** destinada a los datos preparados para análisis.
- **Cuarentena:** destinada a registros que requieran revisión.

La captura automatizada de SNIIV se encuentra configurada mediante GitHub Actions.

El archivo de SHF fue incorporado manualmente al repositorio. La descarga automatizada de esta fuente todavía está pendiente.

## 9. Entrevista a cliente potencial / usuario

**Estado:** Realizada.

- **Perfil:** persona que busca vivienda en renta.

## 10. Ética y legalidad

### SNIIV – SEDATU

- Se identificó el Registro de Vivienda como fuente oficial del Sistema Nacional de Información e Indicadores de Vivienda.
- Se consultó el archivo `robots.txt` del dominio SNIIV, pero no se encontró una página accesible.
- Esta situación no se interpreta como autorización ni prohibición general de extracción.
- Se conserva la procedencia de los datos y se identifica a SEDATU como institución de origen.

### SHF – Sociedad Hipotecaria Federal

- Se identificó la publicación oficial del Índice SHF de Precios de la Vivienda y el archivo de datos abiertos correspondiente al segundo trimestre de 2026.
- Se documentó el fundamento normativo de los datos abiertos de la Administración Pública Federal.
- Se identificó la aplicación institucional de los Lineamientos en materia de Datos Abiertos a SHF.
- Se conservará la atribución a SHF y la procedencia del archivo original.
- Las transformaciones realizadas se documentarán y los resultados derivados no se presentarán como publicaciones oficiales de SHF.

### Criterios éticos y de manejo de información

1. Conservar los archivos originales en la zona Bronce.
2. Identificar las instituciones y fuentes de procedencia.
3. Documentar las transformaciones y validaciones.
4. No alterar los datos originales.
5. Respetar la privacidad y autorización de las personas entrevistadas.
6. No divulgar información personal de los participantes sin autorización.

**Estado:** Revisión documental realizada para las fuentes consultadas. Se mantienen los criterios de atribución, integridad y transparencia durante el desarrollo del proyecto.
