import flask
import os 
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
myFlask = flask.Flask(__name__)
myFlask.config.from_mapping(
	SECRET_KEY = 'Showmethemoneybaby',
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'),
	SQLALCHEMY_TRACK_MODIFICATIONS = False
) 
db = SQLAlchemy(myFlask)
from myapp import routes,models