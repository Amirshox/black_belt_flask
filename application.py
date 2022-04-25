from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from config import DATABASE_CONNECTION_URI
from models import User
from routes import auth, point
from utils.db import db

application = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(application)
login_manager.login_view = 'auth.index'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


# settings
application.secret_key = 'mysecret'

application.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

SQLAlchemy(application)

application.register_blueprint(auth)
application.register_blueprint(point, url_prefix='/points')

with application.app_context():
    db.create_all()

if __name__ == '__main__':
    application.run(debug=True, port=5000)
