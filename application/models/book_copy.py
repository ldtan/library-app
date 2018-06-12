# [START of Imports]
from core.sqlalchemy import BaseModel, db
# [END of Imports]

"""
Contains information of a copy of a specific book.
"""
class BookCopy(BaseModel):

    __tablename__ = 'book_copies'

    # [START of Columns]
    acquisition = db.Column(db.String(20), unique=True, nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    # [END of Columns]

    # [START of Relationships]
    statuses = db.relationship('BookStatus', backref='book_copies', lazy=True)
    # [START of Relationships]    
