
from flask import *
import database as db
from data import question as qb
import time
import datetime


app=Flask(__name__)
#print(type(app),app)
#print(type(__name__),__name__)
usertup=()


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/usercredentials')
def usercredentials():
    return render_template('usercredentials.html')


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
#            print(result)
#            resultx=result['fname'],result['age'],result['phonenum']
#            print(resultx)
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
#    print(usertup)
    qbank=qb.chosquest 
    
    return render_template('gamepage.html',username=user,data=qbank)

if __name__ == '__main__':
    db.CreateDBT()
    app.run(debug=True)