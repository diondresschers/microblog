# P.25 User Login Form

from flask_wtf import FlaskForm         # Most Flask extensions use a `flask_`-naming convention # wtf_forms is pronounces as 'Witty Forms`

from wtforms import StringField
from wtforms import PasswordField
from wtforms import BooleanField
from wtforms import SubmitField

from wtforms.validators import DataRequired

class LoginForm(FlaskForm): 
    username = StringField('Username', validators=[DataRequired()]) # The first argument 'Uername' will be the `.label`
    password = StringField('Password', validators=[DataRequired()]) # Don't forget the (), otherwise the error might be "TypeError: <class 'wtforms.validators.DataRequired'> is not a valid validator because it is a class, it should be an instance"
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign in') # The argument is the label that will be displayed in the button.

