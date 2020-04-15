from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
SECRET_KEY = "change this to be a more random key"
SQLALCHEMY_DATABASE_URI = "postgresql://postgres:password@localhost/user_profile"
SQLALCHEMY_TRACK_MODIFICATIONS = True # added just to suppress a warning
UPLOAD_FOLDER = './app/static/uploads'


app.config.from_object(__name__)

db = SQLAlchemy(app)

from app import views
