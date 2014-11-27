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
db='database.db'

#Classes------------------------------------------------------------------------


def make_conversation(user1,user2):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute("INSERT INTO conversations ('user1','user2','log') VALUES (?, ?, 'Conversations Started... \n')", (user1,user2))
    conn.commit()
    conn.close()

def add(user1,user2,toadd):
    conn = sqlite3.connect(db)
    c =  conn.cursor()
    c.execute("SELECT log FROM conversations WHERE user1=? AND user2=?",(user1,user2))
    now = c.fetchone()
    c.execute("UPDATE conversations SET log=? WHERE user1=? AND user2=?",(now[0]+toadd,user1,user2))
    conn.commit()
    conn.close()

def get(user1,user2):
    conn = sqlite3.connect(db)
    c =  conn.cursor()
    c.execute("SELECT log FROM conversations WHERE user1=? AND user2=?",(user1,user2))
    out = c.fetchone()
    conn.close()
    return out[0]

def getMyConversations(user):
    conn=sqlite3.connect(db)
    c = conn.cursor()
    conversations=[]
    for row in c.execute("SELECT * FROM conversations WHERE user1=?",[user]):
        this={'me':row[1], 'to':row[2], 'log':row[3]}
        conversations.append(this)
    for row in c.execute("SELECT * FROM conversations WHERE user2=?",[user]):
        this={'me':row[2],'to':row[1], 'log':row[3]}
        conversations.append(this)
    conn.commit()
    conn.close()
    return conversations
    
#Functions----------------------------------------------------------------------

#Global-------------------------------------------------------------------------
if __name__ == '__main__':
    #make_conversation('foo','bar')
    #make_conversation('bob','foo')
    #add('foo','bar','ADDED')
    #print get('foo','bar')
    print getMyConversations('foo')