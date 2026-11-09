# TRUSTED DATA LAB — Observatorio inmobiliario de Colima

Proyecto académico individual para estudiar precios y acceso a la vivienda en Colima.

> Estado inicial: estructura y código base. Los datos históricos descritos en el documento de continuidad todavía deben incorporarse al repositorio; no se incluyen datos inventados.

## Objetivo provisional
Analizar la evolución de los precios de vivienda y su relación con indicadores de oferta habitacional en Colima, usando fuentes oficiales SHF y SNIIV.

## Estructura
- `extractores/`: acceso a fuentes.
- `data/bronce/`: respuestas originales y metadatos de captura.
- `data/plata/`, `data/oro/`: reservadas para etapas de limpieza e integración.
- `data/cuarentena/`: registros rechazados.
- `docs/E0/`: propuesta y ficha de entrega.
- `calidad/`: registros PSP individuales.
- `.github/workflows/`: captura programada.

## Requisitos
Python 3.11 o superior.

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
pip install -r requirements.txt
python -m extractores.registro_sniiv
```

## Fuentes
1. SNIIV — Registro de Vivienda: https://sniiv.sedatu.gob.mx/
2. SNIIV — Inventario de Vivienda: https://sniiv.sedatu.gob.mx/
3. SHF — Índice de Precios: https://www.gob.mx/shf

Consulta de Registro usada como punto de partida:
`https://sniiv.sedatu.gob.mx/api/CuboAPI/GetRegistro/2010,2026/06/000/anio,mes,estado,municipio,segmento`

## Importante
La captura programada requiere configurar GitHub Actions y comprobar su primera ejecución. Una ejecución diaria futura no equivale a siete días de bitácoras. La entrevista, cliente y registros PSP deben corresponder a actividades reales.
