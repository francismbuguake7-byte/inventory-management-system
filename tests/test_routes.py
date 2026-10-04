"""Tests for the main CRUD routes (GET, POST, PATCH, DELETE).

Input-validation error cases live in test_validation.py.
"""


def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "running" in response.get_json()["message"]


def test_get_all(client):
    response = client.get("/inventory")
    assert response.status_code == 200
    assert len(response.get_json()) == 2


def test_get_one(client):
    response = client.get("/inventory/1")
    assert response.status_code == 200
    assert response.get_json()["product_name"] == "Milk"


def test_get_one_not_found(client):
    response = client.get("/inventory/999")
    assert response.status_code == 404
    assert response.get_json()["error"] == "Item not found"


def test_create_item(client):
    data = {"product_name": "Eggs", "quantity": 12, "price": 60.0}
    response = client.post("/inventory", json=data)
    assert response.status_code == 201
    assert response.get_json()["product_name"] == "Eggs"


def test_update_item(client):
    response = client.patch("/inventory/1", json={"quantity": 99})
    assert response.status_code == 200
    assert response.get_json()["quantity"] == 99


def test_update_not_found(client):
    response = client.patch("/inventory/999", json={"quantity": 1})
    assert response.status_code == 404


def test_update_empty(client):
    response = client.patch("/inventory/1", json={})
    assert response.status_code == 400
    assert response.get_json()["error"] == "Empty update request"


def test_delete_item(client):
    response = client.delete("/inventory/1")
    assert response.status_code == 200
    assert client.get("/inventory/1").status_code == 404


def test_delete_not_found(client):
    response = client.delete("/inventory/999")
    assert response.status_code == 404
