import os
from dotenv import load_dotenv, find_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(find_dotenv())


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = os.environ.get('EMAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True

    # Flask_Jwt settings
    JWT_SECRET_KEY = os.environ.get('SECRET_KEY')
    JWT_TOKEN_LOCATION = ['headers', 'cookies']
    JWT_ACCESS_TOKEN_EXPIRES = 18000 * 18000  # 30 mins
    JWT_REFRESH_TOKEN_EXPIRES = 1800  # 30 mins
    JWT_HEADER_NAME = 'Authorization'
    JWT_HEADER_TYPE = 'Bearer'


class TestConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
