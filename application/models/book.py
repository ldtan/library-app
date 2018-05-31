# [START of Imports]
from core.sqlalchemy import BaseModel, db
# [END of Imports]

class Book(BaseModel):

    __tablename__ = 'books'

    # [START of Columns]
    accusation = db.Column(db.String(20), unique=True, nullable=False)
    title = db.Column(db.String(50), nullable=False)
    author = db.Column(db.String(50))
    publisher = db.Column(db.String(50))
    published_on = db.Column(db.Date)
    tags = db.Column(db.Text)
    # [END of Columns]

    # [START of Relationships]
    books_status = db.relationship('BookStatus', backref='books', lazy=True)
    # [END of Relationships]