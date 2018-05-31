# [START of Imports]
from application import create_app
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
# [END of Imports]

db = SQLAlchemy(create_app(), session_options={'autocommit': False})

class BaseModel(db.Model):

    __abstract__ = True

    # [START of Columns]
    id = db.Column(db.Integer, primary_key=True)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)
    updated_on = db.Column(db.DateTime, onupdate=datetime.utcnow)
    deleted = db.Column(db.Boolean, default=False, nullable=False)
    # [END of Columns]

    @classmethod
    def create_table(cls):
        return cls.__table__.create(db.engine)


    @classmethod
    def drop_table(cls):
        return cls.__table__.drop(db.engine)

    
    @classmethod
    def get_columns(cls):
        return cls.__table__.c


    def __repr__(self):
        return '<{}({})>'.format(
            self.__class__.__name__,
            ', '.join('%s=%r'.format(n, getattr(self, n)) for n in self.all_fields().keys())
        )


    def populate(self, **columns):
        for column, value in columns.iteritems():
            setattr(self, column, value)

        return self


    def insert(self):
        db.session.add(self)
        return self


    def refresh(self):
        db.session.refresh(self)
        return self


    def expire(self):
        db.session.expire(self)
        return self


    def to_dict(self, includes=all, excludes=None):
        includes = (self.get_columns().keys() if includes is all
            else [] if includes is None
            else includes)
        excludes = (self.excludes if excludes else [])

        return {column: getattr(self, column) for column in includes
            if column not in excludes}
