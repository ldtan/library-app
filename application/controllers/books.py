# [START of Imports]
import json
from application.forms import BookRegistration, EditBook, UpdateBookStatus
from application.models import BookCopy, BookStatus, Book
from core.sqlalchemy import db
from datetime import datetime
from flask import abort, Blueprint, jsonify, render_template, request, session
from sqlalchemy.exc import SQLAlchemyError
# [END of Imports]

books = Blueprint('books', __name__, url_prefix='/books')


def book_to_dict(book):
    return_dict = book.to_dict()
    return_dict['copies'] = [copy.to_dict() for copy in book.copies]

    return return_dict


@books.route('/register', methods=['GET', 'POST'])
def register():
    try:
        if not session['logged_in']:
            abort(401)

        form = BookRegistration()

        if request.method == 'GET':
            return render_template('register_book.html', form=form)
            
        req_body = request.form

        if 'copies' not in req_body:
            abort(400, 'Required acquisitions')

        book_dict = {key: value for key, value in req_body.iteritems()
                if key in Book.__table__.columns}
        book = Book(**book_dict).insert()

        db.session.flush()

        for acquisition in req_body['copies'].split():
            copy = BookCopy(acquisition=acquisition, book_id=book.id).insert()
            db.session.flush()
            BookStatus(book_copy_id=copy.id, status='on-shelf').insert()

        db.session.commit()

        return 'Book registered successfully'

    except SQLAlchemyError as error:
        db.session.rollback()
        abort(400, str(error))


@books.route('/<string:isbn>/update', methods=['GET', 'POST'])
def edit(isbn):
    try:
        if not session['logged_in']:
            abort(401)
        
        book = Book.query.filter_by(isbn=isbn, deleted=False)\
                .first_or_404()

        form = EditBook(**book.to_dict())

        if request.method == 'GET':
            return render_template('edit_book.html', form=form)

        req_body = request.form

        book_dict = {key: value for key, value in req_body.iteritems()
                if key in Book.__table__.columns}
        book.populate(**book_dict)

        if 'add_copies' in req_body:
            for acquisition in req_body['add_copies'].split():
                copy = BookCopy(acquisition=acquisition, book_id=book.id).insert()
                db.session.flush()
                BookStatus(book_copy_id=copy.id, status='on-shelf').insert()

        db.session.commit()

        return 'Edited book successfully'

    except SQLAlchemyError as error:
        db.session.rollback()
        abort(400)


@books.route('/<string:isbn>/<string:acquisition>', methods=['GET', 'POST'])
def update_book_status(isbn, acquisition):
    try:
        if not session['logged_in']:
            abort(401)

        book = Book.query.filter_by(isbn=isbn, deleted=False).first_or_404()
        copy = BookCopy.query.filter_by(acquisition=acquisition,
                deleted=False).first_or_404()
        current_status = BookStatus.query.filter_by(book_copy_id=copy.id,
                deleted=False).order_by(BookStatus.created_on.desc())\
                .first_or_404()

        form = UpdateBookStatus(status=current_status.status)

        if request.method == 'GET':
            return render_template('update_book_status.html', form=form)

        req_body = request.form

        if req_body['status'] == current_status.status:
            abort(400, 'No updates')

        BookStatus(book_copy_id=copy.id, status=req_body['status']).insert()
        db.session.commit()

        return 'Successfully updated book status'

    except SQLAlchemyError as error:
        db.session.rollback()
        abort(400)


# @books.route('/copies/<string:url_safe>', methods=['PUT'])
# def update_status(url_safe):
#     try:
#         req_body = request.get_json()

#         # statuses = ['on-shelf', 'on-repair', 'read',
#         #         'borrowed', 'unreturned', 'lost']

#         book_status = BookStatus.query.order_by(BookStatus.created_on.desc(),
#                 BookStatus.updated_on.desc()).first_or_404()
#         current_status = book_status.status
#         update_status = req_body['status']
#         now = datetime.utcnow()

#         if update_status == current_status:
#             abort(400)

#         if current_status == 'reserved':
#             if 

#         elif current_status == 'borrowed':
#             pass

#     except SQLAlchemyError as error:
#         db.session.rollback()
#         abort(400)


# def book_to_dict(book):
#     return_dict = book.to_dict()
#     return_dict['copies'] = [copy.to_dict() for copy in book.copies]

#     return return_dict


# @books.route('/', methods=['POST'])
# def create():
#     try:
#         req_body = request.get_json()

#         if 'copies' not in req_body:
#             abort(400)

#         book_dict = {key: value for key, value in req_body.iteritems()
#                 if key in Book.__table__.columns}
#         book = Book(**book_dict).insert()

#         for acquisition in req_body['copies'].split('\n'):
#             copy = BookCopy(acquisition=acquisition, book_id=book.id).insert()
#             BookStatus(book_copy_id=copy.id, status='registered').insert()
#             BookStatus(book_copy_id=copy.id, status='on-shelf').insert()

#         db.session.commit()

#         return jsonify(book_to_dict(book))

#     except SQLAlchemyError as error:
#         db.session.rollback()
#         abort(400)


# @books.route('/<string:acquisition>', methods=['PUT'])
# def update(acquisition):
#     try:
#         req_body = request.get_json()

#         book_dict = {key: value for key, value in req_body.iteritems()
#                 if key in Book.__table__.columns}
        

#     except SQLAlchemyError as error:
#         db.session.rollback()
#         abort(400)
