from flask_login import UserMixin

from utils.db import db

from werkzeug.security import generate_password_hash, check_password_hash

bought_points_by_user_identifier = db.Table('bought_points_by_user_identifier',
                                            db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                                            db.Column('point_id', db.Integer, db.ForeignKey('point.id')),
                                            )


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(63))
    last_name = db.Column(db.String(63))
    email = db.Column(db.String(63), unique=True)
    password = db.Column(db.String(200))
    points = db.relationship("Point", secondary=bought_points_by_user_identifier, lazy='dynamic')

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name
