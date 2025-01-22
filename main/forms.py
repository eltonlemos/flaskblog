from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField
from flaskblog.models import User, Post

class SearchForm(FlaskForm):
	search = StringField('Search')
	submit = SubmitField('Search')

		


