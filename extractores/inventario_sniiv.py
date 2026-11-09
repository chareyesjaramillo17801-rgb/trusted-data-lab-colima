"""Descarga un CSV oficial del Inventario SNIIV cuando se configure su URL directa.

No adivina endpoints. La URL debe copiarse desde el recurso oficial del portal SNIIV.
Configurar INVENTARIO_SNIIV_URL como variable de entorno/secret de GitHub.
"""
from datetime import datetime, timezone
from pathlib import Path
import os, json, requests

OUT = Path("data/bronce/sniiv_inventario")
UA = "TDL-Observatorio-Colima/1.0 (proyecto academico; contacto: completar-correo)"

def main():
    url = os.getenv("INVENTARIO_SNIIV_URL")
    if not url:
        raise SystemExit("Falta INVENTARIO_SNIIV_URL. Configura la URL de descarga oficial; no se inventará.")
    OUT.mkdir(parents=True, exist_ok=True)
    r = requests.get(url, headers={"User-Agent": UA}, timeout=120)
    r.raise_for_status()
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    path = OUT / f"inventario_{stamp}.csv"
    path.write_bytes(r.content)
    meta = {"source":"SNIIV Inventario de Vivienda","url":url,"captured_at_utc":stamp,
            "http_status":r.status_code,"bytes":len(r.content)}
    (OUT / f"inventario_{stamp}.metadata.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Guardado: {path} ({len(r.content)} bytes)")

if __name__ == "__main__":
    main()
