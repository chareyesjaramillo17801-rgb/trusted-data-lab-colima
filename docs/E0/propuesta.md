# Propuesta E0 — Observatorio inmobiliario de Colima

**Estado:** propuesta actualizada con base en el planteamiento, las fuentes incorporadas y la entrevista exploratoria.

## 1. Ficha del observatorio

- **Nombre:** Observatorio inmobiliario de Colima: precios y acceso a la vivienda.
- **Sector:** vivienda y mercado inmobiliario.
- **Región:** estado de Colima, México.
- **Enfoque:** mercado inmobiliario general y exploración de las necesidades de vivienda en renta, especialmente para estudiantes.

### Pregunta central

¿Cómo ha evolucionado el mercado de vivienda en el estado de Colima, considerando los registros de vivienda y los índices de precios disponibles, y cómo puede transformarse esta información en conocimiento útil para el sector inmobiliario y para comprender las necesidades de vivienda en renta de la población estudiantil?

### Clientes potenciales

- Asesores y agentes inmobiliarios.
- Agencias inmobiliarias.
- Desarrolladores inmobiliarios.
- Inversionistas.
- Administradores y propietarios de inmuebles.

La necesidad comercial y la disposición de pago de estos perfiles todavía deben validarse mediante entrevistas.

## 2. Necesidad y validación del cliente

Se realizó una entrevista exploratoria a una persona que busca vivienda en renta en Tecomán, Colima.

- **Fecha:** 9 de noviembre de 2026.
- **Duración aproximada:** 15 minutos.
- **Modalidad:** mensajería escrita.
- **Preguntas respondidas:** 8.
- **Autorización:** concedida para utilizar las respuestas con fines académicos.

### Hallazgos

La persona entrevistada lleva aproximadamente tres meses buscando vivienda. Utiliza Facebook y encuentra dificultades para localizar opciones que coincidan con su presupuesto y características deseadas.

También reportó publicaciones de inmuebles que ya están ocupados o que realmente no están disponibles. Considera indispensables las fotografías y un teléfono de contacto, y utilizaría una herramienta especializada si fuera segura y estuviera constantemente actualizada.

### Interpretación

La entrevista aporta evidencia exploratoria de problemas de confiabilidad, actualización y precisión en las publicaciones inmobiliarias.

**Limitación:** esta entrevista corresponde a un usuario potencial, no a un cliente comercial. Sigue pendiente entrevistar a agentes, agencias u otros participantes del sector para validar su necesidad de información y disposición de pago.

**Evidencia:** `docs/entrevista_cliente.md`.

## 3. Preguntas analíticas

### E1 — Pronóstico

¿Es posible pronosticar la evolución del índice de precios de vivienda de Manzanillo y Villa de Álvarez utilizando su comportamiento histórico trimestral?

Se utilizarán las series trimestrales de SHF. La evaluación de los modelos considerará métricas como MAE, RMSE y MAPE, cuando sean aplicables.

### E2 — Experimento

¿La presentación de información inmobiliaria mediante gráficas comparativas, en lugar de tablas numéricas, mejora la rapidez y precisión con la que los usuarios interpretan las tendencias del mercado?

- Variable independiente: formato de presentación (gráficas o tablas).
- Variables dependientes: tiempo de interpretación y precisión de las respuestas.

El experimento está diseñado, pero todavía no se ha ejecutado.

### E3 — Análisis multivariado

¿Qué relación existe entre los registros de vivienda, los índices de precios, los periodos y los segmentos de vivienda en los municipios de Colima que cuentan con información comparable en ambas fuentes?

Será necesario armonizar las frecuencias mensual y trimestral, revisar las categorías y determinar qué variables pueden compararse válidamente.

## 4. Fuentes y recopilación de información

### SNIIV — Registro de Vivienda

