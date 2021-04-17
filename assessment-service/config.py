from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from celery import Celery
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

broker = Celery('tasks', broker='pyamqp://broker//')

db = SQLAlchemy(app)
ma = Marshmallow(app)
