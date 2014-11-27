#------------------------------------------------------------------------------#
# Author: Fred Buchanan
# Name: database/__init__.py
# Project: messagner
# Disciption: Database controll fuctionality
#------------------------------------------------------------------------------#

#Imports------------------------------------------------------------------------
import sqlite3
#from messanger import app
from flask import g

#Global Deleratons--------------------------------------------------------------


#Classes------------------------------------------------------------------------
def make_conversation(user1,user2):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO conversations ('user1','user2','log') VALUES (?, ?, 'Conversations Started... \n')", (user1,user2))
    conn.commit()
    conn.close()

def add(user1,user2,toadd):
    conn = sqlite3.connect('database.db')
    c =  conn.cursor()
    c.execute("SELECT log FROM conversations WHERE user1=? AND user2=?",(user1,user2))
    now = c.fetchone()
    c.execute("UPDATE conversations SET log=? WHERE user1=? AND user2=?",(now[0]+toadd,user1,user2))
    conn.commit()
    conn.close()

def get(user1,user2):
    conn = sqlite3.connect('database.db')
    c =  conn.cursor()
    c.execute("SELECT log FROM conversations WHERE user1=? AND user2=?",(user1,user2))
    out = c.fetchone()
    conn.close()
    return out[0]
#Functions----------------------------------------------------------------------

#Global-------------------------------------------------------------------------
if __name__ == '__main__':
    #make_conversation('foo','bar')
    #add('foo','bar','ADDED')
    print get('foo','bar')