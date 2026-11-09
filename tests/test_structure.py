from pathlib import Path

def test_required_directories_exist():
    for p in ["docs/E0", "extractores", "calidad", "data/bronce",
              "data/plata", "data/oro", "data/cuarentena"]:
        assert Path(p).exists()
