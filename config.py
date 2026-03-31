import os

class Config:
    DEBUG=os.environ.get('DEBUG')

    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL')

    SECRET_KEY=os.environ.get('SECRET_KEY')