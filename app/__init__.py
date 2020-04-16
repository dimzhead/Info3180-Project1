from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
SECRET_KEY = "change this to be a more random key"
DATABASE_URL = "postgresql://mzntyignpahwsm:3d1d7a7b6c001495104f20f59b258c4ee6839880992ab5a23dd48b97188b1f24@ec2-54-197-48-79.compute-1.amazonaws.com:5432/d1f2r4rfpcbufn"
SQLALCHEMY_TRACK_MODIFICATIONS = True # added just to suppress a warning
UPLOAD_FOLDER = './app/static/uploads'


app.config.from_object(__name__)

db = SQLAlchemy(app)

from app import views
