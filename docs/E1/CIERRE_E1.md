# E1 — Evidencia, decisiones y límites

## Verificación local (13 de noviembre de 2026)

- `python -m pytest -q`: **7 pruebas aprobadas**, seis advertencias de compatibilidad.
- `python -m ruff check pipeline tests`: **All checks passed!**
- `python -m pip_audit -r requirements-e1.txt`: **No known vulnerabilities found**.
- `python -m pipeline.ejecutar`: 2,140 SNIIV válidos, 258 SHF Colima válidos, cero rechazados, 131 comparaciones Oro.
- `python -m pipeline.estadistica`: cuatro modelos por municipio, 78 trimestres de entrenamiento y ocho de prueba.
- `python -m pipeline.analisis_e1`: diagnósticos complementarios y ocho filas de pronósticos exploratorios.
- GitHub `main` publicó las correcciones en el commit `24f0a4a`; se informó una ejecución verde del workflow **anterior**.

## Faltantes, atípicos y transformaciones

No hay nulos en la captura SNIIV evaluada. Los nulos de `Municipio` de SHF a nivel estatal son estructurales; no es válido imputarlos ni asignarles MCAR/MAR/MNAR sin evidencia. Los atípicos IQR se señalan para revisión, no se eliminan automáticamente. El preprocesamiento produce transformaciones de escala y discretización; la serie SHF mantiene la escala original para pronósticos. Se preserva la distinción entre datos mensuales y trimestrales.

## Selección de modelos y limitaciones

Manzanillo: ARIMA(1,1,1), MAE 1.270822. Villa de Álvarez: Holt, MAE 2.165961. El p-valor ADF de las primeras diferencias es alto en ambos municipios, por lo que no se afirma estacionariedad. Holt de Villa de Álvarez presenta Ljung-Box p ≈ 0.000284: autocorrelación residual pendiente de corregir. Las bandas son **heurísticas, no intervalos calibrados**. No extrapolar el índice SHF a precios individuales o rentas.

## Seguridad y CI

La auditoría de dependencias y Ruff pasaron localmente. El workflow nuevo incorpora ambos controles; verificar que termine verde en GitHub tras publicar el cambio. El workflow mantiene `permissions: contents: read`.

## Pendientes documentados

Faltan evidencias verificadas para Gitleaks, respaldo Bronce, disponibilidad/MTBF/MTTR a partir de historial real, PSP, SQA IEEE 730 y tablero desplegado. No inventar métricas ni presentar esos puntos como concluidos. Conservar el enlace a la ejecución CI y sus artefactos antes de crear `e1`.
