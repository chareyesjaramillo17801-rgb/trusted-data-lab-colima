# Objetivos de calidad — E0

## 1. Éxito de captura

**Objetivo:** Mantener al menos un 95 % de ejecuciones programadas exitosas durante un periodo de 14 días.

- **Métrica:** (Ejecuciones exitosas / ejecuciones programadas) × 100.
- **Fuente de evidencia:** Historial de ejecuciones de GitHub Actions.
- **Estado:** Pendiente de medición durante 14 días.

## 2. Completitud de datos

**Objetivo:** Alcanzar al menos un 98 % de registros con periodo, municipio y variable de conteo no nulos en la zona Plata.

- **Métrica:** (Registros completos / total de registros evaluados) × 100.
- **Fuente de evidencia:** Validaciones de calidad de la zona Plata.
- **Estado:** Pendiente. La zona Plata todavía no está implementada.

## 3. Trazabilidad de datos

**Objetivo:** Contar con metadatos de procedencia para el 100 % de los archivos crudos incorporados en la zona Bronce.

- **Métrica:** (Archivos crudos con metadatos completos / total de archivos crudos) × 100.
- **Campos mínimos:** Fuente, URL de procedencia y fecha de captura o incorporación.
- **Fuente de evidencia:** Archivos de metadatos JSON en la zona Bronce.
- **Estado:** Parcialmente verificado. Se revisaron dos metadatos SNIIV y se incorporó un archivo de metadatos para SHF. Falta auditar el resto de las capturas.

## 4. Observaciones

Los objetivos anteriores son metas de calidad propuestas para el proyecto. No deben presentarse como resultados alcanzados hasta contar con las mediciones correspondientes.

Las fechas de incorporación no deben confundirse con fechas u horas exactas de descarga. Las estimaciones retrospectivas de tiempo del PSP tampoco deben confundirse con mediciones cronometradas.
