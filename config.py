import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    # MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'PITCH'
    SENDER_EMAIL = 'samuelangienda1998@gmail.com'
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:12345@localhost/pitch'
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConfig(Config):
    '''
    Pruduction configuration child class
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("HEROKU_POSTGRESQL_CRIMSON_URL")

class TestConfig(Config):
    '''
    Testing configuration child class
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class
    '''
    DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}