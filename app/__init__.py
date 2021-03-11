from flask import Flask # We only import Flask, not the whole flask.

app = Flask(__name__) # P.6 We create an instance. # With this, it can find out the location on disk, so it can locate other files and directories.

from app import routes # P.5 At the bottom, to prevent 'circular imports'. # The `routes` refers to the `routes.py`-file.

