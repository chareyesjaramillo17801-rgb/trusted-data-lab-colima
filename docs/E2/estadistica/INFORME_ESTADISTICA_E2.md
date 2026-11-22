# E2 â€” Informe de AnÃ¡lisis EstadÃ­stico

**Proyecto:** TRUSTED DATA LAB â€” Observatorio inmobiliario de Colima
**Fecha de ejecuciÃ³n:** 22 de noviembre de 2026, 22:30:24 UTC
**Fuente local:** `data/bronce/sniiv_registro/registro_20261122T202044Z.json`, 2,140 registros
**Software registrado:** Python 3.13.15, pandas 2.3.3
**Respuesta:** tiempo de ejecuciÃ³n en milisegundos para 30 ciclos de agregaciÃ³n de registros SNIIV. Menor es mejor.

## 1. Objetivo e hipÃ³tesis

Determinar cÃ³mo afectan distintas decisiones de procesamiento al tiempo de agregaciÃ³n de registros SNIIV. Para cada efecto principal e interacciÃ³n, la hipÃ³tesis nula del ANOVA es que su efecto es cero, con Î± = 0.05. El resultado mide rendimiento informÃ¡tico, **no precios, demanda ni oferta de vivienda**.

## 2. Protocolo y trazabilidad

Los diseÃ±os utilizaron tres rÃ©plicas por tratamiento y un orden aleatorizado (semilla 20261122). Se utilizaron datos locales, sin llamar a fuentes externas. La implementaciÃ³n reporta que todos los tratamientos produjeron la misma agregaciÃ³n que la referencia. Se conservaron las 90 mediciones originales en `corridas_aleatorizadas.csv` y los resultados estadÃ­sticos en `RESULTADOS_ESTADISTICA_E2.zip`.

**PrecauciÃ³n:** los experimentos comparten computadora y captura; no se bloquearon variaciones de carga del sistema, hora o cachÃ©. La aleatorizaciÃ³n reduce sesgos sistemÃ¡ticos pero no elimina esos efectos.

## 3. Factorial 2Â³ â€” 24 corridas

Factores: A tamaÃ±o de lote (128 frente a 512), B conversiÃ³n a categorÃ­a (no/sÃ­), C ordenaciÃ³n previa (no/sÃ­). Ocho tratamientos, tres rÃ©plicas cada uno. El modelo ANOVA incluye los tres efectos principales, tres interacciones de dos factores y la interacciÃ³n triple.

| TÃ©rmino | F | p | InterpretaciÃ³n a Î±=0.05 |
|---|---:|---:|---|
| C(factor_a) | 2347.74 | 8.68e-19 | Significativo |
| C(factor_b) | 750.57 | 7.14e-15 | Significativo |
| C(factor_c) | 2022.70 | 2.84e-18 | Significativo |
| C(factor_a):C(factor_b) | 167.88 | 6.72e-10 | Significativo |
| C(factor_a):C(factor_c) | 580.66 | 5.31e-14 | Significativo |
| C(factor_b):C(factor_c) | 23.64 | 0.000173 | Significativo |
| C(factor_a):C(factor_b):C(factor_c) | 0.02 | 0.88 | No significativo |

La interacciÃ³n triple no fue significativa (p=0.8804); las interacciones dobles sÃ­ lo fueron. Por ello, los efectos principales deben interpretarse junto con las interacciones. El tratamiento con menor media observada fue A=+ (512), B=âˆ’ (sin categorÃ­a), C=âˆ’ (sin ordenaciÃ³n), segÃºn `medias_tratamientos_2_3.csv`.

![Significancia ANOVA 2Â³](graficas/anova_2_3.png)

## 4. DiseÃ±o de dos factores 3Ã—2 â€” 18 corridas

