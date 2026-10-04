import pytest
import models
from app import create_app

@pytest.fixture(autouse=True)
def reset_data():
    models.reset_inventory()
    yield
    models.reset_inventory()

@pytest.fixture()
def client():
    app = create_app()
    app.config['TESTING'] = True
    return app.test_client()
