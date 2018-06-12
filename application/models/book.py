# [START of Imports]
from core.sqlalchemy import BaseModel, db
# [END of Imports]

"""
Contains general information of a specific book registed in the system.
"""
class Book(BaseModel):

    __tablename__ = 'books'

    # [START of Columns]
    isbn = db.Column(db.String(50), unique=True, nullable=False)
    title = db.Column(db.String(50), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    edition = db.Column(db.String(50), nullable=False)
    publisher = db.Column(db.String(50))
    published_on = db.Column(db.Date)
    description = db.Column(db.Text)
    tags = db.Column(db.Text)
    # [END of Columns]

    # [START of Relationships]
    copies = db.relationship('BookCopy', backref='books', lazy=True)
    # [END of Relationships]
