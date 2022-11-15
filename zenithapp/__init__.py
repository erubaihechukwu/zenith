from flask import Flask
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_migrate import Migrate

from zenithapp import config
app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
csrf = CSRFProtect(app)
from zenithapp import *
from zenithapp.routes import user_routes,admin_routes

