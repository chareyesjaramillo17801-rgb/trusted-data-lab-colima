# Plan SQA E1 — estructura alineada a IEEE 730

**Estado:** plan documentado; la ejecución de cada actividad debe acreditarse con evidencia real.

## 1. Propósito y alcance
Asegurar la calidad del pipeline SNIIV/SHF, los datos Plata/Oro, los pronósticos y el tablero de TRUSTED DATA LAB Colima.

## 2. Organización y responsabilidades
Responsable del proyecto: integrante desarrollador del observatorio. La revisión independiente debe ser realizada por el docente u otro revisor designado; **no se afirma que ya ocurrió**.

## 3. Normas, criterios y métricas
Integridad de datos y trazabilidad de fuentes; umbrales E0: 95% de ejecuciones exitosas, 98% de completitud y 100% de trazabilidad. El 84.62% observado no alcanza la meta de fiabilidad. Medir cobertura de esquemas, filas rechazadas, ejecución de CI y MAE/RMSE/MAPE.

## 4. Revisiones y auditorías
Revisión de fuentes y permisos, esquemas Pandera, lógica de cuarentena, métricas de pronóstico y supuestos de estacionariedad. Auditoría cruzada externa pendiente.

## 5. Pruebas y verificación
`python -m pytest -q`, `python -m ruff check pipeline tests`, `python -m pip_audit -r requirements-e1.txt`, `python -m pipeline.ejecutar`, `python -m pipeline.estadistica`, `python -m pipeline.analisis_e1`. E1 CI verde confirmado por el usuario en commit `1667b2a`; revisión de la relatoría publicada en `ef0d15b`.

## 6. Reporte de problemas y acciones correctivas
DEF-001: archivo `.metadata.json` seleccionado como datos. DEF-002: variable `columna_mes` no definida. Evidencia en logs de ejecuciones #3 y #6. Registrar corrección exacta y prueba de regresión cuando se identifiquen los commits.

## 7. Herramientas y control de versiones
Git/GitHub, GitHub Actions, Python, Pandera, pytest, Ruff, pip-audit. Conservar E0 mediante su tag; crear tag E1 solo después de revisión final.

## 8. Riesgos y acciones preventivas
Captura automática fallida; datos de diferente granularidad; cambios de esquema; nulos estructurales; fuga de secretos; pronósticos sin cobertura calibrada; dependencia de disponibilidad de fuentes. Mitigar con cuarentena, permisos mínimos, bitácoras, respaldo Bronce y documentación de limitaciones.
