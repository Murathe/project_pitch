from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class Signup_form(wtforms):
    username = StringField('Username', validators=[DataRequired(), Length(min=5, max=15)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Passowrd', validators=[DataRequired(),])
    confirm_password = PasswordField('Confirm password', validators=[DataRequired(), EqualTo('password')])