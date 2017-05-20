"""
This script starts the Flask application
"""
from app import app
from app.views import *
from config import HOST, PORT, DEBUG

if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=DEBUG)
    """Call run method on app object by passing some settings defined in the config file"""
