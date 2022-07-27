from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object(os.environ.get('APP_SETTINGS'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['PREFERRED_URL_SCHEME'] = 'http'
# app.config['SECRET_KEY'] = '4372093cd57da6dad99b7314'
db = SQLAlchemy(app)
db.init_app(app)
from flask_migrate import Migrate

from stuff import routes
from stuff.models import Bin
migrate = Migrate(app, db)