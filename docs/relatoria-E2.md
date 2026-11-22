# Relatoría E2 — TRUSTED DATA LAB

**Proyecto:** Observatorio inmobiliario de Colima · **Modalidad:** individual · **Estado:** cierre pendiente.

## 1. Objetivo

Integrar cartografía oficial INEGI, permitir exploración municipal y reforzar trazabilidad de resultados Bronce–Plata–Oro, respetando límites éticos y de cobertura. La implementación documentada corresponde principalmente a Ingeniería de Datos.

## 2. Cronología y tiempo

- **09/11/2026:** incorporación de SHF según metadatos de Bronce; no consta hora exacta de descarga.
- **13/11/2026:** commits E1 de limpieza, modelos, tablero y validaciones (`37c8390`, `d37437a`, `65f2131`). Son antecedentes de E2.
- **22/11/2026, 14:36 -0600:** commit E2 [`1bdd739`](https://github.com/chareyesjaramillo17801-rgb/trusted-data-lab-colima/commit/1bdd739): geoespacial, linaje y ética.
- **22/11/2026:** validación local posterior de `gpd.sjoin()` con 10/10 municipios, 12 pruebas Pytest aprobadas y Ruff sin errores (informado por la desarrolladora); pendiente commit del cambio.

**Tiempo:** `calidad/tiempo-individual.csv` registra únicamente 8.25 h **estimadas retrospectivamente de E0**. No existe cronometraje verificable de E2; por integridad no se atribuyen horas ficticias a esta etapa.

## 3. Decisiones y alternativas

Se eligió INEGI en lugar de coordenadas de anuncios de renta no verificadas. Se guardó la respuesta original en Bronce, se validaron 10 polígonos y se exportó GeoJSON para el mapa. La unión `gpd.sjoin()` usa puntos representativos derivados de polígonos para validar correspondencia; **no** localiza inmuebles ni demuestra un vínculo espacial independiente con SHF/SNIIV. Se optó por OpenStreetMap frente a una capa que requería clave API. Se preservó la distinción entre indicadores estatales y municipales.

## 4. Defectos y correcciones

Los defectos E0 `D-01` y `D-02` están registrados en `calidad/defectos-individual.csv`. En E2 se documentaron dificultades de serialización GeoJSON, capa base con clave API, selección municipal y pérdida de columnas de linaje al regenerar CSV. Se aplicaron serialización compatible, OpenStreetMap, clic en polígonos y ejecutor `pipeline/ejecutar_analisis.py`. La bitácora original **no contiene identificadores ni fechas verificadas de detección de esos incidentes E2**; no se inventan.

## 5. Aprendizajes y límites por materia

- **Ingeniería de Datos:** la trazabilidad requiere IDs de origen, hashes, granularidad y fechas con método de obtención. El Excel SHF tiene metadato de incorporación `2026-11-09`, pero el pipeline aún usa `mtime_archivo_no_verificado`.
- **Estadística:** se dispone de pronósticos exploratorios previos; el experimento factorial y ANOVA específicos de E2 **no se evidencian** en este repositorio.
- **Calidad:** las pruebas automatizadas verifican comportamientos definidos, pero **no sustituyen** evaluación ISO ni auditoría cruzada externa, aún no acreditadas.

## 6. Evidencias, ética y herramientas

Repositorio: https://github.com/chareyesjaramillo17801-rgb/trusted-data-lab-colima. Ficha `docs/E2/ENTREGA.md`; linaje `docs/E2/LINAJE.md`; ética `docs/etica-datos.md`; pruebas `tests/test_e2.py`; bitácoras `calidad/`. La documentación ética distingue fuentes públicas, permisos, `robots.txt`, sesgos y privacidad. Se utilizó asistencia de IA (ChatGPT) para orientar revisión, redacción y propuesta de código; las decisiones, ejecuciones y validaciones se contrastaron con archivos y resultados locales. El dashboard público, el cierre de CI, el tag y el formulario deben verificarse al finalizar.
