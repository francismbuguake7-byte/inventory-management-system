"""Main Flask application for the Inventory Management System.

Run this file to start the API server:

    python app.py

The API will be available at http://127.0.0.1:5000
"""
from flask import Flask

from routes import crud
from external_routes import helper


def create_app():
    """Create the Flask app and register the route blueprints."""
    app = Flask(__name__)
    app.register_blueprint(crud)
    app.register_blueprint(helper)
    return app


app = create_app()


if __name__ == "__main__":
    # Debug mode gives helpful error messages while learning.
    app.run(host="127.0.0.1", port=5000, debug=True)
