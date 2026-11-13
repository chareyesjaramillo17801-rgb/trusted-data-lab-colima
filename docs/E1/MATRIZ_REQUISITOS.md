# Matriz de requerimientos verificables E1

| ID | Requisito verificable | Evidencia o método de comprobación | Estado |
|---|---|---|---|
| R-01 | Capturar fuentes SNIIV y SHF con trazabilidad | Bronce, metadatos y captura Actions | Implementado; revisar cobertura de fechas |
| R-02 | Generar Plata y Oro reproduciblemente | `python -m pipeline.ejecutar` y `reporte_calidad.json` | Verificado local y CI |
| R-03 | Rechazar filas inválidas indicando motivo | Pandera, cuarentena y prueba con registros defectuosos | Implementado; verificar prueba negativa |
| R-04 | Conservar granularidad mensual/trimestral | Parquet Plata/Oro y documentación | Verificado |
| R-05 | Comparar cuatro modelos con prueba retenida | `comparacion_modelos.csv`, MAE/RMSE/MAPE | Verificado |
| R-06 | Diagnosticar estacionariedad y residuos | ADF, ACF/PACF, Ljung-Box | Ejecutado; Holt Villa de Álvarez con autocorrelación residual |
| R-07 | Publicar pronóstico con intervalo validado | Tablero y prueba de cobertura del intervalo | **Pendiente: bandas actuales no calibradas** |
| R-08 | Demostrar fiabilidad y disponibilidad | Historial de Actions y tiempos de incidentes | Parcial: 84.62% de éxito; MTBF/MTTR no medidos |
| R-09 | Verificar dependencias y secretos | pip-audit, gitleaks | pip-audit verificado; gitleaks pendiente |
| R-10 | Mantener respaldo de Bronce | Copia externa verificable y prueba de restauración | Pendiente |
| R-11 | Ejecutar pruebas, lint y puerta de calidad en CI | Workflow E1 calidad verde | Verificado |
| R-12 | Documentar SQA y defectos | PLAN_SQA.md, SEGURIDAD_Y_CONFIABILIDAD.md | Documentado; revisión externa pendiente |
