# P.25 User Login Form

from flask_wtf import FlaskForm         # Most Flask extensions use a `flask_`-naming convention

from wtforms import StringField
from wtforms import PasswordField
from wtforms import BooleanField
from wtforms import SubmitField

from wtforms.validators import DataRequired

class LoginForm(Flaskform):
    username = StringField('Username', validators=[DataRequired])
    password = StringField('Password', validators=[DataRequired])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign in')
