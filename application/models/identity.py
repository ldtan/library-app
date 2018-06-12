# [START of Imports]
from core.sqlalchemy import BaseModel, db
# [END of Imports]

"""
Contains general information of a certain person registered in the system.
"""
class Identity(BaseModel):

    __tablename__ = 'identities'

    # [START of Columns]
    first_name = db.Column(db.String(50), nullable=False)
    middle_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50), nullable=False)
    sex = db.Column(db.String(10), nullable=False)
    contact = db.Column(db.String(15))
    address = db.Column(db.String(255))
    # [END of Columns]

    # [START of Relationships]
    accounts = db.relationship('Account', backref='identities', lazy=True)
    book_history = db.relationship('BookStatus', backref='identities',
            lazy=True)
    transactions = db.relationship('Transaction', backref='identities',
            lazy=True)
    # [END of Relationships]
