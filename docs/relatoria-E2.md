# Relatoría E2 — TRUSTED DATA LAB

**Proyecto:** Observatorio inmobiliario de Colima. **Modalidad:** individual. **Corte:** 22/11/2026. **Estado:** trabajo interno publicado; auditoría cruzada pendiente.

## 1. Objetivo

Integrar cartografía oficial de INEGI al observatorio, documentar linaje Bronce–Plata–Oro, realizar experimentos factoriales reproducibles sobre procesamiento local y evaluar calidad de software y datos mediante ISO/IEC 25010 y 25012.

## 2. Cronología y tiempo

- **09/11:** incorporación de SHF según metadatos de Bronce; no consta hora exacta de descarga.
- **13/11:** antecedentes E1: limpieza, modelos y validaciones.
- **22/11, 14:36 (-0600):** commit geoespacial E2 `1bdd739`; después, cruce `gpd.sjoin()` con 10/10 coincidencias, documentación y commit `435c0c4`. Se publicó el tag `e2` sobre `435c0c4`.
- **22/11:** experimentos factoriales y confirmación locales; se publicaron 25 archivos de Estadística en `114fddc`. Se eliminó posteriormente el ZIP redundante de resultados, manteniendo los archivos individuales.
- **22/11:** evaluación de siete productos Oro, revisión de métricas, informe ISO y publicación en `5b83f12`. Se comunicaron 12 pruebas Pytest aprobadas y Ruff sin errores en las rutas revisadas.

**Tiempo:** `calidad/tiempo-individual.csv` contiene 8.25 h retrospectivas de E0; no hay cronometraje verificable de E2. No se asignan horas inventadas.

## 3. Decisiones y alternativas

Se eligió cartografía municipal oficial INEGI y OpenStreetMap frente a coordenadas inmobiliarias no verificadas y capas que requieren clave. La unión espacial relaciona puntos representativos derivados de los propios polígonos: valida geometría, **no** localiza viviendas. Para Estadística se midió el procesamiento de datos SNIIV en copias locales, evitando sobrecargar APIs; el diseño fraccionado seleccionó observaciones del 2⁴ completo, no constituyó una ejecución independiente. Se conservaron los resultados originales al corregir estilo de código.

## 4. Resultados y defectos

**Ingeniería de Datos:** 10 municipios verificados; linaje documentado para SNIIV, SHF y productos analíticos. Limitación: la fecha de modificación del Excel SHF no verifica la captura exacta.

**Estadística:** 90 corridas principales, 24 observaciones de fracción y 10 de confirmación; mejora media reportada de 47.73 % en tiempo local (248.95 frente a 130.14 ms). En el diseño 3×2 y el fraccionado, las pruebas Shapiro mostraron p≈0.0423 y p≈0.0214: se documentaron reservas sobre normalidad y alias `I=ABCD`.

**Calidad:** siete productos Oro evaluados, cero filas completamente duplicadas y cuatro con completitud total. Se identificaron **hallazgos por investigar**, no defectos confirmados automáticamente: nulos de SHF, campos de resultados analíticos y trazabilidad de comparación municipal. Se elaboró plantilla de auditoría cruzada; no se atribuyen hallazgos a otro equipo sin revisar su repositorio.

**Incidencias de desarrollo:** se documentaron ajustes de GeoJSON, capa cartográfica, selección municipal y linaje. Las bitácoras anteriores no contienen fechas/IDs completos para cada incidencia E2; no se reconstruyen ficticiamente.

## 5. Aprendizajes, límites y evidencias

El origen, hash y granularidad importan tanto como la presencia de datos; una mejora de rendimiento requiere experimentación y diagnóstico de supuestos; aprobar pruebas de software no equivale a certificación ISO ni a auditoría externa. La auditoría cruzada bidireccional sigue pendiente del acceso al proyecto asignado. El tag `e2` existe, pero precede a los commits de Estadística y Calidad y deberá revisarse al cerrar la versión final.

**Evidencias:** [ficha E2](E2/ENTREGA.md), [linaje](E2/LINAJE.md), [Estadística](E2/estadistica/INFORME_ESTADISTICA_E2.md), [Calidad](E2/calidad/INFORME_CALIDAD_E2.md), [resultados estadísticos](../resultados/estadistica_e2/), [métricas de Calidad](../resultados/calidad_e2/), [auditoría pendiente](E2/calidad/PLANTILLA_AUDITORIA_CRUZADA.md).

**Uso de IA:** se utilizó ChatGPT para apoyo en planificación, código, revisión y redacción. Las ejecuciones locales, resultados y decisiones se contrastaron con salidas de PowerShell y archivos del proyecto; no se fabricaron auditorías externas ni tiempos de trabajo.
