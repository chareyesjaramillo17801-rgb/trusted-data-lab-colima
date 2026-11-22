# Experimentos E2 — Análisis Estadístico

**Fuente:** `data\bronce\sniiv_registro\registro_20261122T202044Z.json` (2140 registros).
**Ejecución UTC:** 2026-11-22T22:30:24.041311+00:00.
**Aleatorización:** semilla 20261122; tres réplicas por tratamiento.
**Respuesta:** milisegundos de 30 ciclos de agregación SNIIV local.
**Integridad:** cada tratamiento produjo la misma agregación que la referencia.

## Diseño 2³
A: tamaño 128/512; B: categoría no/sí; C: ordenación no/sí; agrupación con sort=False.
Mejor media observada: A=+, B=-, C=-.
ANOVA e interacciones: `anova_2_3.csv`; diagnóstico: `diagnostico_2_3.json`.

## Diseño 3×2
Tamaño de lote 64/256/1024 y conversión a categoría no/sí; ANOVA con interacción en `anova_3_2.csv`.

## Diseño 2⁴ completo y fracción 2^(4−1)
D: ordenamiento interno de groupby no/sí. Fracción regular D=ABC, relación definitoria I=ABCD.
Alias: A=BCD; B=ACD; C=ABD; D=ABC; AB=CD; AC=BD; AD=BC.
La fracción de resolución IV confunde interacciones de dos factores entre sí; no permite distinguirlas.
Resultados: `anova_2_4.csv`, `fraccion_2_4_menos_1.csv`, `anova_fraccion.csv`.

## Confirmación independiente
Media base: 248.947 ms; media seleccionada: 130.136 ms.
Cambio confirmado: 47.73% (positivo = más rápido).
La selección del mejor tratamiento puede sobreajustarse al ruido; la confirmación no garantiza mejora.

## Limitaciones
Una sola computadora y una captura histórica; tiempos afectados por carga del sistema y cachés.
Revisar normalidad de residuos y homogeneidad antes de interpretar significancia ANOVA.
No se ha realizado bloqueo por hora o máquina; el orden de las corridas sí fue aleatorizado.
Las métricas son de rendimiento del procesamiento, no estimaciones del mercado inmobiliario.
Las corridas reales y la salida del equipo que las ejecutó son la evidencia principal.
