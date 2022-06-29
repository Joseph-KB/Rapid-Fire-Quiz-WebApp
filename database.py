import sqlite3

from colorama import Cursor

DBname='./database/users.db'

def CreateDBT():
    conn=sqlite3.connect(DBname)
    cursor=conn.cursor()
    query="""CREATE TABLE IF NOT EXISTS USERS(NAME CHAR(20)
    NOT NULL, AGE INT NOT NULL, PHONENUM INT PRIMARY KEY NOT NULL)
    """
    cursor.execute(query)
    conn.commit()
    conn.close()

def AddUser(data):
    name=data["fname"].lower()
    age=int(data["age"])
    phonenum=int(data['phonenum'])

    conn=sqlite3.connect(DBname)
    query=f'''INSERT INTO USERS(NAME,AGE,PHONENUM)
     VALUES('{name}',{age},{phonenum})
    '''
    conn.execute(query)
    conn.commit()
    conn.close()

def ShowAllUsers():
    conn=sqlite3.connect(DBname)
    cursor=conn.execute("SELECT * FROM USERS ORDER BY AGE ASC")
    userdetail=cursor.fetchall()
    conn.commit()
    conn.close()
    return userdetail

def DeleteAll():
    conn=sqlite3.connect(DBname)
    cursor=conn.execute("DELETE FROM USERS")
    conn.commit()
    conn.close()


###########     SCOre To be added To the database
#########
##########
#############
########