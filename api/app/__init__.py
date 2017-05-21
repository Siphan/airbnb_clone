"""
 This script creates a Flask application
 and makes it global to our Python app.
 It also adds a MySQL instance to our code.
"""
from flask import Flask
from flask_json import FlaskJSON
import config
from flask_mysqldb import MySQL

__all__ = ["config"]

"""
Initialize Flask application
An instance of this class will be our WSGI application.
"""
app = Flask(__name__)
mysql = MySQL(app)

# Initialize FlaskJSON instance with Flask app
FlaskJSON(app)

"""Import all views"""
from views import *
