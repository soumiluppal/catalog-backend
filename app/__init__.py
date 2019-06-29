import os
from flask import Flask
from app.config import config
from flask_sqlalchemy import SQLAlchemy
from flask_jwt import JWT
 
flaskapp = Flask(__name__)
flaskapp.config.from_object(config)
print("CHECK ME OUT")
db = SQLAlchemy(flaskapp)
import app.models
db.create_all()
from app.authenticate import authenticate, identity
from app.api import api as api_blueprint
JWT(flaskapp, authenticate, identity)
flaskapp.register_blueprint(api_blueprint)