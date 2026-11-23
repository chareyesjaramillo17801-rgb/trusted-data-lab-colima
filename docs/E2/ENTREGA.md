# Entrega E2 — TRUSTED DATA LAB | Observatorio inmobiliario de Colima

**Modalidad:** individual. **Corte documental:** 22 de noviembre de 2026. **Estado:** implementaciones y evaluaciones internas publicadas en `main`; auditoría cruzada externa pendiente.

**Repositorio:** https://github.com/chareyesjaramillo17801-rgb/trusted-data-lab-colima  
**Último commit de Calidad confirmado:** [`5b83f12`](https://github.com/chareyesjaramillo17801-rgb/trusted-data-lab-colima/commit/5b83f12).  
**Tag `e2`:** https://github.com/chareyesjaramillo17801-rgb/trusted-data-lab-colima/tree/e2 — **advertencia:** apunta a la versión anterior a la integración de Estadística y Calidad; para revisar todas las evidencias recientes usar `main` hasta definir el cierre de versión.

## 1. Ingeniería de Datos — fuente especializada y cruce espacial

- **Fuente oficial:** INEGI, Marco Geoestadístico, [municipios de Colima](https://gaia.inegi.org.mx/wscatgeo/v2/geo/mgem/06).
- **Bronce:** `data/bronce/inegi/` con respuesta original, URL, fecha y hash SHA-256.
- **Transformación:** [`pipeline/geoespacial_e2.py`](../../pipeline/geoespacial_e2.py), con 10 geometrías municipales y producto `data/oro/municipios_colima.geojson`.
- **Cruce espacial:** [`pipeline/cruce_espacial_e2.py`](../../pipeline/cruce_espacial_e2.py) emplea `gpd.sjoin()` entre puntos representativos **derivados de los polígonos oficiales** y los mismos polígonos. Verificación local: 10/10 coincidencias. Es una **validación geométrica interna**, no georreferenciación de viviendas ni vinculación espacial independiente de registros inmobiliarios.
- **Dashboard:** [`dashboard/app.py`](../../dashboard/app.py); mapa municipal interactivo con OpenStreetMap. Se comprobó la interacción municipal en el [dashboard desplegado](https://trusted-data-lab-colima-8dbknfsg2lhzub8uvrrhqo.streamlit.app).
- **Linaje:** [`docs/E2/LINAJE.md`](LINAJE.md) documenta IDs, rutas Bronce, hashes, agregados y límites de trazabilidad. SNIIV: 2,140 registros; SHF Colima: 258; comparaciones municipales Oro: 131; INEGI: 10 municipios.
- **Ética:** [`docs/etica-datos.md`](../etica-datos.md), con fuentes, términos, licencias, `robots.txt`, sesgos, privacidad y límites de interpretación.
- **Límite de fechas SHF:** `retrieved_date: 2026-11-09` registra incorporación sin hora exacta; `mtime_archivo_no_verificado` no constituye prueba de fecha de descarga.

## 2. Análisis Estadístico — diseños, ANOVA y confirmación

- **Informe:** [`docs/E2/estadistica/INFORME_ESTADISTICA_E2.md`](estadistica/INFORME_ESTADISTICA_E2.md).
- **Reproducción:** [`experimentos/e2_estadistica.py`](../../experimentos/e2_estadistica.py) y [`experimentos/README_E2.md`](../../experimentos/README_E2.md).
- **Resultados originales:** [`resultados/estadistica_e2/`](../../resultados/estadistica_e2/) — corridas aleatorizadas, ANOVA de los diseños factoriales 2³, 3×2 y 2⁴, fracción 2^(4−1), diagnósticos, medias y confirmación.
- **Ejecución local comunicada:** 90 corridas principales; fracción de 24 observaciones **seleccionadas del diseño completo** (no experimento independiente); 10 mediciones de confirmación. Reducción media reportada del tiempo de procesamiento: **47.73 %** (248.95 ms a 130.14 ms), para ese entorno y esa comparación.
- **Interpretación y límites:** los diagnósticos de normalidad requieren cautela en 3×2 (Shapiro p≈0.0423) y fraccionado (p≈0.0214); el fraccionado tiene alias por `I=ABCD`, entre otros `AB=CD`. Las mediciones de rendimiento no son predicciones del mercado inmobiliario.
- **Gráficas:** [`docs/E2/estadistica/graficas/`](estadistica/graficas/).

## 3. Calidad — ISO/IEC 25010, 25012 y auditoría

- **Informe y matriz:** [`docs/E2/calidad/INFORME_CALIDAD_E2.md`](calidad/INFORME_CALIDAD_E2.md) y [`PLAN_EVALUACION.md`](calidad/PLAN_EVALUACION.md). Incluyen evaluación de ISO/IEC 25010 y contraste de ISO/IEC 9126, SQuaRE e ISO 9001, con los límites de las evidencias disponibles.
- **Programa de evaluación:** [`calidad/evaluacion_e2.py`](../../calidad/evaluacion_e2.py).
- **Métricas verificables:** [`resultados/calidad_e2/`](../../resultados/calidad_e2/): siete productos Oro evaluados, cero filas completamente duplicadas y cuatro productos con completitud del 100 %. Otros productos requieren interpretación de nulos estructurales y comprobación adicional de trazabilidad.
- **Verificaciones de código:** Ruff sin errores en el módulo de Calidad y 12 pruebas Pytest aprobadas en la ejecución local comunicada.
- **Auditoría cruzada:** [`docs/E2/calidad/PLANTILLA_AUDITORIA_CRUZADA.md`](calidad/PLANTILLA_AUDITORIA_CRUZADA.md). **No ejecutada todavía**: falta recibir el repositorio del equipo asignado y la auditoría de retorno. No se reportan defectos externos no comprobados.

## 4. Relatoría, evidencias y cierre

- **Relatoría E2:** [`docs/relatoria-E2.md`](../relatoria-E2.md), con cronología, decisiones, incidencias, límites y declaración de uso de IA.
- **Bitácoras:** [`calidad/defectos-individual.csv`](../../calidad/defectos-individual.csv) y [`calidad/tiempo-individual.csv`](../../calidad/tiempo-individual.csv). El tiempo E2 no se presenta como cronometraje exacto cuando no existe registro.
- **Pendientes reales:** auditoría cruzada bidireccional; comprobación de los hallazgos de nulos/linaje; verificación de CI tras el commit documental; acordar versión final del tag `e2` para que incluya las tres materias; confirmar canal oficial de entrega cuando sea comunicado.

**Nota:** la existencia de archivos y las pruebas aprobadas no acreditan por sí solas todos los criterios de la rúbrica; la evaluación docente y la auditoría externa siguen pendientes.
