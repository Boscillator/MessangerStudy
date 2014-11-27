#------------------------------------------------------------------------------#
# Author: Fred Buchanan
# Name: views.py
# Project: messanger
# Disciption: Contains view functions for app.
#------------------------------------------------------------------------------#

#Imports------------------------------------------------------------------------
import database
from flask import render_template, request, redirect, url_for, session, flash, g
from messanger import app

#Global Deleratons--------------------------------------------------------------

#Functions----------------------------------------------------------------------
def getConversations():
    with app.app_context():
        try:
            return database.getMyConversations(session['username'])
        except KeyError:
            return []

def do_the_login(username,password):
    return username

#Main Views
@app.route('/')
def index():
    return render_template('home.html', conversations=getConversations())

@app.route('/conv')
def conversations():
    return render_template('conversation.html', conversations=getConversations())
#account views
@app.route('/accounts/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        flash('Logged In')
        session['username']=do_the_login(request.form['username'],request.form['password'])
        return redirect(url_for('index'))
    else:   
        return render_template('login.html', conversations=getConversations())
@app.route('/accounts/logout')
def logout():
    flash('Logged Out')
    session.pop('username',None)
    return redirect(url_for('index'))


#backend views
@app.route('/backend/make', methods=['POST'])
def makeConversation():
    if session['username']:
        database.make_conversation(session['username'],request.form[sendTo])
        flash('Conversation to '+request.form[sendTo]+' started!')
        return redirect(url_for('index'))
    else:
        flash('Please log in')
        return redirect(url_for('index'))




#Global-------------------------------------------------------------------------


