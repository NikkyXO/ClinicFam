from flask_mail import Mail
from flask_jwt_extended import JWTManager, decode_token
from flask_login import LoginManager
from flask_cors import CORS, cross_origin


mail = Mail()
jwt = JWTManager()
login_manager = LoginManager()
Cors_app = CORS()

def security_handler(token):
    return decode_token(token)