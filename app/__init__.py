import os
from flask import Flask
from flask_jwt import JWT
from app.db import init_db
from app.config import config

def create_app():
    app = Flask(__name__)
    init_db()
    from app.api import api as api_blueprint
    app.register_blueprint(api_blueprint)
    
    return app