# [START of Imports]
from application import create_app
from application import models
from application import controllers
from core.sqlalchemy import db
# [END of Imports]

if __name__ == '__main__':
    app = create_app()
    db.init_app(app)
    db.create_all()

    # [model.create_table() for model in [
    #     models.Identity,
    #     models.Account,
    #     models.Book,
    #     models.BookCopy,
    #     models.BookStatus,
    #     models.Transaction
    # ]]

    [app.register_blueprint(controller) for controller in [
        controllers.accounts,
        controllers.books
    ]]

    app.run()
