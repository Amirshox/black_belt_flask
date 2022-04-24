from flask_login import UserMixin

from utils.db import db

from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(63))
    last_name = db.Column(db.String(63))
    email = db.Column(db.String(63), unique=True)
    password = db.Column(db.String(200))

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
