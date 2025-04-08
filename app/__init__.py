from flask import Flask
from .routes import medicine_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(medicine_bp)
    return app
