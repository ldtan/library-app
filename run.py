# [START of Imports]
from application import create_app
from application import models
from application import controllers
from core.sqlalchemy import db
from flask import render_template
# [END of Imports]

if __name__ == '__main__':
    app = create_app()
    db.init_app(app)
    db.create_all()

    [app.register_blueprint(controller) for controller in [
        controllers.accounts,
        controllers.books
    ]]


    @app.route('/', methods=['GET'])
    def index():
        return render_template('dashboard.html')
        

    app.run()
