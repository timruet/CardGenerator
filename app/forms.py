from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length

class PromptForm(FlaskForm):
    occasion = StringField('Occasion', validators=[DataRequired()])
    text1 = StringField('Property1')
    text2 = StringField('Property2')
    text3 = StringField('Property3')
    submit = SubmitField('Generate')

