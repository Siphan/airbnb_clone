"""
    This script initializes our Flask application by creating
    an instance of the Flask class that will be our WSGI application.
"""
from flask import Flask
from flask_json import FlaskJSON
import os

app = Flask(__name__)
json = FlaskJSON(app)

from views import *
