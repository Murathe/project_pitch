import os

class Config:
    '''
    Parent class - general
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'PITCH'
    SENDER_EMAIL = 'murathe@gmail.com'
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:izoh1234@localhost/murathe'
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConfig(Config):
    '''
    Pruduction configuration child class
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
    '''
    Testing configuration child class
    '''
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:izoh1234@localhost/murathe'

class DevConfig(Config):
    '''
    Development configuration child class

    
    '''
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:izoh1234@localhost/murathe'
    DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}