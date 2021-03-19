# P.25 User Login Form

from flask_wtf import FlaskForm         # Most Flask extensions use a `flask_`-naming convention # wtf_forms is pronounces as 'Witty Forms`

from wtforms import StringField
from wtforms import PasswordField
from wtforms import BooleanField
from wtforms import SubmitField

from wtforms.validators import DataRequired
from wtforms.validators import Email # P.60
from wtforms.validators import EqualTo # P.60
from wtforms.validators import ValidationError

from app.models import User


class LoginForm(FlaskForm): 
    username = StringField('Username', validators=[DataRequired()]) # The first argument 'Uername' will be the `.label`
    password = StringField('Password', validators=[DataRequired()]) # Don't forget the (), otherwise the error might be "TypeError: <class 'wtforms.validators.DataRequired'> is not a valid validator because it is a class, it should be an instance"
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign in') # The argument is the label that will be displayed in the button.

class RegistrationForm(FlaskForm): # P.60
    username = StringField('Username', validators=[DataRequired()]) # The first argument 'Uername' will be the `.label`
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeast Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username): # P.61 In wittyforms you can make these own checks
        user = User.query.filter_by(username=username.data).first() # Hierboven moet de `User`, nog geimporteerd worden.
        if user is not None:
            raise ValidationError('Please u a different username.')
        
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first() # pip install email_validator
        if user is not None:
            raise ValidationError('Please use a different email address.')
