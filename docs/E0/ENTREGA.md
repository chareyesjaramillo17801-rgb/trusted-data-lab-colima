# Entrega E0 — Observatorio inmobiliario de Colima
**Equipo:** trabajo individual  
**Etiqueta:** `e0` (crear únicamente al cerrar la versión revisada)  
**Tablero:** no disponible en E0 / pendiente.

## Resumen
Se propone un observatorio inmobiliario para Colima que integra indicadores oficiales de precios y oferta habitacional. La pregunta, cliente y disponibilidad de series se mantienen sujetos a validación documental y entrevista.

## Ingeniería de Datos
| Criterio | Evidencia | Estado |
|---|---|---|
| Dos fuentes | SNIIV Registro, SNIIV Inventario y SHF identificadas | Parcial: confirmar y ejecutar captura de dos recursos |
| Plan y ética | `docs/E0/propuesta.md` | Parcial: revisar términos/licencias y robots.txt por recurso |
| Captura automática | `.github/workflows/captura.yml` | Código base; falta configurar y probar en GitHub |
| Serie histórica >=36 periodos | `data/bronce/` | Pendiente de incorporar y validar SHF |
## Análisis Estadístico
| Criterio | Evidencia | Estado |
|---|---|---|
| Variable para pronóstico | Pregunta E1 en propuesta | Provisional; verificar serie SHF |
| Pregunta de experimento | Pregunta E2 en propuesta | Diseño propuesto; no ejecutado |
| Grupos multivariados | Pregunta E3 en propuesta | Viabilidad pendiente de cinco variables |
## Calidad en los Sistemas de Información
| Criterio | Evidencia | Estado |
|---|---|---|
| Registro PSP de tiempo | `calidad/tiempo-individual.csv` | Abrir y registrar trabajo real |
| Registro PSP de defectos | `calidad/defectos-individual.csv` | Abrir y registrar defectos reales |
| Tres objetivos medibles | `docs/E0/objetivos-calidad.md` | Propuestos; medir posteriormente |
| Bitácora de captura | metadatos en `data/bronce/` | Requiere ejecuciones reales |

## Entrevista
Pendiente de realizar. No se reportan respuestas ficticias.

## Relatoría
Pendiente de documentar actividades reales y evidencias.
