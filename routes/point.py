from flask import Blueprint, render_template, redirect, url_for, flash, session
from flask_login import login_required

from forms.point import PointForm
from models import Point
from utils.db import db

point = Blueprint("point", __name__)


@point.route('/', methods=['GET'])
@login_required
def points():
    user_id = session["_user_id"]

    points = Point.query.all()
    user_points = Point.query.filter_by(author_id=user_id)

    return render_template('point/index.html', points=points, user_points=user_points)


@point.route('/new', methods=['GET', 'POST'])
@login_required
def add_point():
    form = PointForm()
    if form.validate_on_submit():
        user_id = session["user_id"]
        point = Point(
            title=form.title.data,
            description=form.description.data,
            price=form.price.data,
            quantity=form.quantity.data,
            author_id=user_id
        )
        db.session.add(point)
        db.session.commit()
    return render_template('point/index.html')


@point.route("/<int:id>/edit", methods=["GET", "POST"])
def update(id):
    point = Point.query.get(id)

    form = PointForm()
    if form.validate_on_submit():
        point.title = form.title.data,
        point.description = form.description.data,
        point.price = form.price.data,
        point.quantity = form.quantity.data,

        db.session.commit()

        flash('Point updated successfully!')

        return redirect(url_for('point.points'))

    return render_template("point/index.html", point=point)


@point.route("/<int:id>/delete", methods=["GET"])
def delete(id):
    point = Point.query.get(id)
    db.session.delete(point)
    db.session.commit()

    flash('Point deleted successfully!')

    return redirect(url_for('point.points'))