Factor A: tamaÃ±os de lote 64, 256 y 1024; factor B: conversiÃ³n a categorÃ­a no/sÃ­. Se observÃ³ evidencia estadÃ­stica de efecto de A (p=6.86Ã—10â»Â¹âµ), B (p=2.91Ã—10â»Â¹â´) y su interacciÃ³n (p=9.27Ã—10â»Â¹Â³). **LimitaciÃ³n:** Shapiro-Wilk sobre los residuos dio p=0.0423; por tanto se rechaza normalidad a Î±=0.05 y las inferencias paramÃ©tricas requieren cautela. Levene p=0.907 no mostrÃ³ evidencia de heterogeneidad de varianzas.

## 5. Factorial 2â´ completo frente a fracciÃ³n 2^(4âˆ’1)

El factorial completo empleÃ³ 16 tratamientos Ã— 3 rÃ©plicas = 48 corridas. Se agregÃ³ D: ordenaciÃ³n interna de `groupby` (no/sÃ­). A, B y C tuvieron efectos principales significativos; D no (p=0.8056). Se detectaron interacciones significativas, entre ellas AB, AC y BC. Consultar `anova_2_4.csv` para los resultados completos.

La fracciÃ³n regular utiliza **D=ABC**, con relaciÃ³n definitoria **I=ABCD** y resoluciÃ³n IV. Alias: A=BCD; B=ACD; C=ABD; D=ABC; AB=CD; AC=BD; AD=BC. Por ello no permite identificar por separado interacciones de dos factores confundidas. Las 24 observaciones de la fracciÃ³n se **seleccionaron de las 48 del factorial completo**: no constituyen 24 corridas adicionales independientes. El ANOVA fraccionado disponible ajusta solamente efectos principales, por lo que puede absorber interacciones omitidas en el error. Su Shapiro-Wilk p=0.0214 cuestiona normalidad y limita la inferencia. En el modelo ajustado A, B y C fueron significativos y D no.

## 6. Corridas de confirmaciÃ³n â€” 10 mediciones

Se ejecutaron cinco mediciones de la configuraciÃ³n base y cinco del tratamiento seleccionado. Sus medias fueron **248.947 ms** y **130.136 ms**, respectivamente, una reducciÃ³n de **47.73%** calculada como (baseâˆ’seleccionada)/base Ã— 100. La confirmaciÃ³n es independiente de las corridas de selecciÃ³n en el sentido de que son mediciones adicionales, pero se realizÃ³ en el mismo entorno y no garantiza una mejora generalizable.

![ComparaciÃ³n de confirmaciÃ³n](graficas/confirmacion_boxplot.png)

## 7. Conclusiones y lÃ­mites de validez

En esta ejecuciÃ³n local, evitar ordenaciÃ³n previa y conversiÃ³n a categorÃ­a con lote de 512 dio la mejor media entre los tratamientos del factorial 2Â³. El experimento de confirmaciÃ³n mostrÃ³ una reducciÃ³n media del tiempo de 47.73% frente a la configuraciÃ³n base. La presencia de interacciones y las violaciones de normalidad detectadas obligan a interpretar con cautela algunas pruebas ANOVA; no deben presentarse como prueba de causalidad generalizable a otras mÃ¡quinas o capturas. La fracciÃ³n 2^(4âˆ’1) ahorra tratamientos pero confunde interacciones de segundo orden. Para fortalecer la validez externa se recomienda repetir en varias sesiones y computadoras, bloquear por sesiÃ³n y estudiar los residuos grÃ¡ficamente.

## 8. Evidencias

- `corridas_aleatorizadas.csv`: mediciones individuales y orden de ejecuciÃ³n.
- `anova_2_3.csv`: ANOVA principal del diseÃ±o 2Â³.
- `confirmacion.csv`: diez corridas de confirmaciÃ³n.
- `graficas/`: visualizaciones reproducidas desde CSV originales.
- **Archivo fuente que debe conservarse:** `RESULTADOS_ESTADISTICA_E2.zip`, con los 14 archivos originales, incluyendo todos los ANOVA, diagnÃ³sticos y fracciÃ³n.

**Nota de transparencia:** este informe fue elaborado con asistencia de IA a partir de los resultados entregados; no sustituye los archivos originales ni una auditorÃ­a de la implementaciÃ³n experimental.
