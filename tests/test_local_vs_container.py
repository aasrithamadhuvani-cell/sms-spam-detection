from pathlib import Path
def test_dockerfile_exists():
    root=Path(__file__).resolve().parents[1]
    assert (root/"Dockerfile").exists()
    assert (root/"api"/"main.py").exists()
