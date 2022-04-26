from flask_login import UserMixin
from sqlalchemy.orm import backref

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

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name


class UserPoint(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    point_id = db.Column(db.Integer, db.ForeignKey('point.id', ondelete='CASCADE'))
    point = db.relationship("Point", backref=backref("points", uselist=False), passive_deletes=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    user = db.relationship("User", backref=backref("users", uselist=False), passive_deletes=True)
