from flask import Flask

app = Flask(__name__)

from app import routes # At the bottom, to prevent 'circular imports'. # The `routes` refers to the `routes.py`-file.

