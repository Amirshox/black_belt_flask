from utils.db import db


class Point(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(63))
    email = db.Column(db.String(63), unique=True)
    password = db.Column(db.String(200))
