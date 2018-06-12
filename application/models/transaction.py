# [START of Imports]
from core.sqlalchemy import BaseModel, db
# [END of Imports]

"""
Contains information of a transaction that happened.
"""
class Transaction(BaseModel):

    __tablename__ = 'transactions'

    # [START of Columns]
    identity_id = db.Column(db.Integer, db.ForeignKey('identities.id'),
            nullable=False)
    amount = db.Column(db.Float, default=0.00, nullable=False)
    purpose = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(20), nullable=False)
    # [END of Columns]
