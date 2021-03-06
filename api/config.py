"""
This script defines some variables for our RestAPI
that are respective to the development and production environments
"""

import os

env = os.environ.get('AIRBNB_ENV')

if env == 'development':
    DEBUG = True
    HOST = 'localhost'
    PORT = 3333
    DATABASE = { 'host': '158.69.84.193',
                 'user': 'airbnb_user_dev',
                 'database': 'airbnb_dev',
                 'port': 3306,
                 'charset': 'utf8',
                 'password': os.environ.get('AIRBNB_DATABASE_PWD_DEV') }

elif env == 'production':
    DEBUG = False
    HOST = '0.0.0.0'
    PORT = 3000
    DATABASE = { 'host': '158.69.84.193',
                 'user': 'airbnb_user_prod',
                 'database': 'airbnb_prod',
                 'port': 3306,
                 'charset': 'utf8',
                 'password': os.environ.get('AIRBNB_DATABASE_PWD_PROD') }

elif env == "test":
    DEBUG = False
    HOST = 'localhost'
    PORT = 5555
    DATABASE = { 'host': '158.69.84.193',
                 'user': 'airbnb_user_test',
                 'database': 'airbnb_test',
                 'port': 3306,
                 'charset': 'utf8',
                 'password': os.environ.get('AIRBNB_DATABASE_PWD_TEST') }
