import os
basedir = os.path.abspath(os.path.dirname(__file__)) # P.37, this is the location, which is equal to the path of the `__file__`, and the file is `config.py` 
class Config(object): # P.22 Here can be added more config settings.
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'DummyKey' # P.22 _ This can also be set in the `__init__.py` file of in the app Directory. # Against Cross-Site Request Forgery (CSRF), pronounced as 'seasurf`.
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db' # P.37 The after the two slashes '//', there should be the servername, which is local, so there is none, so this can be empty, so a third slash '/'. Than the databasename you want to call it.
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db') # P.27 This is the same location as above.
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db') # P.27 This is the same location as above. # Use this, as the `DATABASE_URL` is set, otherwise use the `app.db` 
    SQLALCHEMY_TRACK_MODIFICATIONS = False # It will nag you with notifications everytime a change has been made.