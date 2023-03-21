from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_create_sentiment():
    response = client.post(
        "/sentiments",
        headers={"X-Token": "coneofsilence"},
        json={"inputs": "sample text"},
    )
    print(response)
    assert response.status_code == 200
    assert response.json() == {
        "inputs": "sample text"
    }