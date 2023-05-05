import os
from dotenv import load_dotenv, find_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(find_dotenv())


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    MONGODB_SETTINGS = {
        # 'db':'ctrlearndb',
        'host': os.environ.get('MONGODB_URI')}
    # CORS_HEADERS = 'Content-Type'

class TestConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    MONGODB_SETTINGS = {
        'db': 'test_database',
        'host': 'mongodb://127.0.0.1:27017/test_database'
    }
    # CORS_HEADERS = 'Content-Type'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = 'example@example.com'
    MAIL_PASSWORD = 'ex_password'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
