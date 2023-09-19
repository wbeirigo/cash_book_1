import pytest
from starlette.testclient import TestClient
from ..main import app

def test_post():
    client = TestClient(app)
    payload = {
                "titulo": "tssseste001",
                "lancamento_dt": "2023-09-19T16:23:48.730Z",
                "valor": 32,
                "status": "Crédito"
                }
    response = client.post("/api/cashbook", json=payload)
    assert response.status_code == 201

    chave = response.json()['id']
    client.delete(f"/api/cashbook/{chave}")    


def test_post_values():
    client = TestClient(app)
    payload = {
                "titulo": "tssseste001",
                "lancamento_dt": "2023-09-19T16:23:48.730Z",
                "valor": 32,
                "status": "Crédito"
                }
    response = client.post("/api/cashbook", json=payload)
    assert response.status_code == 201

    assert response.json()['titulo'] == payload['titulo']
    assert response.json()['valor'] == payload['valor']
    assert response.json()['status'] == payload['status']


    chave = response.json()['id']
    client.delete(f"/api/cashbook/{chave}")    


def test_post_empty_title_values():
    client = TestClient(app)
    payload = {
                "titulo": "",
                "lancamento_dt": "2023-09-19T16:23:48.730Z",
                "valor": 32,
                "status": "Crédito"
                }
    response = client.post("/api/cashbook", json=payload)
    assert response.status_code == 422


def test_post_empty_value_values():
    client = TestClient(app)
    payload = {
                "titulo": "reewrewr",
                "lancamento_dt": "2023-09-19T16:23:48.730Z",
                "valor": 0,
                "status": "Crédito"
                }
    response = client.post("/api/cashbook", json=payload)
    assert response.status_code == 422


def test_post_empty_status_values():
    client = TestClient(app)
    payload = {
                "titulo": "reewrewr",
                "lancamento_dt": "2023-09-19T16:23:48.730Z",
                "valor": 333,
                "status": ""
                }
    response = client.post("/api/cashbook", json=payload)
    assert response.status_code == 422


def test_post_wrong_date_values():
    client = TestClient(app)
    payload = {
                "titulo": "reewrewr",
                "lancamento_dt": "03-12-2023T16:23:48.730Z",
                "valor": 333,
                "status": "Crédito"
                }
    response = client.post("/api/cashbook", json=payload)
    assert response.status_code == 422




def test_get_values():
    client = TestClient(app)
    payload = {
                "titulo": "tssseste001",
                "lancamento_dt": "2023-09-19T16:23:48.730Z",
                "valor": 32,
                "status": "Crédito"
                }
    response = client.post("/api/cashbook", json=payload)
    
    chave = response.json()['id']
    response = client.get(f"/api/cashbook/{chave}")
    assert response.json()['titulo'] == payload['titulo']
    assert response.json()['valor'] == payload['valor']
    assert response.json()['status'] == payload['status']
    assert response.status_code == 200

    chave = response.json()['id']
    client.delete(f"/api/cashbook/{chave}")  

def test_put_values():
    client = TestClient(app)
    payload = {
                "titulo": "tssseste001",
                "lancamento_dt": "2023-09-19T16:23:48.730Z",
                "valor": 32,
                "status": "Crédito"
                }
    response = client.post("/api/cashbook", json=payload)
    
    chave = response.json()['id']
    payload['status'] = "Debito"
    response = client.put(f"/api/cashbook/{chave}", json=payload)
    assert response.json()['titulo'] == payload['titulo']
    assert response.json()['valor'] == payload['valor']
    assert response.json()['status'] == payload['status']
    assert response.status_code == 200

    client.delete(f"/api/cashbook/{chave}")  


def test_delete_values():
    client = TestClient(app)
    payload = {
                "titulo": "tssseste001",
                "lancamento_dt": "2023-09-19T16:23:48.730Z",
                "valor": 32,
                "status": "Crédito"
                }
    response = client.post("/api/cashbook", json=payload)
    
    chave = response.json()['id']
    response = client.delete(f"/api/cashbook/{chave}")  
    assert response.status_code == 204