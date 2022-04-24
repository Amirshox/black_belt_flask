from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required

from forms.auth import RegistrationForm, LoginForm
from models import User
from utils.db import db

auth = Blueprint("auth", __name__)


@auth.route('/register', methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).count() == 0:
            user = User(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data)
            user.set_password(form.password1.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))
        flash('Email Address is Already Registered.')
    return render_template('registration.html', form=form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.check_password(form.password.data):
            login_user(user)
            next = request.args.get("next")
            return redirect(next or url_for('home'))
        flash('Invalid email address or Password.')
    return render_template('login.html', form=form)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))
