from fastapi.testclient import TestClient

from main import app


client = TestClient(
    app,
)

def test_read_groups():
    response = client.get('/')
    assert response.status_code == 200
