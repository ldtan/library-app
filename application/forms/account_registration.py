# [START of Imports]
from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, SelectField, StringField
from wtforms.validators import DataRequired, Email, EqualTo
# [END of Imports]

"""

"""
class AccountRegistration(FlaskForm):

    first_name = StringField('First Name', validators=[DataRequired()])
    middle_name = StringField('Middle Name')
    last_name = StringField('Last Name', validators=[DataRequired()])
    sex = SelectField('Sex', choices=[('male', 'Male'), ('female', 'Female')])
    contact = StringField('Contact Number')
    address = StringField('Address', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(),Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(),
            EqualTo('confirm_password', message='Passwords must match')])
    confirm_password = PasswordField('Confirm Password')
    accept_terms = BooleanField('Accept Terms of Service',
            validators=[DataRequired()])
