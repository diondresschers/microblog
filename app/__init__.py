from flask import Flask     # We only import Flask, not the whole flask.
from config import Config   # P.23 _ The `config` is the config.py file and this is done to read the token against seasurf. 

app = Flask(__name__) # P.6 We create an instance. # With this, it can find out the location on disk, so it can locate other files and directories.
app.config.from_object(Config)
# app.config['SECRET_KEY'] = "DummyKey" # P.22 _ This can be done, or it can be get from the OS, in this case you can create a `config.py` file in the top level.

# The secret key can be read in the Python interpreter via:
# >>> from microblog import app
# >>> app.config['SECRET_KEY']

from app import routes # P.5 At the bottom, to prevent 'circular imports'. # The `routes` refers to the `routes.py`-file.


