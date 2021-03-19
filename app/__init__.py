from flask import Flask     # We only import Flask, not the whole flask.
from config import Config   # P.23 _ The `config` is the config.py file and this is done to read the token against seasurf. 
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate # This is for the Alembic extension, to track database changes.

from flask_login import LoginManager

app = Flask(__name__) # P.6 We create an instance. # With this, it can find out the location on disk, so it can locate other files and directories.
app.config.from_object(Config)

db = SQLAlchemy(app) # P.38 
migrate = Migrate(app, db) # The Alembic database tracker, needs the app and the db as arguments.
login = LoginManager(app)
login.login_view = 'login' # P.57 This is the URL-for # This is telling where the login page is

# app.config['SECRET_KEY'] = "DummyKey" # P.22 _ This can be done, or it can be get from the OS, in this case you can create a `config.py` file in the top level.

# The secret key can be read in the Python interpreter via:
# >>> from microblog import app
# >>> app.config['SECRET_KEY']

from app import routes # P.5 At the bottom, to prevent 'circular imports'. # The `routes` refers to the `routes.py`-file.
from app import models # This is for the database. This is at the bottom for again 'circulair dependancies`.


