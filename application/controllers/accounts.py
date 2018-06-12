# [START of Imports]
from application.forms import AccountRegistration, Login, EditAccount
from application.models import Account, Identity
from core.sqlalchemy import db
from flask import abort, Blueprint, jsonify, redirect, render_template, request, session, url_for
from sqlalchemy.exc import SQLAlchemyError
# [END of Imports]

accounts = Blueprint('accounts', __name__, url_prefix='/accounts')


def account_to_dict(account, identity=None):
    identity = Identity.query.filter_by(account.identity_id)\
            .first_or_404() if identity == None else identity

    account_dict = account.to_dict(exclude=['identity_id'])
    account_dict['identity'] = identity.to_dict()

    return account_dict


@accounts.route('/register', methods=['GET', 'POST'])
def register():
    try:    
        form = AccountRegistration()

        if request.method == 'GET':
            return render_template('register_account.html', form=form)

        req_body = request.form

        identity_dict = {key: value for key, value in req_body.iteritems()
                if key in Identity.__table__._columns}
        identity = Identity(**identity_dict).insert()

        db.session.flush()
        
        account_dict = {key: value for key, value in req_body.iteritems()
                if key in Account.__table__._columns}
        account_dict['identity_id'] = identity.id
        account_dict.update(
            identity_id=identity.id,
            category='user'
        )
        account = Account(**account_dict)
        account.hash_password()
        account.insert()

        db.session.commit()

        return 'Registered successfully'

    except SQLAlchemyError as error:
        db.session.rollback()
        abort(400, str(error))


@accounts.route('/login', methods=['GET', 'POST'])
def login():
    form = Login()

    if request.method == 'GET':
        return render_template('login.html', form=form)

    req_body = request.form

    account = Account.query.filter_by(username=req_body['username'],
            deleted=False).first()

    if account == None:
        abort(400, 'Account does not exist')

    if account.check_password(req_body['password']):
        session.update(username=account.username, logged_in=True)
        return 'Logged in successfully'

    else:
        abort(400, 'Wrong password')


@accounts.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('username')
    session.pop('logged_in')

    return redirect(url_for('accounts.login'))


@accounts.route('/edit', methods=['GET', 'POST'])
def edit():
    try:
        if not session['logged_in']:
            abort(401)

        account = Account.query.filter_by(username=session['username'],
                deleted=False).first_or_404()
        identity = Identity.query.filter_by(id=account.identity_id,
                deleted=False).first_or_404()
        
        form_dict = account.to_dict()
        form_dict.update(identity.to_dict())
        form = EditAccount(**form_dict)

        if request.method == 'GET':
            return render_template('edit_account.html', form=form)

        req_body = request.form

        account_dict = {key: value for key, value in req_body.iteritems()
                if key in Account.__table__._columns}
        account.populate(**account_dict)
        identity_dict = {key: value for key, value in req_body.iteritems()
                if key in Identity.__table__._columns}
        identity.populate(**identity_dict)

        db.session.commit()

        return 'Edited account successfully'

    except SQLAlchemyError as error:
        db.session.rollback()
        abort(400)


# def account_to_dict(account, identity=None):
#     identity = (Identity.filter_by(id=account.identity_id).first_or_404()
#             if identity == None else identity)

#     return_dict = account.to_dict()
#     return_dict.pop('identity_id')
#     return_dict['identity'] = identity.to_dict()

#     return return_dict


# @accounts.route('/', methods=['GET'])
# def get_all():
#     try:
#         sort_by = request.args.get('sort_by', 'updated_on', str)
#         order_by = request.args.get('order_by', 'desc', str)
#         limit = request.args.get('limit', None, int)
#         page = request.args.get('page', 1, int) if limit is not None else None

#         query = Account.query.filter_by(deleted=False)

#         if hasattr(Account, sort_by):
#             column = Account.get_columns()[sort_by]
#             query = query.order_by(column.desc() if sort_by == 'desc' else column)

#         if limit is not None:
#             query = query.limit(limit)

#         if page is not None:
#             query = query.offset((page - 1) * limit)

#         return jsonify([account_to_dict(account) for account in query.all()])

#     except SQLAlchemyError as error:
#         abort(400)


# @accounts.route('/<string:username>', methods=['GET'])
# def get(username):
#     try:
#         account = Account.filter_by(username=username, deleted=False)\
#                 .first_or_404()

#         return jsonify(account_to_dict(account))

#     except SQLAlchemyError as error:
#         abort(400)


# @accounts.route('/', methods=['POST'])
# def create():
#     try:
#         req_body = request.get_json()

#         identity_dict = {key: value for key, value in req_body.iteritems()
#                 if key in Identity.__table__._columns}
#         identity = Identity(**identity_dict).insert()

#         account_dict = {key: value for key, value in req_body.iteritems()
#                 if key in Account.__table__._columns}
#         account_dict['identity_id'] = identity.id
#         account = Account(**account_dict).insert()

#         db.session.commit()
        
#         return jsonify(account_to_dict(account, identity))

#     except SQLAlchemyError as error:
#         db.session.rollback()
#         abort(400)


# @accounts.route('/<string:username>', methods=['PUT'])
# def update(username):
#     try:
#         req_body = request.get_json()

#         account_dict = {key: value for key, value in req_body.iteritems()
#                 if key in Account.__table__._columns}
#         account = Account.filter_by(username=username, deleted=False)\
#                 .first_or_404().populate(**account_dict)

#         identity_dict = {key: value for key, value in req_body.iteritems()
#                 if key in Identity.__table__._columns}
#         identity = Identity(id=account.identity_id, deleted=False)\
#                 .first_or_404().populate(identity_dict)

#         db.session.commit()

#         return jsonify(account_to_dict(account, identity))

#     except SQLAlchemyError as error:
#         db.session.rollback()
#         abort(400)


# @accounts.route('/<string:username>')
# def delete(username):
#     try:
#         account = Account.filter_by(username=username, deleted=False)\
#                 .first_or_404()
#         account.deleted = True

#         db.session.commit()

#         return jsonify(account_to_dict(account))

#     except SQLAlchemyError as error:
#         db.session.rollback()
#         abort(400)
