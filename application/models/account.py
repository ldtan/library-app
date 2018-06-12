# [START of Imports]
from core.sqlalchemy import BaseModel, db
from werkzeug.security import generate_password_hash, check_password_hash
# [END of Imports]

"""
Available for students and other school personels to use, to access specific 
and private data through the school's website.
"""
class Account(BaseModel):

    __tablename__ = 'accounts'

    # [START of Columns]
    identity_id = db.Column(db.Integer, db.ForeignKey('identities.id'),
            nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    confirmed_on = db.Column(db.DateTime)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(20), nullable=False, default='unconfirmed')
    # [END of Columns]

    def hash_password(self):
        self.password = generate_password_hash(self.password)
        print type(self.password)
        print self.password
        return self.password


    def check_password(self, password):
        return check_password_hash(self.password, password)
