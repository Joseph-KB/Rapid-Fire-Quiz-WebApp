# In command line run pip install Flask 
# All functions and methods are called 
# from the Flask library.
from flask import *

# Below python script in the root folder named
# database is called... Codes in that is writen using
# SQLite3 for database creation and updation CRUD
import database as db

# For Question generation question.py is created in 
# data folder. 
from data import question as qb



app=Flask(__name__)

# The below decorater routes the server to the
#respective page, and functions below it will be 
# executed.
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


# Respective html pages are rendered/loaded
@app.route('/usercredentials')
def usercredentials():
    return render_template('usercredentials.html')


# When any post or get command is recieved from the
# client side we create a user and the user details
# are stored into the database.
@app.route('/insertusercred',methods=["post","get"])
def insertusercred():
    message='User Created'
    print(request.method)
    
    if request.method=='POST':
        result=request.form
        print(result)
        try:
            db.AddUser(result)
            global usertup
            usertup=result
        except:
            message="Boys Time To debug!! Error entering user details."
            return render_template('errorpage.html',insertmessage=message)
    return render_template('welcome.html',username=result['fname'].upper())



@app.route('/allusers',methods=["POST","GET"])
def allusers():
    userdetails=db.ShowAllUsers()
    if request.method=='POST':
        print(request.form)
        db.DeleteAll()
        return render_template('allusers.html')
    else:
        pass
    return render_template('allusers.html',data=userdetails)



@app.route('/gamepage',methods=['post','get'])
def gamepage():
    user=usertup.get('fname',None)
    qbank=qb.chosquest 
    return render_template('gamepage.html',username=user,data=qbank)
    


# Our web app will be only initialised afterwards
if __name__ == '__main__':
    db.CreateDBT()
    app.run(debug=True)