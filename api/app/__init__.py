from flask import Flask
from flask_json import FlaskJSON
import os

app = Flask(__name__)
json = FlaskJSON(app)

from views import *
