"""
This script starts the Flask application
"""
from flask import Flask
from flask_json import FlaskJSON
import app
from config import *
from app import app
from app.views import *

if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=DEBUG)
    """Call run method on app object by passing some settings defined in the config file"""
