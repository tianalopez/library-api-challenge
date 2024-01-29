from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_marshmallow import Marshmallow
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager
from datetime import timedelta

load_dotenv()
# Local imports

# Instantiate app, set attributes
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

#! flask-sqlalchemy setup
db = SQLAlchemy(app)
#! flask-migrate setup
migrate = Migrate(app, db)
#! flask-marshmallow setup
ma = Marshmallow(app)
#! flask-restful setup
api = Api(app)
