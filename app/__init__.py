from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
SECRET_KEY = "change this to be a more random key"
SQLALCHEMY_DATABASE_URI = "postgresql://uniejdwejpajrc:2c62823acbe7ffa053b0488996592b3498be54505159bc74bfd6142c8bcad636@ec2-18-206-84-251.compute-1.amazonaws.com:5432/d2rhu69ms8mi14"
SQLALCHEMY_TRACK_MODIFICATIONS = True # added just to suppress a warning
UPLOAD_FOLDER = './app/static/uploads'


app.config.from_object(__name__)

db = SQLAlchemy(app)

from app import views
