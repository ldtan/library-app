# [START of Imports]
import os
from flask import Flask
# [END of Imports]

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.template_folder = 'application/views'
    app.static_folder = 'application/static'

    # Load the default configuration
    app.config.from_object('config.default')

    # Load the configuration from the instance folder
    app.config.from_pyfile('config.py')

    # Load the file specified by the APP_CONFIG_FILE environment variable
    # Variables defined here will override those in the default configuration
    app.config.from_object(os.getenv('APP_CONFIG_FILE', 'config.development'))

    return app