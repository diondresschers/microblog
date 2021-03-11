from flask import render_template
from app import app # The first `app`, is the `app`-directory. The second `app` is the `app` created in the `__init__.py`-file: `app = Flask(__name__)`.

@app.route('/') # P.6 - These are 'decorators'.
@app.route('/index') # P.6 - You can chain decorators.
def index():
    user2 = {                # P12. Dummy-data.
        "username":"Dion", 
    }
    posts2 = [ # This is a Python3 'list', a tuple will be within paranthesis `()``.
        {
            'author' : {'username' : 'Mimi'},
            'body' : "Oh it's such a perfect day!",
        },
        {
            'author' : {'username': "Peter"}, 
            'body' : "Je suis, Jackshon...",
        },   
    ]
    return render_template('index.html', user=user2, title="Homepagina", posts=posts2) # The first user is the `user` is the `user` in the template, the second is the `user`-variable defined above.
