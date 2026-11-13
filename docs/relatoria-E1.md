# Relatoría E1 — Observatorio inmobiliario de Colima

**Fecha de cierre documental:** 13 de noviembre de 2026  
**Repositorio:** https://github.com/chareyesjaramillo17801-rgb/trusted-data-lab-colima  
**Último commit de E1 verificado por la estudiante:** `1667b2a` (rama `main`)

## 1. Trabajo realizado

Se desarrolló y ejecutó un pipeline reproducible de datos por capas Bronce → Plata → Oro, con limpieza de textos, validaciones mediante Pandera, generación de cuarentena para registros rechazados y salidas analíticas. Se conservaron las capturas y los documentos de E0.

El pipeline local procesó **2,140 registros SNIIV**, todos válidos y ninguno rechazado, y **258 registros SHF de Colima**, todos válidos y ninguno rechazado. Generó **131 comparaciones** en la vista Oro. La ausencia de rechazos describe únicamente estas capturas; no demuestra por sí sola que las reglas de cuarentena cubran todos los defectos posibles.

## 2. Decisiones de tratamiento y calidad

- Los nulos de `Municipio` en los agregados estatales SHF son **estructurales**. No se imputaron ni se clasificaron como MCAR, MAR o MNAR sin evidencia estadística.
- Se preservaron las granularidades originales: SNIIV mensual y SHF trimestral. Para comparaciones se agregaron registros SNIIV por trimestre, sin convertir el índice SHF en precio individual o renta.
- Se analizaron valores atípicos mediante IQR y se conservaron los extremos potencialmente reales para no borrar observaciones válidas.
- Se documentaron transformaciones y vistas analíticas; las reglas de calidad permiten registrar el motivo de rechazo en cuarentena.

## 3. Modelado estadístico y validación

Se compararon **SES, Holt, Holt-Winters y ARIMA(1,1,1)** sobre las series trimestrales SHF, con **78 observaciones de entrenamiento** y **8 de prueba** por municipio.

| Municipio | Modelo con menor MAE | MAE de prueba | Observación |
|---|---|---:|---|
| Manzanillo | ARIMA(1,1,1) | 1.270822 | Selección por MAE entre cuatro candidatos |
| Villa de Álvarez | Holt | 2.165961 | Autocorrelación residual: Ljung-Box p ≈ 0.000284 |

Se ejecutaron diagnósticos ADF, ACF/PACF, descomposición de series y Ljung-Box. Los valores p ADF elevados, incluso después de la primera diferencia, **no permiten afirmar estacionariedad**. Se generaron ocho filas de pronósticos exploratorios (cuatro por municipio); sus bandas son heurísticas y **no intervalos de predicción calibrados**. Los resultados no representan pronósticos de renta ni precios individuales.

## 4. Evidencias de pruebas y automatización

- **Pruebas locales:** `python -m pytest -q` → **7 aprobadas**, con seis advertencias de compatibilidad.
- **Estilo y análisis estático:** `python -m ruff check pipeline tests` → **All checks passed!**
- **Auditoría de dependencias local:** `python -m pip_audit -r requirements-e1.txt` → **No known vulnerabilities found**.
- **Ejecución local:** `python -m pipeline.ejecutar`, `python -m pipeline.estadistica` y `python -m pipeline.analisis_e1` completadas.
- **CI:** la estudiante confirmó que **E1 calidad** terminó en verde para el commit `1667b2a`, tras incorporar comprobaciones de Ruff y auditoría de dependencias.
- **Evidencia CI:** https://github.com/chareyesjaramillo17801-rgb/trusted-data-lab-colima/actions (añadir enlace directo a la ejecución cuando esté disponible).

## 5. Defectos, seguridad y PSP/SQA

Se corrigieron observaciones de Ruff y una restricción de dependencia que impedía instalar la versión de pytest indicada por la auditoría como corregida. La auditoría posterior no reportó vulnerabilidades conocidas. **No se ha aportado un registro completo con fecha, duración, severidad y tiempo de corrección de cada defecto**; no se calculan métricas PSP sin esa evidencia.

El workflow E1 usa permisos de lectura del repositorio. **No se ha presentado evidencia de ejecución de Gitleaks**, ni de un respaldo probado y restaurado, ni un plan SQA IEEE 730 completo. Estas actividades deben realizarse o declararse pendientes en la entrega.

## 6. Disponibilidad y continuidad

La ejecución verde de E1 confirma una ejecución de CI, pero **no basta para calcular disponibilidad histórica, MTBF ni MTTR**. Se necesita el historial de ejecuciones de captura y calidad del período solicitado por el profesor, incluyendo fallas y tiempos de recuperación. No se atribuyen porcentajes ni tiempos ficticios.

## 7. Alcance, limitaciones y pendientes de cierre

El producto E1 incluye procesamiento y análisis reproducible, pero **no se ha confirmado un tablero desplegado**. Las bandas de pronóstico requieren calibración y el modelo Holt de Villa de Álvarez necesita revisión residual. Quedan por verificar el historial de capturas, evidencia de escaneo de secretos, SQA/PSP y la correspondencia final con la rúbrica del profesor.

**Estado:** documentación de resultados comprobados; **no equivale a declarar todos los requisitos de E1 terminados**. Crear el tag `e1` solamente después de la revisión final y de decidir explícitamente cómo documentar los requisitos pendientes.
