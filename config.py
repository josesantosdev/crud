from distutils.debug import DEBUG

class BaseConfig():
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://admin:admin123@localhost/books'
    DATABASE_CONNECT_OPRTIONS = {}