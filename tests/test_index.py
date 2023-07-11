from starlette.testclient import TestClient

from main import app

client = TestClient(app)


def test():
    assert True


def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert type(response.json()) == dict
    assert response.json()["message"] == "Hello World"
