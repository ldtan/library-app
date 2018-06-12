# [START of Imports]
from flask_wtf import FlaskForm
from wtforms import SelectField
from wtforms.validators import DataRequired
# [END of Imports]

"""

"""
class UpdateBookStatus(FlaskForm):

    status = SelectField('Status', choices=[
            ('on-shelf', 'On-shelf'),
            ('on-repair', 'On-repair'),
            ('reserved', 'Reserved'),
            ('read', 'Read'),
            ('borrowed', 'Borrowed'),
            ('un-returned', 'lost')])
