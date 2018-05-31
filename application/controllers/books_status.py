# [START of Imports]
from application.models.book_status import BookStatus
from core.sqlalchemy import db
from flask import abort, Blueprint, jsonify, request
# [END of Imports]

books_status = Blueprint('books_status', __name__, url_prefix='/books_status')


@books_status.route('/', methods=['POST'])
def create():
    try:
        req_body = request.get_json()
        record = BookStatus(**req_body).insert()
        db.session.commit()

        return jsonify(record.to_dict())

    except SQLAlchemyError as error:
        db.session.rollback()
        abort(400)


@books_status.route('/<int:id>', methods=['PUT'])
def update(id):
    try:
        record = BookStatus.query.filter_by(id=id, deleted=False).first()

        if record is None:
            abort(404)

        req_body = request.get_json()
        req_body.pop('deleted', None)
        record.populate(**req_body)
        db.session.commit()

        return jsonify(record.to_dict())

    except SQLAlchemyError as error:
        db.session.rollback()
        abort(400)


@books_status.route('/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        record = BookStatus.query.filter_by(id=id, deleted=False).first()

        if record is None:
            abort(404)

        record.populate(deleted=True)
        db.session.commit()

        return jsonify(record.to_dict())

    except SQLAlchemyError as error:
        db.session.rollback()
        abort(400)


@books_status.route('/', methods=['GET'])
def get_all():
    sort_by = request.args.get('sort_by', 'updated_on', str)
    order_by = request.args.get('order_by', 'desc', str)
    limit = request.args.get('limit', None, int)
    page = request.args.get('page', 1, int) if limit is not None else None

    query = BookStatus.query.filter_by(deleted=False)

    if hasattr(BookStatus, sort_by):
        column = BookStatus.get_columns()[sort_by]
        query = query.order_by(column.desc() if sort_by == 'desc' else column)

    if limit is not None:
        query = query.limit(limit)

    if page is not None:
        query = query.offset((page - 1) * limit)

    return jsonify([record.to_dict() for record in query.all()])


@books_status.route('/<int:id>', methods=['GET'])
def get(id):
    record = BookStatus.query.filter_by(id=id, deleted=False).first_or_404()
    return jsonify(record.to_dict())