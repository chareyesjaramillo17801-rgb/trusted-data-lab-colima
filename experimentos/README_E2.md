# E2 — Experimentos de Análisis Estadístico

Este módulo usa la captura local más reciente de SNIIV y **no hace peticiones a Internet**. No modifica los datos originales ni el pipeline existente.

## Ejecutar desde la raíz del repositorio

```powershell
python -m pip install -r requirements-e1.txt
python -m experimentos.e2_estadistica
```

El programa genera automáticamente en `resultados/estadistica_e2/`:

- `corridas_aleatorizadas.csv`: 90 mediciones (24 para 2³, 18 para 3×2 y 48 para 2⁴).
- `anova_2_3.csv`, `anova_3_2.csv`, `anova_2_4.csv`, `anova_fraccion.csv`.
- `fraccion_2_4_menos_1.csv`: 24 mediciones, fracción de resolución IV, I=ABCD.
- `diagnostico_*.json`: Shapiro, Levene y Durbin-Watson.
- `medias_tratamientos_2_3.csv`, `confirmacion.csv`, `resumen.json` e `INFORME.md`.

**Factor A:** tamaño de lote (128/512), o 64/256/1024 para diseño 3×2. **B:** conversión de municipio a categoría. **C:** ordenación previa. **D:** ordenación de grupos en `groupby`.

**Respuesta:** duración de 30 ciclos de agregación de registros SNIIV, medida en milisegundos. Todas las estrategias deben devolver exactamente la misma agregación. Los experimentos se ejecutan en orden aleatorio con semilla fija y 3 réplicas por tratamiento. La confirmación usa 5 mediciones nuevas de base y 5 de la combinación seleccionada.

Los resultados dependen de la computadora y la carga del sistema; no se deben sustituir por mediciones de otro equipo. No afirmar significancia estadística si los supuestos de ANOVA no se sostienen. Las 90 corridas se ejecutan localmente y el informe se genera después de medirlas.

**Nota:** los análisis estadísticos de este paquete miden desempeño computacional; no predicen el precio de viviendas. La comparación fraccionada reutiliza las corridas del factorial completo, por lo que no representa una campaña experimental independiente.
