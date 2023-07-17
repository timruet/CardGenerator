from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length

class PromptForm(FlaskForm):
    occasion = StringField('1. Occasion', validators=[DataRequired()], default="e.g. birthday")
    length = SelectField('2. Length', choices=['short', 'medium length','long'], validators=[DataRequired()])
    content = TextAreaField('3. Content', render_kw={'style': 'height: 200px'}, default="e.g. memories, good times")
    submit = SubmitField('Generate')



