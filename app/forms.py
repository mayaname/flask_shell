"""
Program: Forms
Author: Maya Name
Creation Date: 03/05/2025
Revision Date: 
Description: Forms for Flask application


Revisions:

"""


from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import InputRequired
from app.extensions import db


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Sign In')



