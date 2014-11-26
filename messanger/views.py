#------------------------------------------------------------------------------#
# Author: Fred Buchanan
# Name: views.py
# Project: messanger
# Disciption: Contains view functions for app.
#------------------------------------------------------------------------------#

#Imports------------------------------------------------------------------------
from flask import render_template, request, redirect, url_for, session
from messanger import app

#Global Deleratons--------------------------------------------------------------
dummyConv=[{'to':1, 'log':"Lorem Ipsum"},{'to':2, 'log':"Lorem Ipsum"}]
#Functions----------------------------------------------------------------------
def do_the_login(username,password):
    return username


@app.route('/')
def index():
    return render_template('jiberish.html', conversations=dummyConv)

@app.route('/conv')
def conversations():
    return render_template('conversation.html', conversations=dummyConv)

@app.route('/accounts/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        session['username']=do_the_login(request.form['username'],request.form['password'])
        return redirect(url_for('index'))
    else:
        return render_template('login.html', conversations=dummyConv)
@app.route('/accounts/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('index'))
#Global-------------------------------------------------------------------------