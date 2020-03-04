import os
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
# app.config.from_object(Config)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'secret-key!'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY__DATABASE_URI') or 'sqlite:///{}'.format(os.path.join(basedir, 'app.db'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models
