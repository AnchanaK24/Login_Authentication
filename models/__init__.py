import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()

from models.user import User
from models.user import Session
