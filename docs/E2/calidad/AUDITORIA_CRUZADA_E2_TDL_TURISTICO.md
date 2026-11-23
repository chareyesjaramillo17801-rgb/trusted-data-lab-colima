# Auditoría cruzada E2 — Observatorio turístico de Colima

**Equipo auditor:** Observatorio inmobiliario de Colima (TRUSTED DATA LAB)
**Proyecto auditado:** [tdl-turistico-colima](https://github.com/Leslie581/tdl-turistico-colima)
**Fecha de revisión documental:** 2026-11-23
**Alcance:** documentación pública E2 en rama `main`; esta revisión **no equivale a ejecución independiente de pruebas ni certificación ISO**.

## Metodología
Se contrastaron la ficha de entrega E2, las evaluaciones ISO/IEC 25010 y 25012, y el documento geoespacial. Los hallazgos se clasifican por impacto potencial y por incumplimiento declarado. Las cifras se atribuyen a los resultados publicados por el equipo auditado, **no a mediciones independientes del auditor**.

## Hallazgos

### AC-E2-01 — Mayor — Incumplimiento de RNF-PRI-03 en oferta municipal
**Criterio:** El propio proyecto exige no publicar conteos exactos inferiores a tres establecimientos.
**Evidencia:** Su evaluación ISO/IEC 25012 reporta **28 de 88 celdas** con conteos exactos de 1 o 2 establecimientos (12 celdas de 1; 16 de 2) en `manzanillo_oferta_hospedaje.csv`. La ficha E2 confirma el incumplimiento y la decisión de documentarlo sin modificar el producto en E2.
**Impacto:** Incumplimiento verificable del requisito de privacidad definido por el equipo; puede facilitar la identificación de categorías con muy pocos establecimientos. **No implica por sí solo una filtración de datos personales**, dado que el equipo declara que los datos base DENUE son públicos.
**Recomendación:** Establecer una estrategia de publicación coherente entre bronce, oro y tablero; si el requisito se mantiene, implementar supresión/rangos en el agregado municipal, revisar inferencia por totales y versionar el cambio de contrato. Mantener explícita la limitación de datos ya publicados.
**Fuentes:** [ISO 25012](https://github.com/Leslie581/tdl-turistico-colima/blob/main/docs/E2/iso25012.md) · [ENTREGA E2](https://github.com/Leslie581/tdl-turistico-colima/blob/main/docs/E2/ENTREGA.md).

### AC-E2-02 — Mayor — Objetivo O1 de fiabilidad no alcanzado
**Criterio:** Objetivo O1: al menos 95 % de éxito en cualquier ventana completa de siete días.
**Evidencia:** El informe ISO/IEC 25010 registra una peor ventana de **9 éxitos en 10 ejecuciones (90 %)** y tasa global de **15/16 (93.8 %)** al corte. El equipo reconoce que el indicador posterior a la corrección no borra el incumplimiento histórico.
**Impacto:** Incumplimiento del objetivo de fiabilidad y riesgo de capturas faltantes ante nuevas fallas de configuración.
**Recomendación:** Añadir validación previa de configuración al flujo automatizado, alertas de ejecución fallida y medición continua por ventanas móviles; mantener el incidente en la serie histórica.
**Fuentes:** [ISO 25010](https://github.com/Leslie581/tdl-turistico-colima/blob/main/docs/E2/iso25010.md) · [ENTREGA E2](https://github.com/Leslie581/tdl-turistico-colima/blob/main/docs/E2/ENTREGA.md).

### AC-E2-03 — Menor — Diccionario incompleto para agregado AGEB
**Criterio:** Comprensibilidad y documentación de columnas de los productos de oro.
**Evidencia:** El informe ISO/IEC 25012 reporta **0 de 12 columnas** del agregado AGEB incluidas en `diccionario_datos.csv`, aunque aclara que están explicadas en documentación especializada.
**Impacto:** Dificulta a terceros interpretar y reutilizar el agregado sin consultar varias fuentes.
**Recomendación:** Extender la generación del diccionario en `pipeline/oro.py`, incorporar las doce columnas y comprobarlo con prueba automática.
**Fuentes:** [ISO 25012](https://github.com/Leslie581/tdl-turistico-colima/blob/main/docs/E2/iso25012.md) · [Geoespacial](https://github.com/Leslie581/tdl-turistico-colima/blob/main/docs/E2/geoespacial.md).

### AC-E2-04 — Menor — Etapa geoespacial fuera de la ejecución principal
**Criterio:** Integración operativa y reproducibilidad del pipeline E2.
**Evidencia:** `docs/E2/ENTREGA.md` reconoce que `python -m pipeline.geoespacial agregar` se ejecuta por separado y no está incorporado a `pipeline.ejecutar` ni a la captura diaria.
**Impacto:** El mapa puede mostrar un corte anterior a las capturas recientes si no se ejecuta manualmente la agregación. No se demuestra pérdida de registros: el equipo documenta equivalencia de contenido entre las capturas del 21 y 22 de noviembre.
**Recomendación:** Incorporar el agregado geoespacial como etapa posterior a una captura validada, o automatizar una comprobación que detecte diferencias y advierta de la antigüedad del mapa.
**Fuentes:** [ENTREGA E2](https://github.com/Leslie581/tdl-turistico-colima/blob/main/docs/E2/ENTREGA.md) · [Geoespacial](https://github.com/Leslie581/tdl-turistico-colima/blob/main/docs/E2/geoespacial.md).

## Observaciones sin clasificación como defecto
- **Actualidad de DataTur:** 23 meses de rezago frente al corte; la documentación lo atribuye a la fuente abierta y lo señala como limitación, no como error demostrado del pipeline.
- **Diseño 2⁴ / 2⁴⁻¹:** la ficha declara que son matrices teóricas sin mediciones del factor D; no debe afirmarse que se ejecutaron esas corridas experimentales.
- **Revisión independiente:** esta auditoría examinó documentación pública. No se verificaron de manera independiente los 266 linajes, la suite de pruebas, las 134 asignaciones geoespaciales ni los indicadores reportados.

## Dictamen documental
El proyecto presenta evidencias documentales de integración geoespacial, experimentación estadística y evaluación de calidad. **Se identificaron dos hallazgos mayores y dos menores**, todos sustentados en limitaciones o incumplimientos expresamente declarados por el equipo. No se identificó un defecto crítico con la evidencia examinada. La evaluación no determina aprobación o rechazo integral de E2 y queda sujeta a validación técnica independiente si la rúbrica la exige.

**Estado:** borrador de auditoría documental listo para revisión y firma del equipo auditor; no se ha enviado ni aceptado por el equipo auditado.

## Verificación técnica complementaria — 23 de noviembre de 2026

**Repositorio auditado:** https://github.com/Leslie581/tdl-turistico-colima

**Commit auditado:** `73e741ca3bc9130ad63bb0bb2f6a1a865210b359`

**Método:** clonación independiente del repositorio, inspección de archivos CSV y JSON, y búsqueda estática de referencias en el código y workflows. No se ejecutaron las pruebas automatizadas del proyecto auditado.

### AC-E2-01 — Privacidad

Archivo: `data/oro/manzanillo_oferta_hospedaje.csv`.

Se verificaron 88 filas. De ellas, 28 contienen valores de `establecimientos` iguales a 1 o 2: 12 filas con valor 1 y 16 con valor 2.

Porcentaje afectado: 31.82 %.

### AC-E2-02 — Fiabilidad

Archivo: `docs/E2/evidencia/iso25010.json`.

El criterio exige al menos 95 % de éxito en cualquier ventana completa de siete días.

- Peor ventana histórica: 9 éxitos y 1 fallo, equivalente al 90 %.
- Tasa global observada: 15 éxitos de 16 ejecuciones, equivalente al 93.75 %.
- Dictamen del propio equipo: NO CUMPLE.
- Después de la corrección: ocho ventanas completas posteriores cumplieron el objetivo.

El incumplimiento histórico está confirmado, pero también se reconoce la recuperación observada.

### AC-E2-03 — Diccionario AGEB

Archivos: `data/oro/manzanillo_oferta_ageb.csv` y `data/oro/diccionario_datos.csv`.

El agregado AGEB contiene 12 columnas. No se encontraron entradas cuyo campo `dataset` sea `manzanillo_oferta_ageb` en el diccionario.

Resultado: 0 de 12 columnas documentadas específicamente bajo ese identificador.

### AC-E2-04 — Automatización geoespacial

Archivos examinados:

- `pipeline/ejecutar.py`
- `.github/workflows/captura-diaria.yml`
- `.github/workflows/ci.yml`

No se encontraron referencias explícitas a `geoespacial`, `manzanillo_oferta_ageb`, `extraer_ageb` o `agregar_ageb` en esos tres archivos.

Sí existe `pipeline/geoespacial.py`, con funcionalidad para procesar polígonos AGEB y generar el agregado. Por tanto, la observación se limita a la integración automática no identificada en los puntos examinados; no se afirma ausencia de implementación geoespacial.

### Alcance y limitaciones

La revisión reproduce conteos y contrasta documentación con archivos de la versión auditada. No constituye una prueba dinámica integral, una certificación ISO ni una auditoría de seguridad exhaustiva.
