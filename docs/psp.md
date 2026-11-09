# PSP – Proceso Personal de Software
## TRUSTED DATA LAB – Entrega E0

### 1. Objetivo

Registrar el tiempo dedicado al desarrollo de E0, los defectos encontrados, las acciones correctivas y las observaciones del proceso de trabajo.

### 2. Registro de tiempo

Los tiempos son estimaciones retrospectivas acordadas a partir del trabajo realizado. No fueron medidos con cronómetro.

| Actividad | Tiempo estimado |
|---|---:|
| Configuración de GitHub y estructura del proyecto | 1 hora |
| Desarrollo y corrección del extractor SNIIV | 2 horas |
| Incorporación y validación de SHF | 2 horas |
| Documentación del planteamiento y ficha E0 | 1 hora |
| Configuración de GitHub Actions y automatización | 1 hora |
| Revisión ética y legalidad | 1 hora |
| Entrevista a cliente potencial | 15 minutos |
| **Total** | **8 horas 15 minutos** |

### 3. Registro de defectos

| ID | Defecto identificado | Corrección realizada |
|---|---|---|
| D-01 | La configuración inicial de `.gitignore` impedía incorporar correctamente los archivos de la zona Bronce al repositorio. | Se modificaron las reglas para permitir el seguimiento de `data/bronce` y mantener excluidas las zonas correspondientes a datos procesados. |
| D-02 | El validador de SNIIV seleccionaba incorrectamente archivos auxiliares en lugar de analizar el archivo de registros. | Se corrigió la selección del archivo para analizar los registros JSON correspondientes. |

### 4. Observaciones del proceso

- Se requirieron ajustes en la configuración del repositorio para conservar correctamente los datos originales.
- Fue necesario corregir la selección de archivos durante la validación de SNIIV.
- Se implementaron validaciones para revisar registros faltantes, duplicados y cobertura temporal.
- La incorporación de SHF permitió ampliar el análisis con una segunda fuente de información.
- La entrevista permitió identificar necesidades concretas de personas que buscan vivienda en renta.

### 5. Limitaciones del registro

- Los tiempos se reconstruyeron retrospectivamente y son aproximados.
- No se registraron por separado los tiempos de detección y corrección de cada defecto.
- No se cuenta con una medición formal de productividad ni con una tasa de defectos por hora.
- El registro de defectos incluye los problemas identificados durante el trabajo y documentados en esta bitácora; no representa necesariamente todos los incidentes menores ocurridos.

### 6. Resultado

Se registraron **8 horas con 15 minutos** de trabajo estimado y **2 defectos documentados**, ambos con sus respectivas correcciones.

Este registro constituye la bitácora retrospectiva del proceso de desarrollo de la entrega E0.
