from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
	title= StringField('Title', validators=[DataRequired()])
	content = TextAreaField('Content', validators=[DataRequired()])
	submit = SubmitField('Post')
	genre = SelectField('Genre', choices=[("Horror",'Horror'), ('Romance','Romance'), ('Drama', 'Drama'),('Suspense','Suspense'), ('Comedy','Comedy'), ('General', 'General'), ('Sci-fy','Sci-fy')])
