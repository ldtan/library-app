# [START of Imports]
from core.sqlalchemy import BaseModel, db
from datetime import datetime
# [END of Imports]

class BookStatus(BaseModel):

    __tablename__ = 'books_status'

    # [START of Columns]
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    current_holder_id = db.Column(db.Integer, db.ForeignKey('identities.id'))
    status = db.Column(db.String(20))
    started_on = db.Column(db.DateTime, default=datetime.utcnow)
    ended_on = db.Column(db.DateTime)
    # [END of Columns]