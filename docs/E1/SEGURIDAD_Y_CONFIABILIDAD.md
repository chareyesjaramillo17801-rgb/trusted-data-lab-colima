# E1 — Seguridad y confiabilidad: evidencia y límites

## Captura de fuentes (captura de pantalla del historial de Actions)

Ventana visible: 9–12 de noviembre de 2026; 13 ejecuciones visibles: 11 exitosas y 2 fallidas. Tasa de éxito por ejecución = 11/13 = **84.62%**, por debajo del objetivo E0 del 95%. Las tres ejecuciones programadas visibles (10, 11 y 12 de noviembre) tuvieron éxito (3/3). La imagen no acredita cobertura del 6 al 8 ni del 13 de noviembre. **No confundir tasa de éxito con disponibilidad temporal.**

## Defectos observados

| ID | Ejecución | Evidencia | Diagnóstico | Estado de verificación |
|---|---|---|---|---|
| DEF-001 | #3, 9 nov., 10:04 | `ValueError: No se encontró una lista de registros en el JSON.` sobre `registro_20261109T160506Z.metadata.json` | Selección de metadatos en lugar del JSON de datos | Hubo ejecuciones posteriores exitosas; confirmar commit de corrección del validador |
| DEF-002 | #6, 9 nov., 10:29 | `NameError: name 'columna_mes' is not defined` | Variable utilizada sin definición previa | Hubo ejecuciones posteriores exitosas; confirmar commit de corrección |

Las duraciones de los workflows (26 s y 23 s para las fallas) **no** son tiempos de reparación. No se dispone de registros de inicio/fin de incidentes para calcular MTTR ni MTBF verificables. La disponibilidad temporal tampoco puede calcularse con precisión a partir de estados de ejecución aislados. No inventar estas métricas.

## Seguridad

- El workflow E1 declara `permissions: contents: read`.
- `pip-audit` ejecutado localmente: `No known vulnerabilities found`; E1 CI verde tras incorporar la comprobación.
- Ruff y pytest ejecutados localmente y en CI: 0 errores de Ruff y 7 pruebas aprobadas.
- **Pendiente de ejecutar y adjuntar evidencia:** gitleaks sobre historial completo, revisión de secretos y política de respaldo/recuperación de Bronce.

## Comandos de evidencia pendientes

```powershell
# Si Docker está instalado, revisar historial sin instalar gitleaks localmente:
docker run --rm -v "${PWD}:/repo" ghcr.io/gitleaks/gitleaks:latest git /repo --redact --verbose
# Guardar el resultado y registrar la versión y fecha. No publicar secretos detectados.
```

Si Docker no está disponible, instalar gitleaks desde su distribución oficial y ejecutar `gitleaks git . --redact --verbose`. Revisar la versión y sintaxis instalada. No declarar el escaneo completado antes de ejecutarlo.
