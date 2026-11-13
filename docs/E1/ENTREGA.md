# E1 — Avance técnico y evidencia

## Pipeline

`python -m pipeline.ejecutar` lee la última captura JSON SNIIV (excluye metadatos) y el Excel SHF de Bronce. Genera Parquet de Plata, cuarentena y Oro, más `data/oro/reporte_calidad.json`. El workflow `e1-calidad.yml` ejecuta pruebas y pipeline en GitHub Actions. La automatización de captura E0 es independiente; aún no está enlazada automáticamente a este workflow.

## Reglas de calidad

- Pandera valida esquema y rangos de registros aceptados; reglas por fila permiten conservar rechazados con `motivo_rechazo`.
- SNIIV: campos obligatorios, meses, años, municipios, claves y viviendas enteras no negativas, duplicados dimensionales.
- SHF: se filtra Colima antes de validar; nulos de Municipio son legítimos para el nivel estatal. El resto de México no se considera cuarentena.
- SNIIV mensual y SHF trimestral se conservan por separado. La comparación Oro agrega SNIIV a trimestre y une por municipio/año/trimestre.

## Faltantes e imputación

En SNIIV no se detectaron nulos en el diagnóstico inicial (2140 filas). En SHF hay nulos estructurales por nivel geográfico, no atribuibles automáticamente a MCAR/MAR/MNAR. No se imputan para no crear observaciones ficticias. La clasificación MCAR/MAR/MNAR no puede demostrarse estadísticamente a partir de nulos estructurales.

## Pendiente de evidencia para cerrar E1 integral

Ejecutar pruebas y pipeline en el equipo de entrega, registrar resultados, comprobar calidad y cobertura de capturas del periodo, analizar atípicos con justificación de tratamiento, documentar escalado/discretización/reducción cuando correspondan, ejecutar `python -m pipeline.estadistica` para generar diagnóstico ADF/ACF/PACF, atípicos IQR y comparación SES/Holt/Holt-Winters/ARIMA con 8 trimestres de prueba; completar intervalos y residuos, completar SQA/seguridad/PSP, relatoría y validación del tablero. No afirmar estos puntos como terminados sin evidencia.

## Estadística reproducible

Tras ejecutar el pipeline, `python -m pipeline.estadistica` genera `data/oro/comparacion_modelos.csv` y `data/oro/diagnostico_series.json`. Es un análisis preliminar: no publica pronósticos futuros ni intervalos; requiere revisión de residuos y justificación de selección final.
