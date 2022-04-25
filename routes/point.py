import flask
from flask import Blueprint, render_template, redirect, url_for, flash, session
from flask_login import login_required

from forms.point import PointForm
from models import Point, User
from utils.db import db

point = Blueprint("point", __name__)


@point.route('/', methods=['GET'])
@login_required
def points():
    user_id = session["_user_id"]

    points = Point.query.all()
    user = User.query.get(user_id)
    bought_points = User.query.get(user_id).points

    return render_template('point/point_list.html', points=points, bought_points=bought_points, user=user)


@point.route('/<int:id>/', methods=['GET'])
@login_required
def detail_point(id):
    user_id = session["_user_id"]

    point = Point.query.get(id)
    user = User.query.get(user_id)

    is_buy = True if len(User.query.get(user_id).points.filter(
        Point.id == id).all()) == 0 else False

    return render_template('point/point_detail.html', point=point, is_buy=is_buy)


@point.route('/new', methods=['GET', 'POST'])
@login_required
def add_point():
    form = PointForm()
    if form.validate_on_submit():
        user_id = session["_user_id"]
        point = Point(
            title=form.title.data,
            description=form.description.data,
            price=form.price.data,
            quantity=form.quantity.data,
            author_id=user_id
        )
        db.session.add(point)
        db.session.commit()
        return redirect(url_for('point.points'))
    return render_template('point/point_create.html', form=form)


@point.route("/<int:id>/edit/", methods=["GET", "POST"])
def update(id):
    point = Point.query.get_or_404(id)

    form = PointForm()

    if form.validate_on_submit():
        point.title = form.title.data,
        point.description = form.description.data,
        point.price = form.price.data,
        point.quantity = form.quantity.data,

        db.session.commit()

        flash('Point updated successfully!')

        return redirect(url_for('point.points'))

    return render_template("point/point_edit.html", form=form)


@point.route("/<int:id>/delete/", methods=["GET"])
def delete(id):
    point = Point.query.get(id)
    db.session.delete(point)
    db.session.commit()

    flash('Point deleted successfully!')

    return redirect(url_for('point.points'))


@point.route("/<int:id>/buy/", methods=["GET"])
def bought_by_user(id):
    user_id = session["_user_id"]

    point = Point.query.get(id)
    user = User.query.get(user_id)

    bought_points_count = len(User.query.get(user_id).points.filter(Point.id == id).all())

    if bought_points_count == 0:
        if point.quantity > point.sold_count:

            user.points.append(point)
            point.sold_count += 1

            db.session.add(user)
            db.session.commit()

            flash('Point bought successfully!')
        else:
            flash('Point bought unsuccessfully!')
    else:
        flash('Point already bought!')

    return redirect(url_for('point.points'))
