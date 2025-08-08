from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to WorkSync AI API"}

def test_invalid_route():
    response = client.get("/nonexistent")
    assert response.status_code == 404
