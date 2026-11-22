# Entrega E2 — TRUSTED DATA LAB | Observatorio inmobiliario de Colima

**Modalidad:** individual. **Estado:** implementación local probada; cierre y tag `e2` pendientes.
**Repositorio:** https://github.com/chareyesjaramillo17801-rgb/trusted-data-lab-colima
**Commit base E2 publicado:** [`1bdd739`](https://github.com/chareyesjaramillo17801-rgb/trusted-data-lab-colima/commit/1bdd739) (22/11/2026, 14:36 -0600). Las correcciones posteriores se documentarán con su propio commit.

## Ingeniería de Datos: fuente especializada

- **Fuente oficial:** INEGI, Marco Geoestadístico, [servicio municipal de Colima](https://gaia.inegi.org.mx/wscatgeo/v2/geo/mgem/06).
- **Bronce:** `data/bronce/inegi/` (respuestas originales, fecha, URL y SHA-256).
- **Transformación:** [`pipeline/geoespacial_e2.py`](https://github.com/chareyesjaramillo17801-rgb/trusted-data-lab-colima/blob/main/pipeline/geoespacial_e2.py); valida 10 geometrías municipales y genera `data/oro/municipios_colima.geojson`.
- **Unión espacial verificable:** `pipeline/cruce_espacial_e2.py` calcula puntos representativos *derivados de los polígonos oficiales* y los relaciona con los mismos polígonos mediante `gpd.sjoin(..., predicate="within")`. Resultado local: **10/10 correspondencias**, sin discordancias. **Alcance:** validación geométrica, no georreferenciación de viviendas ni relación espacial independiente con los indicadores inmobiliarios.
- **Mapa:** [`dashboard/app.py`](https://github.com/chareyesjaramillo17801-rgb/trusted-data-lab-colima/blob/main/dashboard/app.py), con polígonos seleccionables y fondo OpenStreetMap. Funcionamiento local probado; **publicación actualizada en Streamlit Cloud aún no comprobada**.
- **Pruebas:** `tests/test_e2.py`; última ejecución local comunicada: **12 pruebas Pytest aprobadas** y **Ruff sin errores**.

## Ingeniería de Datos: linaje Bronce → Plata → Oro

- [`docs/E2/LINAJE.md`](https://github.com/chareyesjaramillo17801-rgb/trusted-data-lab-colima/blob/main/docs/E2/LINAJE.md) describe IDs de observaciones, rutas Bronce, SHA-256, agregados y productos analíticos.
- SNIIV: 2,140 registros procesados; SHF Colima: 258 registros (incluye agregado estatal, **no** municipio de Colima); 131 comparaciones municipales Oro; INEGI: 10 municipios.
- Los modelos conservan IDs históricos: 8 comparaciones (78 entrenamiento + 8 prueba), 8 pronósticos (86 referencias) y 2 diagnósticos (86 referencias).
- **Limitación SHF:** el pipeline utiliza la fecha de modificación del archivo como `fecha_ingesta_utc`, marcada `mtime_archivo_no_verificado`. Sin embargo, el archivo `data/bronce/shf/Indice_SHF_datos_abiertos_2_trim_2026.metadata.json` consigna `retrieved_date: 2026-11-09` como fecha de incorporación al proyecto **sin hora exacta**. La fecha de archivo no debe presentarse como captura UTC confirmada.

## Ingeniería de Datos: ética y legalidad

[`docs/etica-datos.md`](https://github.com/chareyesjaramillo17801-rgb/trusted-data-lab-colima/blob/main/docs/etica-datos.md) documenta fuentes SNIIV, SHF e INEGI; términos de uso, atribución, `robots.txt`, privacidad, sesgos y límites de interpretación. La revisión de licencias individuales se mantiene diferenciada de los permisos generales.

## Estadística: evidencia de E2

**No acreditada en el repositorio revisado:** diseño factorial 2³ con aleatorización y réplicas, ANOVA de dos factores con tres niveles en uno, comparación factorial completo/fraccionado 2⁴ vs. 2^(4−1), análisis de residuos y corrida confirmatoria. Los pronósticos existentes de E1 **no sustituyen** estas evidencias. Deben realizarse y enlazarse antes de afirmar cumplimiento integral.

## Calidad: evidencia de E2

**No acreditada en el repositorio revisado:** evaluación E2 con métricas ISO/IEC 25010 y 25012, contraste 9126/SQuaRE/9001 y auditoría cruzada de otro equipo con recepción de auditoría. `docs/E1/PLAN_SQA.md` es un plan previo, no prueba de ejecución de E2. La auditoría externa depende de un tercero; no debe inventarse.

## Evidencias y cierre

- [`docs/relatoria-E2.md`](https://github.com/chareyesjaramillo17801-rgb/trusted-data-lab-colima/blob/main/docs/relatoria-E2.md): cronología, incidencias y limitaciones.
- [`calidad/defectos-individual.csv`](https://github.com/chareyesjaramillo17801-rgb/trusted-data-lab-colima/blob/main/calidad/defectos-individual.csv) y [`calidad/tiempo-individual.csv`](https://github.com/chareyesjaramillo17801-rgb/trusted-data-lab-colima/blob/main/calidad/tiempo-individual.csv): bitácoras, con registro temporal de E2 no medido.
- **Pendientes antes del cierre:** verificar Streamlit Cloud; correr CI después del commit de cierre; confirmar alcance de evaluación de las tres materias; crear tag `e2` sobre el commit final; enviar enlace al formulario oficial.
