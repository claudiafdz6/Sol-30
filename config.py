import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'guess'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///tickets.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
