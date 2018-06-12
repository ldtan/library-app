# [START of Imports]
from flask_wtf import FlaskForm
from wtforms import DateField, PasswordField, StringField, TextAreaField
from wtforms.validators import DataRequired, Optional
# [END of Imports]

"""

"""
class BookRegistration(FlaskForm):

    isbn = StringField('ISBN', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    edition = StringField('Edition', validators=[DataRequired()])
    publisher = StringField('Publisher')
    published_on = DateField('Published Date', format='%m/%d/%Y', validators=[Optional()])
    description = TextAreaField('Description')
    copies = TextAreaField('Copies (acquisition number per line)',
            validators=[DataRequired()])
    tags = TextAreaField('Tags (tag per line)')
