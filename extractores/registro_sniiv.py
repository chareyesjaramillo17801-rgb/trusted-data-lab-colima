"""Descarga el cubo de Registro de Vivienda de SNIIV y conserva la respuesta cruda."""
from datetime import datetime, timezone
from pathlib import Path
import json
import requests

URL = ("https://sniiv.sedatu.gob.mx/api/CuboAPI/GetRegistro/"
       "2010,2026/06/000/anio,mes,estado,municipio,segmento")
OUT = Path("data/bronce/sniiv_registro")
UA = "TDL-Observatorio-Colima/1.0 (proyecto academico; contacto: completar-correo)"

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    r = requests.get(URL, headers={"User-Agent": UA}, timeout=60)
    r.raise_for_status()
    payload = r.json()
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    data_path = OUT / f"registro_{stamp}.json"
    meta_path = OUT / f"registro_{stamp}.metadata.json"
    data_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    meta = {
        "source": "SNIIV Registro de Vivienda",
        "url": URL,
        "captured_at_utc": stamp,
        "http_status": r.status_code,
        "content_type": r.headers.get("Content-Type"),
        "records": len(payload) if isinstance(payload, list) else None,
        "note": "Respuesta cruda; validar estructura y cobertura antes de analizar."
    }
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Guardado: {data_path}; registros: {meta['records']}")

if __name__ == "__main__":
    main()
