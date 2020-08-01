# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 10:50:37 2020

@author: coola
"""

from flask import Flask,render_template,url_for,flash,redirect
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from forms import registration_form,login_form
from configure import Config
app=Flask(__name__)
app.config.from_object(Config)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
db=SQLAlchemy(app)
mess=[{'name':'arnab paul','dept':'ECE'},{'name':'farhaz alam','dept':'CSE'},{'name':'dhiman paul','dept':'ECE'},{'name':'debranjan poddar','dept':'ECE'},{'name':'shuvam hazra','dept':'ECE'}
     ]
class user(db.Model):
    id=db.Column(db.Integer,unique=True,nullable=False,primary_key=True)
    username=db.Column(db.String,nullable=False)
    email=db.Column(db.String,unique=True,nullable=False)
    profile_pic=db.Column(db.String,unique=True,nullable=False,default='deafualt.jpg')
    password=db.Column(db.String,nullable=False)
    posts=db.relationship('post',backref='author',lazy=True)
    def __repr__(self):
        return f"user({self.username},{self.email},{self.profile_pic})"
class post(db.Model):
    post_id=db.Column(db.Integer,unique=True,nullable=False,primary_key=True)
    post_date=db.Column(db.DateTime,default=datetime.utcnow)
    content=db.Column(db.String,nullable=False)
    user_id=db.Column(db.String,db.ForeignKey('user.id'),nullable=False)
    def __repr__(self): 
        return f"{post.post_id} is posted at {post.content}"
    
@app.route('/')
def info():
    return render_template('layout.html',mess=mess)
@app.route('/Hello/<username>')
def show_user_profile(username):
    return 'Hello User %s' % username
@app.route('/home')
def home_page():
    return "this is a blog page.you can post here."
@app.route("/register",methods=['GET','POST'])
def register():
    form=registration_form()
    if form.validate_on_submit():       
        flash(f'{form.username.data} login successful!!','success')
        return redirect(url_for('home_page'))
               
    return render_template('register.html',title='register',form=form)
@app.route("/login",methods=['GET','POST'])
def login():
    form = login_form()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home_page'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

