# Evaluación E2 — Calidad del Observatorio inmobiliario de Colima

## ISO/IEC 25012: calidad de datos

Ejecutar `python -m calidad.evaluacion_e2` desde la raíz del repositorio. Produce `resultados/calidad_e2/metricas_iso25012.csv`, `.json` y `RESUMEN.md` sin modificar los archivos Oro.

**Atributos medidos:** completitud de celdas, unicidad de filas completas y presencia de origen/hash de linaje donde existan columnas. **No confundir** la ausencia estructural de un municipio en SHF con error; la unicidad de fila no sustituye la unicidad por clave de negocio. Los atributos de exactitud frente a fuentes externas, actualidad, credibilidad y accesibilidad requieren pruebas adicionales.

## ISO/IEC 25010: matriz de evidencia (modelo de ocho características)

| Característica | Evidencia que debe verificarse | Estado inicial |
|---|---|---|
| Adecuación funcional | Pruebas de pipeline, mapa municipal, filtros, reportes | Pendiente de medición E2 |
| Eficiencia de desempeño | Experimentos de Estadística E2: tiempos de procesamiento local | Evidencia disponible; alcance parcial |
| Compatibilidad | Ejecución local y despliegue Streamlit en navegadores diferentes | Pendiente de prueba cruzada |
| Usabilidad | Prueba de tareas con usuarios y registro de incidencias | Pendiente de evaluación con usuarios |
| Fiabilidad | Pytest, ejecuciones CI y comportamiento ante archivos defectuosos | Pendiente de recopilar evidencia fechada |
| Seguridad | Dependencias, secretos, controles de acceso, datos públicos | Pendiente de auditoría específica |
| Mantenibilidad | Ruff, estructura de módulos, pruebas y documentación | Pendiente de registrar salida E2 |
| Portabilidad | Instalación limpia en otro entorno, dependencias declaradas | Pendiente de prueba independiente |

No se asignan porcentajes arbitrarios a características no medidas. Documentar fecha, procedimiento, evidencia y resultado para cada característica.

## Comparación de marcos

| Marco | Propósito | Aplicación concreta |
|---|---|---|
| ISO/IEC 9126 | Modelo histórico de calidad de producto software (seis características) | Antecedente conceptual; no es la norma actual de evaluación |
| SQuaRE / ISO/IEC 25010 | Familia y modelo de calidad del producto software | Evaluar comportamiento y características del observatorio |
| ISO/IEC 25012 | Modelo de calidad de datos | Medir calidad de datasets Oro y explicitar limitaciones |
| ISO 9001 | Sistema de gestión de calidad organizacional | Gestión de procesos, evidencias, mejora y acciones correctivas; no certifica por sí sola el código |

**Nota de versión:** se emplea el modelo de ocho características de ISO/IEC 25010:2011 solicitado en la rúbrica; la edición de 2023 reorganiza las características y debe distinguirse si se exige actualidad normativa.

## Auditoría cruzada

Pendiente de recibir versión estable y evidencia del equipo asignado. Registrar repositorio/commit, fecha, alcance, hallazgos críticos/mayores/menores, pasos para reproducir, evidencias y recomendaciones. No emitir hallazgos sin revisión ni declarar recepción de auditoría externa sin acta.
