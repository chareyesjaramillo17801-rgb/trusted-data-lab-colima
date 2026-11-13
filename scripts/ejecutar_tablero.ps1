$ErrorActionPreference = 'Stop'
Set-Location (Split-Path -Parent $PSScriptRoot)
python -m pip install -r requirements-dashboard.txt
if ($LASTEXITCODE -ne 0) { throw 'No se pudieron instalar las dependencias' }
python -m pipeline.ejecutar
if ($LASTEXITCODE -ne 0) { throw 'Falló pipeline.ejecutar' }
python -m pipeline.estadistica
if ($LASTEXITCODE -ne 0) { throw 'Falló pipeline.estadistica' }
python -m pipeline.analisis_e1
if ($LASTEXITCODE -ne 0) { throw 'Falló pipeline.analisis_e1' }
python -m streamlit run dashboard/app.py
