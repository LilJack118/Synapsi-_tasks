from fastapi.testclient import TestClient

from api import app

client = TestClient(app)

def test_encoder_1():
    response = client.post(
    "/encode/",
    json={"Content": "Hello World"})

    assert response.status_code == 200
    assert response.json() == {
    "Content": "V1xLFh8TKyQuEUs=",
    }

def test_encoder_2():
    response = client.post(
    "/encode/",
    json={"Content": "FastAPI"})

    assert response.status_code == 200
    assert response.json() == {
    "Content": "CQwRLQ85Hg==",
    }


def test_decoder_1():
    response = client.post(
    "/decode/",
    json={"Content": "V1xLFh8TKyQuEUs="})

    assert response.status_code == 200
    assert response.json() == {
    "Content": "Hello World",
    }

def test_decoder_2():
    response = client.post(
    "/decode/",
    json={"Content": "CQwRLQ85Hg=="})

    assert response.status_code == 200
    assert response.json() == {
    "Content": "FastAPI",
    }
    