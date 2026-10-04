"""Tests for the /inventory/lookup and /inventory/import routes.

The external_api functions are mocked so no real network is used.
"""
from unittest.mock import patch

import requests


@patch("external_api.lookup_by_name")
def test_lookup_route(mock_lookup, client):
    mock_lookup.return_value = {"product_name": "Milk", "quantity": 1, "price": 0}
    response = client.get("/inventory/lookup?name=milk")
    assert response.status_code == 200
    assert response.get_json()["product_name"] == "Milk"


def test_lookup_route_no_param(client):
    response = client.get("/inventory/lookup")
    assert response.status_code == 400


@patch("external_api.lookup_by_name")
def test_lookup_route_not_found(mock_lookup, client):
    mock_lookup.return_value = None
    response = client.get("/inventory/lookup?name=zzz")
    assert response.status_code == 404


@patch("external_api.lookup_by_name")
def test_lookup_route_api_failure(mock_lookup, client):
    mock_lookup.side_effect = requests.RequestException("down")
    response = client.get("/inventory/lookup?name=milk")
    assert response.status_code == 502


@patch("external_api.lookup_by_name")
def test_import_route(mock_lookup, client):
    mock_lookup.return_value = {"product_name": "Juice", "quantity": 1, "price": 0}
    response = client.post("/inventory/import", json={"name": "juice"})
    assert response.status_code == 201
    assert response.get_json()["product_name"] == "Juice"
    assert len(client.get("/inventory").get_json()) == 3
