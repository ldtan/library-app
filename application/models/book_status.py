# [START of Imports]
from core.sqlalchemy import BaseModel, db
from datetime import datetime
# [END of Imports]

"""
Defines a book's current status from a given point in time, recording its
history.
"""
class BookStatus(BaseModel):

    __tablename__ = 'book_statuses'

    # [START of Columns]
    book_copy_id = db.Column(db.Integer, db.ForeignKey('book_copies.id'),
            nullable=False)
    current_holder_id = db.Column(db.Integer, db.ForeignKey('identities.id'))
    status = db.Column(db.String(20))
    started_on = db.Column(db.DateTime, default=datetime.utcnow)
    ended_on = db.Column(db.DateTime, default=datetime.utcnow)
    # [END of Columns]
