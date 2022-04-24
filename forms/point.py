from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, FloatField
from wtforms.validators import DataRequired, Length, NumberRange


class PointForm(FlaskForm):
    title = StringField('Title', validators=[Length(min=2), DataRequired()])
    description = TextAreaField('Description', validators=[Length(min=10), DataRequired()])
    price = FloatField('Price', validators=[NumberRange(min=0), DataRequired()])
    quantity = IntegerField('Quantity', validators=[NumberRange(min=0), DataRequired()])
