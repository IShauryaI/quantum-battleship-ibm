from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

def create_app():
    load_dotenv()

    app = Flask(__name__)
    CORS(app)  # Allow React frontend to call Flask API

    # Load config
    app.config.from_object("config.Config")

    # Register routes
    from .routes import main
    app.register_blueprint(main)

    return app

