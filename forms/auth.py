from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class RegistrationForm(FlaskForm):
    first_name = StringField('first_name', validators=[Length(min=2), DataRequired()])
    last_name = StringField('last_name', validators=[Length(min=2), DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password1 = PasswordField('Password', validators=[Length(min=8), DataRequired()])
    password2 = PasswordField('Confirm Password', validators=[Length(min=8), DataRequired(), EqualTo('password1')])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[Length(min=8), DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
