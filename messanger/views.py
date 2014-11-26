#------------------------------------------------------------------------------#
# Author: Fred Buchanan
# Name: views.py
# Project: messanger
# Disciption: Contains view functions for app.
#------------------------------------------------------------------------------#

#Imports------------------------------------------------------------------------
from flask import render_template
from messanger import app

#Global Deleratons--------------------------------------------------------------

#Functions----------------------------------------------------------------------
@app.route('/')
def index():
    return render_template('jiberish.html', conversations=['1','2','3'])


    

#Global-------------------------------------------------------------------------