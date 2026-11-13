# E1 — Seguridad y confiabilidad: evidencia y límites

## Captura de fuentes (captura de pantalla del historial de Actions)

**Actualización al 13 de noviembre de 2026.** El historial de GitHub Actions «Captura de fuentes» presenta 14 ejecuciones: 12 exitosas y 2 fallidas.

La tasa de éxito por ejecución es:

**12 / 14 × 100 = 85.71 %.**

El resultado permanece por debajo del objetivo de confiabilidad del 95 % definido en E0. Las dos fallas históricas corresponden a los defectos DEF-001 y DEF-002, documentados previamente.

La tasa de éxito por ejecución no equivale a disponibilidad temporal. No se dispone de evidencia suficiente para calcular MTBF, MTTR o disponibilidad temporal verificables. No se atribuyen valores estimados a estas métricas.

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

### Auditoría de secretos — Gitleaks

**Fecha:** 13 de noviembre de 2026.

**Herramienta:** Gitleaks, ejecutado mediante Docker.

**Comando utilizado:**
`docker run --rm -v "${PWD}:/repo" ghcr.io/gitleaks/gitleaks:latest git /repo --redact --verbose`

**Resultados:**
- Commits analizados: 61.
- Volumen examinado: aproximadamente 6.05 MB.
- Duración del escaneo: 2.01 segundos.
- Secretos detectados: 0.
- Mensaje final: `no leaks found`.

**Conclusión:** No se identificaron posibles secretos mediante las reglas de Gitleaks en el historial examinado. El resultado constituye evidencia de la revisión de seguridad, sin garantizar que no existan otros riesgos.
## Respaldo y restauracion de Bronce

Fecha: 13 de noviembre de 2026.

Archivo: trusted-data-lab-backup-20261113_155739.zip

Ubicacion: directorio personal del usuario, fuera del repositorio.

Metodo: Compress-Archive y Expand-Archive de PowerShell.

Verificacion:
- Archivos originales: 30.
- Archivos restaurados: 30.
- Comparacion SHA-256 por archivo: sin diferencias.
- Resultado: RESTAURACION VERIFICADA.

El respaldo se conserva separado del repositorio.
