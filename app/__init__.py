import os
from flask import Flask
from config import Config

app = Flask(__name__)
# app.config.from_object(Config)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'secret-key!'

from app import routes
