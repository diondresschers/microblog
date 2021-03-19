from flask import render_template
from flask import flash             # P.28 for Flask messages. 
from flask import redirect          # Redeirect when a form is succesfully entered, redirect to another page.
from flask import url_for
from flask import request

from werkzeug.urls import url_parse

from flask_login import login_user
from flask_login import current_user
from flask_login import logout_user
from flask_login import login_required

from app import app # The first `app`, is the `app`-directory. The second `app` is the `app` created in the `__init__.py`-file: `app = Flask(__name__)`.
from app import db # P.63, to make sure the user is not yet in the db

from app.forms import LoginForm # De `app`, is de `app`-directory, de `.forms` is de `forms.py`-file en de `LoginForm` is de Class in die file
from app.forms import RegistrationForm # P.63
from app.models import User 

@app.route('/') # P.6 - These are 'decorators'.
@app.route('/index') # P.6 - You can chain decorators.
@login_required
def index():
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
    return render_template('index.html', title="Homepagina", posts=posts2) # The first user is the `user` is the `user` in the template, the second is the `user`-variable defined above.

@app.route('/login', methods=['GET','POST']) # P.29, accept the 'GET' and the 'POST' methods for forms.
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm() # P.27 Deze moeten we daadwerkerlijk doorgeven!
    # Check if the form is submitted or not:
    if form.validate_on_submit(): # This is a function from Witty-forms. If the Submit-button have been pushed, so when this is a POST in stead of a GET
        user = User.query.filter_by(username=form.username.data).first() # P.55
        if user is None or not user.check_password(form.password.data): # This is an invalid try
            flask('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data) # P.55 This is from flask-login, to login the user
        next_page = request.args.get('next')   #P.58, this is the end of a URL after the `?`.
        if not next_page or url_parse(next_page).netloc != '':  # P.58  -The `netloc` is the domain + toplevel domain. This should be relative, so empty. This is not set, if this is set to example `example.com`, than there might be problem.
            next_page = url_for('index')
        return redirect(next_page)

        # flash(f'Login requested for user {form.username.data}, {form.remember_me.data}') # P.29 The `data` is the data that came with the form that the user just added. When you call the flash() message this will be stored, but you also have to show them in the template!
        return redirect(url_for('index')) # The `url_for`, needs the function name, not the actual URL. # You need to import this function as well.
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user() # P57
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST']) # P.63
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

