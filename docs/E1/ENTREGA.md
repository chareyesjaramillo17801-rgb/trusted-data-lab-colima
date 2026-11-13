# E1 — Avance técnico y evidencias

## Pipeline y calidad de datos

`python -m pipeline.ejecutar` procesa la última captura JSON SNIIV y el Excel SHF de Bronce. Genera Parquet de Plata, cuarentena y Oro, además de `data/oro/reporte_calidad.json`. La captura E0 y el workflow E1 son independientes; el segundo se ejecuta en cada push a `main`, en pull requests o manualmente.

En la ejecución local verificada el 13 de noviembre de 2026 se procesaron **2,140 registros SNIIV válidos** y **258 registros SHF de Colima válidos**, con **cero rechazados** y **131 comparaciones** en Oro. Cero rechazados no significa que se haya probado la cuarentena ante todos los defectos posibles.

Pandera valida esquemas y rangos; las reglas por fila permiten conservar registros rechazados con su motivo. SHF se filtra a Colima antes de validar. Los nulos de `Municipio` en agregados estatales son estructurales; no se imputan ni se clasifican arbitrariamente como MCAR/MAR/MNAR. SNIIV mensual y SHF trimestral conservan sus granularidades originales; las comparaciones se hacen por trimestre.

## Preprocesamiento y análisis

El análisis complementario registra atípicos por IQR para revisión, sin eliminarlos automáticamente, y produce transformaciones de escala y bandas de conteo. La serie SHF mantiene su escala original para modelado. Consultar `data/oro/diagnostico_preprocesamiento.json` y los archivos Oro generados para comprobar los resultados exactos.

`python -m pipeline.estadistica` compara SES, Holt, Holt-Winters y ARIMA(1,1,1) usando 78 trimestres de entrenamiento y ocho de prueba para cada municipio. Resultados locales verificados:

| Municipio | Mejor modelo por MAE | MAE | RMSE | MAPE (%) |
|---|---|---:|---:|---:|
| Manzanillo | ARIMA(1,1,1) | 1.270822 | 1.626301 | 0.622588 |
| Villa de Álvarez | Holt | 2.165961 | 2.477812 | 1.060982 |

`python -m pipeline.analisis_e1` genera descomposición aditiva, ADF, Ljung-Box y ocho filas de pronósticos exploratorios (cuatro por municipio). **Las bandas no son intervalos de predicción calibrados**. Los valores p de ADF de la primera diferencia fueron 0.920482 (Manzanillo) y 0.990787 (Villa de Álvarez): no se ha demostrado estacionariedad. Para Holt de Villa de Álvarez, Ljung-Box dio p ≈ 0.000284, señal de autocorrelación residual; su selección por MAE no equivale a validación definitiva del modelo. El índice SHF no representa precios individuales ni ofertas de renta.

## Pruebas, automatización y seguridad

En el equipo local, después de las correcciones de código, se verificó: `python -m ruff check pipeline tests` sin observaciones, `python -m pytest -q` con **7 pruebas aprobadas** (y advertencias de compatibilidad), ejecución correcta de los tres módulos y `python -m pip_audit -r requirements-e1.txt` sin vulnerabilidades conocidas. Los cambios de código se publicaron en `main` mediante commit `24f0a4a`; se informó que el workflow anterior terminó en verde.

El workflow actualizado incluye Ruff y `pip-audit`, además del pipeline, pruebas y análisis. **Su ejecución en GitHub deberá verificarse después de publicar esta actualización**. Un resultado local no sustituye la evidencia de CI.

## Evidencias y limitaciones por cerrar

Guardar el enlace a la ejecución verde de GitHub Actions y descargar el artefacto `e1-reporte-calidad`. Revisar cobertura y fallos de capturas del periodo solicitado antes de calcular disponibilidad o MTBF/MTTR. No se cuenta todavía con evidencia confirmada de escaneo Gitleaks, respaldo verificable, SQA IEEE 730 completo, bitácora PSP cuantificada ni tablero desplegado. No declarar estos requisitos terminados sin evidencia. Documentar los pendientes como limitaciones de la entrega y contrastarlos con la rúbrica del profesor.

## Reproducción

```powershell
python -m pip install -r requirements-e1.txt
python -m pipeline.ejecutar
python -m pytest -q
python -m ruff check pipeline tests
python -m pipeline.estadistica
python -m pipeline.analisis_e1
```

Para auditar dependencias localmente, instalar `pip-audit` y ejecutar `python -m pip_audit -r requirements-e1.txt`.
