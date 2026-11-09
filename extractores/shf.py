"""Descarga un recurso estructurado de SHF cuando se configure su URL oficial."""
from datetime import datetime, timezone
from pathlib import Path
import os, json, requests

OUT = Path("data/bronce/shf")
UA = "TDL-Observatorio-Colima/1.0 (proyecto academico; contacto: completar-correo)"

def main():
    url = os.getenv("SHF_DATOS_URL")
    if not url:
        raise SystemExit("Falta SHF_DATOS_URL. Copia la URL del archivo 'datos abiertos' de SHF.")
    OUT.mkdir(parents=True, exist_ok=True)
    r = requests.get(url, headers={"User-Agent": UA}, timeout=120)
    r.raise_for_status()
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    suffix = ".xlsx" if "spreadsheet" in r.headers.get("Content-Type","") else ".bin"
    path = OUT / f"indice_shf_{stamp}{suffix}"
    path.write_bytes(r.content)
    meta = {"source":"Sociedad Hipotecaria Federal - Índice SHF","url":url,
            "captured_at_utc":stamp,"http_status":r.status_code,
            "content_type":r.headers.get("Content-Type"),"bytes":len(r.content)}
    (OUT / f"indice_shf_{stamp}.metadata.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Guardado: {path}")
if __name__ == "__main__":
    main()
