from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length

class Signup_form(wtforms):
    username = StringField('Username', validators=[DataRequired(), Length(min=5, max=15)])
    email =StringField('Email', validators=[DataRequired(), Email()])