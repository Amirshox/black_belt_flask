from sqlalchemy.orm import backref

from utils.db import db


class Point(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    price = db.Column(db.Float, unique=True)
    quantity = db.Column(db.Integer)
    sold_count = db.Column(db.Integer, default=0)

    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = db.relationship("User", backref=backref("user", uselist=False))
