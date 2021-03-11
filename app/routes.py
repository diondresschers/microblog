from flask import render_template
from flask import flash             # P.28 for Flask messages. 
from flask import redirect          # Redeirect when a form is succesfully entered, redirect to another page.

from app import app # The first `app`, is the `app`-directory. The second `app` is the `app` created in the `__init__.py`-file: `app = Flask(__name__)`.
from app.forms import LoginForm # De `app`, is de `app`-directory, de `.forms` is de `forms.py`-file en de `LoginForm` is de Class in die file
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

@app.route('/login', methods=['GET','POST']) # P.29, accept the 'GET' and the 'POST' methods for forms.
def login():
    form2 = LoginForm() # P.27 Deze moeten we daadwerkerlijk doorgeven!
    # Check if the form is submitted or not:
    if form2.validate_on_submit(): # This is a function from Witty-forms. If the Submit-button have been pushed, so when this is a POST in stead of a GET
        flash(f'Login requested for user {form2.username.data}, {form2.remember_me.data}') # P.29 The `data` is the data that came with the form that the user just added. When you call the flash() message this will be stored, but you also have to show them in the template!
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form2)