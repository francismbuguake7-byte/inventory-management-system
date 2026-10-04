from flask import Flask
from routes import crud
from external_routes import helper

def create_app():
    app = Flask(__name__)
    app.register_blueprint(crud)
    app.register_blueprint(helper)
    return app
app = create_app()
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
