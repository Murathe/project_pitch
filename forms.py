from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length

class Signup_form(wtforms):
    username = StringField('username', validators=[])