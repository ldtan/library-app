# [START of Imports]
from application import create_app
from application.models import (
    account,
    book_status,
    book,
    identity,
    transaction
)
from application.controllers import (
    accounts,
    books_status,
    books,
    identities,
    transactions
)
from core.sqlalchemy import db
# [END of Imports]

if __name__ == '__main__':
    app = create_app()
    db.init_app(app)

    models = [
        identity.Identity,
        book.Book,
        account.Account,
        book_status.BookStatus,
        transaction.Transaction
    ]

    for model in models:
        try:
            model.create_table()

        except Exception as error:
            pass

    controllers = [
        identities.identities,
        books.books,
        accounts.accounts,
        books_status.books_status,
        transactions.transactions
    ]

    for controller in controllers:
        app.register_blueprint(controller)

    app.run()