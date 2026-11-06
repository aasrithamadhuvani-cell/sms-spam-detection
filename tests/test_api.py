from fastapi.testclient import TestClient
from api.main import app
def test_root():
    with TestClient(app) as client:
        r=client.get("/")
        assert r.status_code==200
        assert r.json()["status"]=="success"
def test_health():
    with TestClient(app) as client:
        r=client.get("/health")
        assert r.status_code==200
