# [START of Imports]
from flask import Blueprint, render_template
# [END of Imports]

pages = Blueprint('pages', __name__)

@pages.route('/<string:page>', methods=['GET'])
def index(page):
    return render_template(page)