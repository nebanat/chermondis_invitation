"""
    This defines a sample of application settings/configuration

    To do:
        - Create a settings.py file and define your application settings
        like the configs in the settings.py

    Note: You can decide to read app settings from a .env file
    don't forget to update the app.py file
"""
DEBUG = True

SECRET_KEY = 'some random string'

# db_uri = 'mysql+pymysql://root:coldplay@localhost/chermondis'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:coldplay@localhost/chermondis'
SQLALCHEMY_TRACK_MODIFICATIONS = False

SEED_ADMIN_EMAIL = 'dev@chermondis.com'
SEED_ADMIN_PASSWORD = 'devpassword'

