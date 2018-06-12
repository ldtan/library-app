# [START of Imports]
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField
from wtforms.validators import DataRequired
# [END of Imports]

"""

"""
class EditBook(FlaskForm):

    isbn = StringField('ISBN', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    edition = StringField('Edition', validators=[DataRequired()])
    publisher = StringField('Publisher')
    published_on = StringField('Published Date')
    description = TextAreaField('Description')
    add_copies = TextAreaField('Add Copies (acquisition number per line)')
    tags = TextAreaField('Tags (tag per line)')
