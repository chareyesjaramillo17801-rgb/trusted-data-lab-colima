# Relatoría de actividades — Entrega E0
**Proyecto:** TRUSTED DATA LAB — Observatorio inmobiliario de Colima  
**Responsable:** Trabajo individual  
**Fecha de consolidación:** 9 de noviembre de 2026

## 1. Objetivo del trabajo

Desarrollar la primera etapa de un observatorio inmobiliario para el estado de Colima, mediante la identificación de fuentes de información oficiales, la construcción de extractores de datos, la validación de su calidad y la documentación del planteamiento del proyecto.

## 2. Actividades realizadas

### 2.1. Configuración del proyecto

- Se creó el repositorio de GitHub `trusted-data-lab-colima`.
- Se organizó la estructura inicial de carpetas para separar documentación, extractores y datos.
- Se configuró el control de versiones mediante Git y GitHub.

### 2.2. Integración de la fuente SNIIV

- Se identificó la API del Sistema Nacional de Información e Indicadores de Vivienda (SNIIV).
- Se desarrolló un extractor para obtener los registros de vivienda.
- Se almacenaron las respuestas originales en la zona Bronce.
- Se implementó una validación para revisar registros faltantes, duplicados, municipios y periodos disponibles.

**Resultado:** Se obtuvieron 2,140 registros, correspondientes a ocho municipios de Colima y 200 periodos año-mes únicos. La información disponible comprende de 2010 a 2026, con ocho meses registrados para 2026.

### 2.3. Integración de la fuente SHF

- Se incorporó el archivo oficial de datos abiertos del Índice SHF de Precios de la Vivienda.
- Se desarrolló un procedimiento de validación para revisar duplicados, cobertura y disponibilidad de información.
- Se analizó la cobertura correspondiente al estado de Colima.

**Resultado:** Se identificaron 258 registros de Colima, distribuidos entre Manzanillo y Villa de Álvarez, con 86 periodos trimestrales por municipio, desde 2005 hasta el segundo trimestre de 2026.

### 2.4. Automatización

- Se configuró GitHub Actions para ejecutar automáticamente el extractor de registros SNIIV.
- Se verificó una ejecución satisfactoria del flujo de trabajo.
- Se dejaron pasos opcionales para otras fuentes, sujetos a la configuración de sus variables.

La captura automática de SHF todavía no está implementada; su archivo fue incorporado manualmente.

### 2.5. Documentación y planteamiento

Se elaboraron y actualizaron los documentos relacionados con:

- Planteamiento del observatorio.
- Identificación de clientes y usuarios potenciales.
- Preguntas analíticas para las siguientes etapas.
- Objetivos de calidad.
- Ética y legalidad de las fuentes.
- Validación de los datos SNIIV y SHF.
- Ficha de entrega E0.

Se decidió trabajar con dos enfoques complementarios: el análisis general del mercado inmobiliario de Colima y una línea específica sobre las necesidades de vivienda en renta para estudiantes.

### 2.6. Entrevista exploratoria

Se realizó una entrevista escrita a una persona que busca vivienda en Tecomán, Colima. La conversación duró aproximadamente 15 minutos e incluyó ocho preguntas.

Entre los principales hallazgos se identificaron dificultades para encontrar información confiable y actualizada sobre precios y características de las viviendas, así como publicaciones que permanecen disponibles aunque el inmueble ya esté ocupado o no exista una intención real de rentarlo.

La persona entrevistada manifestó que utilizaría una herramienta de consulta inmobiliaria si fuera segura y se mantuviera actualizada.

La entrevista constituye una exploración de las necesidades de los usuarios; no representa una validación comercial con agentes o agencias inmobiliarias.

## 3. Problemas encontrados y correcciones

Durante el desarrollo se identificaron dos defectos principales:

- **D-01:** Las reglas iniciales de `.gitignore` impedían incorporar los archivos de la zona Bronce. Se modificaron las reglas para permitir su seguimiento.
- **D-02:** El validador SNIIV seleccionaba archivos auxiliares en lugar del archivo JSON de registros. Se corrigió la selección del archivo de entrada.

Ambos defectos fueron corregidos y documentados en el registro PSP.

## 4. Resultados obtenidos

- Repositorio de GitHub creado y organizado.
- Dos fuentes oficiales incorporadas al proyecto.
- Extractor SNIIV funcional.
- Datos SHF incorporados y validados.
- Automatización de la captura SNIIV mediante GitHub Actions.
- Series históricas superiores a 36 periodos.
- Documentación de planteamiento, entrevista, ética, calidad y validaciones.
- Registros iniciales de tiempo y defectos en los datasets PSP.

## 5. Limitaciones y actividades pendientes

- Incorporar y validar la fuente SNIIV Inventario.
- Automatizar la captura de SHF.
- Implementar las zonas Plata, Oro y Cuarentena.
- Evaluar la comparabilidad entre las fuentes para el análisis multivariado.
- Realizar una validación comercial con agentes, asesores o agencias inmobiliarias.
- Confirmar con el docente la aceptación de la entrevista escrita.
- Medir los objetivos de calidad durante el periodo establecido.
- Verificar la trazabilidad completa de los archivos crudos.
- Desarrollar los análisis correspondientes a E1, E2 y E3.

## 6. Conclusión

La etapa E0 permitió establecer la base documental y técnica del Observatorio Inmobiliario de Colima. Se integraron dos fuentes oficiales, se obtuvieron series históricas, se desarrollaron mecanismos iniciales de validación y se automatizó la captura de una de las fuentes.

Los resultados permiten continuar con el desarrollo del proyecto, aunque todavía existen actividades pendientes relacionadas con la automatización, la arquitectura de datos, la validación comercial y la evaluación de calidad.
