"""Unit tests for the OpenFoodFacts helper functions in external_api.py.

The network calls are mocked so the tests never use the real internet.
The lookup/import ROUTE tests live in test_external_routes.py.
"""
from unittest.mock import MagicMock, patch

import external_api


def fake_response(json_data):
    """Build a fake requests response object."""
    response = MagicMock()
    response.json.return_value = json_data
    response.raise_for_status.return_value = None
    return response


@patch("external_api.requests.get")
def test_lookup_barcode_success(mock_get):
    mock_get.return_value = fake_response(
        {"status": 1, "product": {"product_name": "Milk"}}
    )
    product = external_api.lookup_by_barcode("123")
    assert product["product_name"] == "Milk"
    assert product["quantity"] == 1
    assert product["price"] == 0


@patch("external_api.requests.get")
def test_lookup_barcode_not_found(mock_get):
    mock_get.return_value = fake_response({"status": 0})
    assert external_api.lookup_by_barcode("000") is None


@patch("external_api.requests.get")
def test_lookup_name_success(mock_get):
    mock_get.return_value = fake_response(
        {"products": [{"product_name": "Bread"}]}
    )
    product = external_api.lookup_by_name("bread")
    assert product["product_name"] == "Bread"


@patch("external_api.requests.get")
def test_lookup_name_not_found(mock_get):
    mock_get.return_value = fake_response({"products": []})
    assert external_api.lookup_by_name("zzz") is None