- **Institución:** Secretaría de Desarrollo Agrario, Territorial y Urbano (SEDATU).
- **Recurso:** Registro de Vivienda.
- **Formato:** JSON.
- **Frecuencia:** mensual.
- **Captura:** automatizada mediante Python y GitHub Actions.
- **Ubicación:** `data/bronce/sniiv_registro/`.

Resultados de validación:

- 2,140 registros.
- 8 columnas.
- 8 municipios de Colima.
- Periodo disponible: 2010–2026.
- 200 periodos año-mes únicos.
- 0 valores faltantes.
- 0 registros duplicados.

**Evidencia:** `docs/E0/validacion_sniiv.md` y `docs/validacion_sniiv.md`.

### SHF — Índice de Precios de la Vivienda

- **Institución:** Sociedad Hipotecaria Federal.
- **Recurso:** Índice SHF de Precios de la Vivienda.
- **Archivo:** `Indice_SHF_datos_abiertos_2_trim_2026.xlsx`.
- **Formato:** Excel.
- **Frecuencia:** trimestral.
- **Captura:** incorporación manual.
- **Ubicación:** `data/bronce/shf/`.

Resultados de validación:

- 10,406 registros.
- 7 columnas.
- 258 registros correspondientes a Colima.
- 86 periodos trimestrales para Manzanillo.
- 86 periodos trimestrales para Villa de Álvarez.
- Periodo disponible: 2005–segundo trimestre de 2026.
- Sin filas completamente duplicadas ni duplicados según la clave dimensional utilizada.
- Índice sin valores faltantes en los registros de Colima.

**Evidencia:** `docs/E0/validacion_shf.md` y `docs/validacion_shf.md`.

### SNIIV — Inventario de Vivienda

Se mantiene como fuente complementaria potencial. Su recurso, URL oficial, condiciones de uso y captura todavía deben verificarse antes de incorporarlo formalmente.

## 5. Ética y legalidad

Se utilizan fuentes institucionales públicas y se conserva la procedencia de los datos.

Se realizaron revisiones documentales de SNIIV y SHF, incluyendo la consulta de robots.txt y la documentación del fundamento normativo aplicable a los datos abiertos de SHF.

Criterios de trabajo:

1. Identificar las instituciones de origen.
2. Conservar los archivos originales y sus metadatos.
3. Documentar las transformaciones y validaciones.
4. No presentar resultados derivados como publicaciones oficiales de las instituciones.
5. Respetar la privacidad y autorización de las personas entrevistadas.

**Evidencia:** `docs/etica_legalidad.md`.

## 6. Arquitectura y almacenamiento

El proyecto utiliza una estructura de almacenamiento por zonas:

- **Bronce:** conservación de archivos originales y metadatos. Implementada.
- **Plata:** datos tipados, normalizados y validados. Pendiente.
- **Oro:** indicadores agregados preparados para análisis. Pendiente.
- **Cuarentena:** registros que requieren revisión y conservación del motivo de rechazo. Pendiente.

La captura automatizada de SNIIV Registro está configurada mediante GitHub Actions y cuenta con una ejecución exitosa confirmada.

La incorporación de SHF fue manual; su automatización sigue pendiente.

## 7. Objetivos de calidad

Se establecieron tres objetivos medibles:

1. **Éxito de captura:** al menos 95% de ejecuciones programadas exitosas durante una ventana de medición de 14 días.
2. **Completitud:** al menos 98% de registros con periodo, municipio y variable de conteo no nulos en Plata.
3. **Trazabilidad:** 100% de archivos crudos acompañados de metadatos de fuente, URL y fecha/hora UTC de captura.

Son objetivos propuestos; su cumplimiento todavía requiere mediciones.

**Evidencia:** `docs/E0/objetivos-calidad.md`.

## 8. Riesgos y decisiones pendientes

1. Validar comercialmente el observatorio mediante entrevistas con participantes del sector inmobiliario.
2. Revisar la continuidad y comparabilidad de las series SHF antes del pronóstico.
3. Armonizar las frecuencias mensual y trimestral de las fuentes.
4. Comprobar la disponibilidad de variables
