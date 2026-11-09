# Entrega E0 — Observatorio inmobiliario de Colima

**Equipo:** trabajo individual  
**Entrega:** E0 — Planteamiento, fuentes y captura inicial  
**Etiqueta:** `e0` (pendiente de crear tras la revisión final)  
**Tablero:** no disponible en E0.

## Resumen

Se propone desarrollar un observatorio inmobiliario para el estado de Colima que integre información oficial sobre registros de vivienda e índices de precios.

El proyecto contempla dos enfoques complementarios: el análisis del mercado inmobiliario general y la exploración de las necesidades de información de las personas que buscan vivienda en renta, especialmente estudiantes.

Durante E0 se definió el planteamiento, se incorporaron dos fuentes oficiales, se realizaron validaciones de calidad, se configuró la captura automatizada de SNIIV Registro y se realizó una entrevista exploratoria a una persona que busca vivienda.

La validación comercial con participantes del sector inmobiliario continúa pendiente.

## Ingeniería de Datos

| Criterio | Evidencia | Estado |
|---|---|---|
| Dos fuentes de información | SNIIV Registro y SHF en `data/bronce/` | Cumplido |
| Fuente complementaria | SNIIV Inventario identificada, sin incorporación confirmada | Pendiente |
| Plan y ética | `docs/E0/propuesta.md` y `docs/etica_legalidad.md` | Documentado |
| Revisión de robots.txt | Resultados documentados para los dominios consultados | Documentado con limitaciones |
| Captura automática | `.github/workflows/captura.yml` y ejecución exitosa de GitHub Actions | Cumplido para SNIIV Registro |
| Captura automática SHF | Archivo incorporado manualmente | Pendiente |
| Serie histórica de al menos 36 periodos | SNIIV: 200 periodos año-mes; SHF: 86 periodos trimestrales por municipio | Cumplido |
| Validación de calidad | `docs/E0/validacion_sniiv.md` y `docs/E0/validacion_shf.md` | Cumplido |
| Metadatos de procedencia | Nueve archivos de metadatos SNIIV con contenido y metadatos SHF incorporados | Parcialmente verificado |

## Análisis Estadístico

| Criterio | Evidencia | Estado |
|---|---|---|
| Variable para pronóstico | Pregunta E1 sobre índices SHF de Manzanillo y Villa de Álvarez | Definida; análisis pendiente |
| Pregunta de experimento | Pregunta E2 sobre interpretación de gráficas y tablas | Definida; experimento pendiente |
| Pregunta multivariada | Pregunta E3 sobre registros, precios, periodos y segmentos | Definida; viabilidad técnica pendiente |
| Comparabilidad de variables | Armonización de frecuencias y categorías entre fuentes | Pendiente para E3 |

## Calidad en los Sistemas de Información

| Criterio | Evidencia | Estado |
|---|---|---|
| Registro PSP de tiempo | `docs/psp.md` y `calidad/tiempo-individual.csv` | Documentado; estimaciones retrospectivas |
| Registro PSP de defectos | `docs/psp.md` y `calidad/defectos-individual.csv` | Documentado |
| Tres objetivos medibles | `docs/E0/objetivos-calidad.md` | Definidos; medición pendiente |
| Bitácora de captura | Metadatos en `data/bronce/` | Evidencia disponible |
| Éxito de captura durante 14 días | Objetivo de calidad 1 | Pendiente de medición |
| Completitud en Plata | Objetivo de calidad 2 | Pendiente de implementar Plata |
| Trazabilidad del 100 % | Objetivo de calidad 3 | Auditoría completa pendiente |

Los tiempos del PSP son estimaciones retrospectivas y no mediciones cronometradas. Los defectos registrados corresponden a problemas identificados y corregidos durante el desarrollo.

## Entrevista y validación del cliente

**Estado del requisito de entrevista: cumplido.**

Se realizó una entrevista escrita de aproximadamente 15 minutos, con ocho preguntas respondidas por una persona que busca vivienda en Tecomán, Colima. El docente confirmó que acepta esta modalidad para satisfacer el requisito de entrevista de E0.

- Perfil: persona que busca vivienda en renta.
- Ubicación: Tecomán, Colima.
- Fecha: 9 de noviembre de 2026.
- Hora: 12:07 p. m.
- Duración aproximada: 15 minutos.
- Modalidad: mensajería escrita.
- Preguntas respondidas: 8.
- Autorización para uso académico: confirmada.

La entrevista identificó dificultades relacionadas con publicaciones desactualizadas, disponibilidad real de inmuebles, precios y características de las viviendas.

La entrevista tiene carácter exploratorio y no representa una validación comercial con agentes, asesores o agencias inmobiliarias. La disposición de pago de clientes comerciales continúa pendiente.

**Evidencia:** `docs/entrevista_cliente.md`.

## Relatoría

**Estado: documentada.**

Se creó `docs/relatoria.md`, que consolida las actividades realizadas, los resultados técnicos, los problemas encontrados, las correcciones y las limitaciones del proyecto.

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
- `docs/relatoria.md`
- `calidad/tiempo-individual.csv`
- `calidad/defectos-individual.csv`

## Pendientes para el cierre de E0

1. Intentar validar la necesidad comercial y la disposición de pago con un participante del sector inmobiliario.
2. Auditar los nueve archivos de metadatos SNIIV y comprobar todos los campos requeridos.
3. Revisar la trazabilidad completa de los archivos originales, incluidos los metadatos SHF.
4. Comprobar la consistencia de todos los documentos y archivos del repositorio.
5. Crear la etiqueta `e0` después de la revisión final.

## Estado general

E0 cuenta con avances sustanciales en planteamiento, fuentes, captura, validación, entrevista y documentación. El requisito formal de entrevista fue aceptado por el
