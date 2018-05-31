DEBUG = True
SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}/{}'.format(
    'mysql',            # Driver
    'root',             # Username
    '',                 # Password
    'localhost',        # Host
    'library_app'       # Database
)
SQLALCHEMY_TRACK_MODIFICATIONS = True