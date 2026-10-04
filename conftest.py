"""Shared pytest fixtures for all tests.

Provides a Flask test client and resets the in-memory inventory before
every test so each test starts from the same data.
"""
import pytest

import models
from app import create_app


@pytest.fixture(autouse=True)
def reset_data():
    """Reset the inventory before and after each test."""
    models.reset_inventory()
    yield
    models.reset_inventory()


@pytest.fixture()
def client():
    """Return a Flask test client."""
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()
