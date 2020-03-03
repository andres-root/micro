import os


class Config(object):
    def __init__(self):
        self.SECRET_KEY = os.environ.get('SECRET_KEY') or 'this-is-my-secret!'
        