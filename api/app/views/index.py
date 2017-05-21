'''Defines the flask function to run when a GET request is made to the root
directory '/'. Handles the behavior for a 404 error.
'''
from flask import Flask, jsonify, request
from flask_json import FlaskJSON, JsonError, json_response, as_json
from app import app
import datetime
import time
from app.models.base import *
from peewee import *


@app.route('/', methods=['GET'])
@as_json
def index():
    """
    Root of the AirBnB API
    This endpoint return API status and server times (local and UTC)
    ---
    tags:
      - Index
    responses:
      200:
        description: Status and server times
        schema:
          id: return_index
          properties:
            status:
              type: string
              description: API Status
              default: 'OK'
            time:
              type: datetime
              description: server time
              default: '20/07/2016 15:47:29'
            utc_time:
              type: datetime
              description: server time in UTC
              default: '20/07/2016 22:47:29'
    """
    return jsonify(status="OK",
                   utc_time=datetime.datetime
                                    .utcnow()
                                    .strftime("%Y/%m/%d %H:%M:%S"),
                   time=datetime.datetime
                                .now()
                                .strftime("%Y/%m/%d %H:%M:%S"))

@app.before_request
def before_request():
    '''Connect to the database defined in BaseModel.'''
    BaseModel.database.connect()

@app.after_request
def after_request():
    '''Close the connection to the database defined in the BaseModel.'''
    BaseModel.database.close()
    return response


@app.errorhandler(404)
def page_not_found(error):
    '''Return a JSON object with the code 404, and a message "not found".'''
    return jsonify(code=404,
                   msg="not found")
