# [START of Imports]
from core.sqlalchemy import BaseModel, db
# [END of Imports]

class Account(BaseModel):

    __tablename__ = 'accounts'

    # [START of Columns]
    identity_id = db.Column(db.Integer, db.ForeignKey('identities.id'), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(20), nullable=False)
    # [END of Columns]