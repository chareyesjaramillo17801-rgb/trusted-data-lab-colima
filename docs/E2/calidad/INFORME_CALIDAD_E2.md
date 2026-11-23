# Informe de evaluación de calidad E2

**Proyecto:** TRUSTED DATA LAB — Observatorio inmobiliario de Colima
**Corte de evidencia:** 22 de noviembre de 2026
**Alcance:** siete productos de capa Oro, pruebas de código y resultados experimentales locales.
**Estado:** evaluación interna documentada; auditoría cruzada pendiente de recibir el repositorio del equipo asignado.

## 1. Método y reproducibilidad

Se ejecutó `python -m calidad.evaluacion_e2` sobre los archivos Oro. La salida `resultados/calidad_e2/metricas_iso25012.csv`, `metricas_iso25012.json` y `RESUMEN.md` constituye la evidencia primaria. La ejecución registrada en JSON fue `2026-11-22T23:26:53.795183+00:00`. Se verificaron adicionalmente `python -m ruff check calidad` (sin observaciones) y `python -m pytest -q` (12 pruebas aprobadas, 7.12 s), según la salida local facilitada. Estos resultados no equivalen a una certificación ISO.

## 2. ISO/IEC 25012: calidad de datos

| Producto Oro | Filas | Completitud de celdas | Duplicados de fila completa | Presencia de origen y hash |
|---|---:|---:|---:|---:|
| registros_trimestrales | 383 | 100 % | 0 | 100 % |
| indice_shf_colima | 258 | 91.11 % | 0 | 100 % |
| comparacion_municipal | 131 | 100 % | 0 | No evaluable |
| variables_analiticas_sniiv | 2140 | 100 % | 0 | 100 % |
| comparacion_modelos | 8 | 93.75 % | 0 | 100 % |
| pronosticos_exploratorios | 8 | 96.88 % | 0 | 100 % |
| diagnostico_ampliado | 2 | 100 % | 0 | 100 % |

**Interpretación:** 4 de 7 productos tienen completitud de celdas del 100 %. La ausencia de filas completamente duplicadas no demuestra unicidad de claves de negocio; solo `indice_shf_colima` tiene una clave evaluada (`id_fila_bronce`, sin duplicados). La presencia de un nombre de origen y hash no demuestra que el contenido de Bronce se haya revalidado criptográficamente.

### Incidencias para investigación, no defectos confirmados

| ID | Prioridad provisional | Evidencia | Verificación y criterio de cierre |
|---|---|---|---|
| QC-01 | Media | SHF: 258 valores nulos en `Global` y 86 en `Municipio` | Verificar el esquema original SHF y documentar qué celdas son no aplicables; no imputar sin justificación |
| QC-02 | Media | `comparacion_modelos`: 8 nulos en `error` | Comprobar si el campo corresponde a error de ejecución, ausencia legítima de errores o información omitida; documentar semántica |
| QC-03 | Baja | `pronosticos_exploratorios`: 4 nulos en `origenes_backtesting` | Identificar si esas filas no emplearon backtesting y etiquetar explícitamente como no aplicable si procede |
| QC-04 | Media | `comparacion_municipal`: solo se detectó `id_fila_bronce`; la métrica origen+hash no es evaluable | Revisar vínculo de cada agregado con sus filas fuente, hashes y fecha de captura; demostrar linaje mediante consulta reproducible |

**Limitaciones:** la evaluación no mide exactitud contra fuentes originales, actualidad, credibilidad, consistencia semántica ni disponibilidad de datos. Esos atributos requieren procedimientos separados.

## 3. ISO/IEC 25010: modelo de ocho características solicitado en la rúbrica

| Característica | Evidencia disponible | Resultado y límite |
|---|---|---|
| Adecuación funcional | Pipeline, siete productos Oro, dashboard y pruebas | Existencia de funcionalidades; cobertura de requisitos no cuantificada |
| Eficiencia de desempeño | `resultados/estadistica_e2/` y `docs/E2/estadistica/` | Prueba local de optimización: 47.73 % de reducción media reportada; no extrapolar a todo el sistema |
| Compatibilidad | Despliegue Streamlit confirmado por la responsable | Falta matriz de navegadores, sistemas y versiones |
| Usabilidad | Dashboard interactivo y mapa municipal confirmado por la responsable | Falta prueba formal con tareas, usuarios y métricas |
| Fiabilidad | `pytest -q`: 12/12; ejecución de evaluación 7/7 | No se ha medido disponibilidad, recuperación ni fallos prolongados |
| Seguridad | Datos de origen público y documentación ética | Falta análisis de secretos, dependencias, permisos y amenazas |
| Mantenibilidad | `ruff check calidad`: sin errores; pruebas y módulos | Evidencia parcial: Ruff no mide por sí solo complejidad ni facilidad de cambio |
| Portabilidad | Repositorio con Python y dependencias; ejecución local | Falta instalación limpia reproducida en un segundo entorno |

**Nota normativa:** se aplica el modelo de ocho características de ISO/IEC 25010:2011 solicitado en la actividad; no debe confundirse con la reorganización posterior del modelo.

## 4. Comparación de modelos y sistemas de calidad

| Norma o familia | Objeto | Uso en este proyecto |
|---|---|---|
| ISO/IEC 9126 | Modelo histórico de calidad del producto software | Antecedente de los atributos de evaluación |
| ISO/IEC 25010 (SQuaRE) | Modelo de calidad del producto software | Matriz de ocho características y evidencias de funcionamiento |
| ISO/IEC 25012 (SQuaRE) | Modelo de calidad de datos | Métricas de completitud, duplicados y presencia de linaje en Oro |
| ISO 9001 | Sistema de gestión de la calidad | Gestión de procesos, trazabilidad de acciones correctivas, auditoría y mejora continua; no certifica el código ni los datos automáticamente |

## 5. Auditoría cruzada

**Pendiente externo.** La responsable tiene equipo asignado, pero aún no ha recibido su repositorio. No se declara auditoría ejecutada ni se inventan defectos de terceros. Una vez disponible: fijar URL y commit auditado; comprobar instalación, ejecución, pruebas, calidad de datos, documentación y linaje; registrar defectos críticos/mayores/menores con pasos de reproducción y evidencia; compartir hallazgos al equipo y documentar respuesta y revalidación.

## 6. Conclusión y acciones siguientes

La medición inicial de siete productos Oro y la ejecución de 12 pruebas permiten sustentar una evaluación interna parcial. Los principales pendientes son verificar la semántica de nulos, demostrar trazabilidad de agregados, ampliar pruebas de ISO/IEC 25010 y ejecutar la auditoría cruzada. No se afirma conformidad total ni certificación ISO.

**Fuentes internas:** `resultados/calidad_e2/metricas_iso25012.json`, `resultados/calidad_e2/metricas_iso25012.csv`, `resultados/calidad_e2/RESUMEN.md`, `resultados/estadistica_e2/`, salida de Ruff y pytest del 22/11/2026.
