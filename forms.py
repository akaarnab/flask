# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 15:17:57 2020

@author: coola
"""

from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,BooleanField
from wtforms.validators import EqualTo,DataRequired,Length

class registration_form(FlaskForm):
    username=StringField('username',validators=[DataRequired(),Length(min=2,max=20)])
    email=StringField('email',validators=[DataRequired()])
    password=PasswordField('password',validators=[DataRequired(),Length(min=2,max=20)])
    confirm_password=PasswordField('confirm_password',validators=[DataRequired(),EqualTo(password)])
    submit=SubmitField('sign up')

class login_form(FlaskForm):
    email=StringField('email',validators=[DataRequired()])
    password=PasswordField('password',validators=[DataRequired(),Length(min=2,max=20)])
    remember_me=BooleanField('remember')
    submit=SubmitField('log in')