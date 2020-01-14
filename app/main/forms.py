from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,SubmitField,TextAreaField,RadioField
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError

class PitchForm(FlaskForm):
	title = StringField('Title', validators=[Required()])
	description = TextAreaField("Pitch Idea",validators=[Required()])
	category = RadioField('Label', choices=[('movies','movies'), ('music','music'), ('art','art'),('general','general')],validators=[Required()])
	submit = SubmitField('Submit')

class CommentForm(FlaskForm):
	description = TextAreaField('Add your comments here!',validators=[Required()])
	submit = SubmitField('Add')

class UpvoteForm(FlaskForm):
	submit = SubmitField('Submit')

class Downvote(FlaskForm):
	submit = SubmitField('Submit')