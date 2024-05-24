import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_valid_payload():
    payload = {
        "batchid": "id0101",
        "payload": [[1, 2], [3, 4]]
    }
    response = client.post("/addition/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["batchid"] == "id0101"
    assert data["status"] == "complete"
    assert len(data["response"]) == 2
    assert data["response"][0] == 3
    assert data["response"][1] == 7


def test_invalid_payload():
    payload = {
        "batchid": "id0101",
        "payload": [[1, 2], ["a", "b"]]  # Invalid payload with non-integer values
    }
    response = client.post("/addition/", json=payload)
    assert response.status_code == 422  # Expecting 422 Unprocessable Entity


def test_empty_payload():
    payload = {
        "batchid": "id0101",
        "payload": []  # Empty payload
    }
    response = client.post("/addition/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["batchid"] == "id0101"
    assert data["status"] == "complete"
    assert len(data["response"]) == 0  # Expecting an empty response


def test_error_handling():
    payload = {
        "batchid": "id0101",
        "payload": [[1, 2], [3, 4]]
    }
    # Intentionally cause an error by providing incorrect data type to sum function
    with pytest.raises(TypeError):
        response = client.post("/addition/", json=payload)
