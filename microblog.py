from app import app

# P.49 Onderstaande is om te importeren voor de `(venv) $ flask shell`
from app import db
from app.models import User, Post

@app.shell_context_processor # P.49, Decorator voor de `(venv) $ flask shell`, it is invoked when the `flask shell` command is issued.
def make_shell_context():
    return {'db': db, 'User': User, 'Post' : Post}

# (venv_microblog) microblog $ flask shell
# Python 3.7.3 (default, Jul 25 2020, 13:03:44) 
# [GCC 8.3.0] on linux
# App: app [development]
# Instance: /home/dion/git/py/flask/microblog/instance
# >>> User
# <class 'app.models.User'>
# >>> Post
# <class 'app.models.Post'>
# >>> 