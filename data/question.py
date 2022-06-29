import csv
import random
import time
import datetime


with open("data\questions.csv") as fp:
    csvreader=csv.reader(fp)
    row=[x for x in csvreader]


#    chosquest=random.choices(row,k=10)
    chosquest=[]

    while len(chosquest)!=10:
        x=random.choice(row)
        if x not in chosquest:
            chosquest.append(x)
    random.shuffle(chosquest)

print(chosquest)

x=0
def countdown(h,m,s):
    total_sec=h*3600+m*60+s
    while total_sec>0:
        timer = datetime.timedelta(seconds = total_sec)
        global x
        x=print(timer, end="\r")
        time.sleep(1)
        total_sec -= 1

        