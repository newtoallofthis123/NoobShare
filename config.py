import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = '4372093cd57da6dad99b7314'
    POSTGRES_HOST = os.environ.get("POSTGRES_HOST", "localhost")
    POSTGRES_USER = os.environ.get("POSTGRES_USER")
    POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
    POSTGRES_PORT = os.environ.get("POSTGRES_PORT", 5432)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POSTGRES_DB = os.environ.get("POSTGRES_DB", "ss_db")
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
        f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
    )


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = (
        "postgresql://bjpzfbupryzakv:b21b56f0b36e0b114706e0cc4241663a9998790cf8b7dd591e4fb293ba01af0a@ec2-44-198-82-71.compute-1.amazonaws.com:5432/dcv8qp2j7jn7j6"
    )


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True