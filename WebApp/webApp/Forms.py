'''
Created on Aug 2, 2019

@author: latikamehra
'''

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    usrnm = StringField('Username', validators=[DataRequired()])
    pswrd = PasswordField('Password', validators=[DataRequired()])
    rmmbr_me = BooleanField('Remember Me')
    sbmt = SubmitField('Sign In')
