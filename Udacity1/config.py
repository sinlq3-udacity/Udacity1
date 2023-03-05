import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'sinlq3udacity1sa'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or '3Rc7Y2hBUSiwq9WITuZbYoLf5vEX9sFc++M/EM++3RsShWZFzXLAuvRjTugP+LtJoVbi6gkwSSQJ+ASt1MHAzA=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'udacity1'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'sinlq3udacity1.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'udacity-1'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'udacity'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Passw0rd'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET = "w~V8Q~3uA6GyhC7yQacK8gtZ~ZrCvdVH2qFxyaCO"
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    # if not CLIENT_SECRET:
    #     raise ValueError("Need to define CLIENT_SECRET environment variable")

    #AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    AUTHORITY = "https://login.microsoftonline.com/f958e84a-92b8-439f-a62d-4f45996b6d07"

    CLIENT_ID = "35cb749e-5e6f-40e9-9656-3b5e5a465453"

    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session