# Entrega E0 — Observatorio inmobiliario de Colima

**Equipo:** trabajo individual  
**Entrega:** E0 — Planteamiento, fuentes y captura inicial  
**Etiqueta:** `e0` (crear únicamente al cerrar la versión revisada)  
**Tablero:** no disponible en E0 / pendiente.

## Resumen

Se propone desarrollar un observatorio inmobiliario para el estado de Colima que integre información oficial sobre registros de vivienda e índices de precios.

El proyecto contempla dos enfoques complementarios: el análisis del mercado inmobiliario general y la exploración de las necesidades de información de las personas que buscan vivienda en renta, especialmente estudiantes.

Durante E0 se definió el planteamiento, se incorporaron dos fuentes oficiales, se realizaron validaciones de calidad, se configuró la captura automatizada de SNIIV Registro y se realizó una entrevista exploratoria a una persona que busca vivienda.

La validación comercial con participantes del sector inmobiliario continúa pendiente.

## Ingeniería de Datos

| Criterio | Evidencia | Estado |
|---|---|---|
| Dos fuentes de información | SNIIV Registro y SHF incorporadas en `data/bronce/` | Cumplido |
| Fuente complementaria | SNIIV Inventario identificada, pero sin incorporación confirmada | Pendiente |
| Plan y ética | `docs/E0/propuesta.md` y `docs/etica_legalidad.md` | Documentado |
| Revisión de robots.txt | Resultados documentados para los dominios consultados | Documentado con limitaciones |
| Captura automática | `.github/workflows/captura.yml` y ejecución exitosa de GitHub Actions | Cumplido para SNIIV Registro |
| Captura automática SHF | Archivo incorporado manualmente | Pendiente |
| Serie histórica de al menos 36 periodos | SNIIV: 200 periodos año-mes; SHF: 86 periodos trimestrales por municipio | Cumplido |
| Validación de calidad | `docs/E0/validacion_sniiv.md` y `docs/E0/validacion_shf.md` | Cumplido |

## Análisis Estadístico

| Criterio | Evidencia | Estado |
|---|---|---|
| Variable para pronóstico | Pregunta E1 sobre índices SHF de Manzanillo y Villa de Álvarez | Definida; análisis pendiente |
| Pregunta de experimento | Pregunta E2 sobre interpretación de gráficas y tablas | Definida; experimento pendiente |
| Pregunta multivariada | Pregunta E3 sobre registros, precios, periodos y segmentos | Definida; viabilidad técnica pendiente |
| Comparabilidad de variables | Requiere armonizar frecuencias y categorías entre fuentes | Pendiente para E3 |

## Calidad en los Sistemas de Información

| Criterio | Evidencia | Estado |
|---|---|---|
| Registro PSP de tiempo | `docs/psp.md` | Documentado |
| Registro PSP de defectos | `docs/psp.md` | Documentado |
| Tres objetivos medibles | `docs/E0/objetivos-calidad.md` | Definidos; medición pendiente |
| Bitácora de captura | Metadatos de capturas en `data/bronce/` | Existe evidencia inicial |
| Medición de éxito de captura durante 14 días | Objetivo de calidad 1 | Pendiente |
| Medición de completitud en Plata | Objetivo de calidad 2 | Pendiente de implementar Plata |
| Comprobación de trazabilidad del 100% | Objetivo de calidad 3 | Pendiente de auditoría completa |

## Entrevista y validación del cliente

**Estado:** entrevista exploratoria realizada.

- Perfil: persona que busca vivienda en renta.
- Ubicación de búsqueda: Tecomán, Colima.
- Fecha: 9 de noviembre de 2026.
- Hora: 12:07 p. m.
- Duración aproximada: 15 minutos.
- Modalidad: mensajería escrita.
- Preguntas respondidas: 8.
- Autorización para uso académico: confirmada.

La entrevista identificó dificultades relacionadas con publicaciones desactualizadas, disponibilidad real de inmuebles, precios y características de las viviendas.

**Limitaciones:** la entrevista corresponde a un usuario potencial y no valida la disposición de pago de clientes comerciales. También queda sujeta a la aceptación de la modalidad escrita por parte del docente.

**Evidencia:** `docs/entrevista_cliente.md`.

## Relatoría

La relatoría de actividades debe consolidar las actividades efectivamente realizadas, sus fechas, dificultades, decisiones y evidencias.

Los avances técnicos y documentales se encuentran distribuidos en:

- `docs/psp.md`
- `docs/entrevista_cliente.md`
- `docs/etica_legalidad.md`
- `docs/ficha_e0.md`
- `docs/planteamiento_e0.md`
- `docs/E0/validacion_sniiv.md`
- `docs/E0/validacion_shf.md`

**Estado:** pendiente de consolidación en una relatoría específica.

## Documentación de soporte

- `docs/E0/propuesta.md`
- `docs/E0/objetivos-calidad.md`
- `docs/E0/validacion_sniiv.md`
- `docs/E0/validacion_shf.md`
- `docs/ficha_e0.md`
- `docs/planteamiento_e0.md`
- `docs/entrevista_cliente.md`
- `docs/etica_legalidad.md`
- `docs/psp.md`

## Pendientes para el cierre de E0

1. Confirmar con el docente si acepta la entrevista escrita como evidencia del requisito de duración mínima.
2. Intentar validar la necesidad comercial y la disposición de pago con un participante del sector inmobiliario.
3. Comprobar la evidencia de los registros PSP y sus archivos de respaldo.
4. Revisar la trazabilidad de los archivos originales y sus metadatos.
5. Consolidar la relatoría de actividades.
6. Comprobar la consistencia de todos los documentos y archivos del repositorio.
7. Crear la etiqueta `e0` únicamente después de la revisión final.

**Estado general:** E0 cuenta con avances sustanciales en planteamiento, fuentes, captura, validación y documentación. El cierre formal queda sujeto a la revisión de los pendientes y a los criterios de aceptación de la entrega.
