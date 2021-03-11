import os

class Config(object): # P.22 Here can be added more config settings.
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'DummyKey' # P.22 _ This can also be set in the `__init__.py` file of in the app Directory. # Against Cross-Site Request Forgery (CSRF), pronounced as 'seasurf`.

