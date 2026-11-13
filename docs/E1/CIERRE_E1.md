# E1 — Evidencia, decisiones y límites

## Resultados verificados antes de esta actualización

El usuario ejecutó `pytest -q` con 6 pruebas aprobadas. `pipeline.ejecutar` reportó 2140 SNIIV válidos, 258 SHF de Colima válidos, cero rechazados y 131 comparaciones trimestrales. `pipeline.estadistica` comparó SES, Holt, Holt-Winters y ARIMA con 78 trimestres de entrenamiento y ocho de prueba. GitHub Actions de E1 fue reportado en verde por el usuario. Estos resultados son de la versión anterior y deben verificarse nuevamente después de instalar la actualización.

## Datos faltantes y mecanismo

SNIIV no presenta valores nulos en la captura evaluada. SHF contiene nulos de Municipio en agregados estatales; son nulos estructurales, no observaciones faltantes de municipios. No es defendible inferir MCAR/MAR/MNAR ni imputar estos campos. Se conserva nivel estatal y municipal sin inventar datos.

## Atípicos y transformación

El módulo `analisis_e1.py` señala atípicos IQR globales de viviendas como indicadores de revisión; no los borra porque los conteos tienen asimetría y el extremo puede ser real. Se producen Z-score y Min-Max por municipio, además de bandas de conteo. La serie SHF conserva su escala original para pronóstico. Se generan atributos trimestrales y una vista analítica; se evita mezclar las granularidades originales.

## Modelos, diagnósticos y límites

La comparación inicial utiliza 8 trimestres retenidos. El análisis complementario reentrena el modelo seleccionado por MAE y reporta ADF, descomposición aditiva, Ljung-Box y cuatro pronósticos trimestrales exploratorios. Las bandas generadas son **heurísticas basadas en residuos, no intervalos de predicción calibrados**. Un p-valor ADF alto no permite afirmar estacionariedad; un Ljung-Box bajo indica autocorrelación residual que requiere revisar el modelo. No interpretar el pronóstico como precio individual de viviendas ni como oferta de renta.

## Seguridad, PSP y disponibilidad

El workflow usa `permissions: contents: read`. La auditoría de dependencias con `pip-audit`, escaneo de secretos con `gitleaks`, política de respaldo, MTBF/MTTR y SQA IEEE 730 requieren ejecución/evidencia adicional. No inventar valores de disponibilidad ni defectos. Consultar bitácoras reales de GitHub Actions para calcular tasa de éxito del periodo requerido.

## Verificación antes del tag e1

1. Ejecutar pipeline, pruebas, análisis y linter; comprobar que CI termina verde.
2. Revisar `data/oro/diagnostico_ampliado.csv` y `pronosticos_exploratorios.csv`.
3. Adjuntar enlace de ejecución de Actions y registrar horas/defectos reales en PSP.
4. Revisar requerimientos del profesor y no afirmar tablero desplegado si no existe.
5. Crear tag `e1` sólo después de cerrar lo obligatorio y documentar limitaciones.
