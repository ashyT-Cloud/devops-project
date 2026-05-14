import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_hello_endpoint(client):
    res = client.get("/")
    assert res.status_code == 200
    data = res.get_json()
    assert data["message"] == "Hello DevOps!"
    assert "version" in data

def test_health_endpoint(client):
    res = client.get("/health")
    assert res.status_code == 200
    assert res._get_json()["status"] == "ok"

def test_health_returns_json(client):
    res = client.get("/health")
    assert res.content_type == "application/json"

def test_unknown_route_returns_404(client):
    res = client.get("/doesnotexit")
    assert res.status_code == 400
