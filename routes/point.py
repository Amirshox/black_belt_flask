import flask
from flask import Blueprint, render_template, redirect, url_for, flash, session
from flask_login import login_required
from sqlalchemy import and_, or_, not_
from sqlalchemy import desc
from sqlalchemy.orm import load_only

from forms.point import PointForm
from models import Point, User, UserPoint
from utils.db import db

point = Blueprint("point", __name__)


@point.route('/', methods=['GET'])
@login_required
def points():
    user_id = session["_user_id"]

    user = User.query.get(user_id)

    # points_id = list()
    #
    # point_ids = UserPoint.query.filter(UserPoint.user_id.like(user_id)).with_entities(UserPoint.point_id).all()
    #
    # for point_id in point_ids:
    #     points_id.append(point_id[0])
    #
    # bought_points = Point.query.filter(Point.id.in_(points_id)).order_by(desc(Point.id))

    points = Point.query.order_by(desc(Point.id))

    return render_template('point/point_list.html', points=points, bought_points=bought_points, user=user)


@point.route('/<int:id>/', methods=['GET'])
@login_required
def detail_point(id):
    user_id = session["_user_id"]

    point = Point.query.get(id)

    is_buy = True \
        if UserPoint.query.filter(and_(UserPoint.point_id.like(id), UserPoint.user_id.like(user_id))).count() == 0 \
        else False

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

        db.session.add(point)
        db.session.commit()

        return redirect(url_for('point.points', id=point.id))

    form.title.data = point.title
    form.description.data = point.description
    form.price.data = point.price
    form.quantity.data = point.quantity

    return render_template("point/point_edit.html", form=form)


@point.route("/<int:id>/delete/", methods=["GET"])
def delete(id):
    point = Point.query.get(id)

    db.session.delete(point)
    db.session.commit()

    return redirect(url_for('point.points'))


@point.route("/<int:id>/buy/", methods=["GET"])
def bought_by_user(id):
    user_id = session["_user_id"]

    point = Point.query.get(id)

    bought_points_count = UserPoint.query.filter(
        and_(UserPoint.point_id.like(id), UserPoint.user_id.like(user_id))).count()

    if bought_points_count == 0:
        if point.quantity > point.sold_count:
            user_point = UserPoint(point_id=id, user_id=user_id)
            point.sold_count += 1

            db.session.add(user_point)
            db.session.commit()

    return redirect(url_for('point.detail_point', id=id))
