"""
This module allows only GET requests to be called on our API.
Response returns UTC time and local time of server.
HTTP response code 404 is handled.
"""

from flask_json import FlaskJSON, json_response
from datetime import datetime, tzinfo
from pytz import utc, timezone
from app import app, models
from peewee import *

local_tz = timezone('America/Los_Angeles')

@app.route('/', methods=['GET'])
def index():
    """
    Function to manage the API route /
    allowing only GET request
    response will be a JSON
    return a hash with keys/values:
    status 'OK', utc_time and time
    """
    return json_response(status="OK", utc_time=datetime.utcnow().strftime('%m/%d/%Y %H:%M:%S'), time=utc_to_local(datetime.utcnow()).strftime('%m/%d/%Y %H:%M:%S')) #format 2nd arg into UTC


@app.route('/')
def users():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT user, host FROM mysql.user''')
    rv = cur.fetchall()
    return str(rv)


@app.errorhandler(404)
def not_found(e):
    """Function to manage all not found routes"""
    return json_response(add_status_=False, code=404, msg="not found")

def utc_to_local(utc_dt):
    """Function to convert UTC to local server time"""
    local_dt = utc_dt.replace(tzinfo=utc).astimezone(local_tz)
    return local_tz.normalize(local_dt)

def before_request():
    """Function to open a database connection before each request"""
    models.database.connect()

def after_request():
    """Function to close a database connection after each request"""
    models.database.close()
