from datetime import datetime
import sqlite3 as mydb
import sys

con = mydb.connect('testTime.db')
#Reads the date and time and returns them in that order
def logTime():
    i = datetime.now()
    xdate =  i.strftime('%Y-%m-%d')
    xtime =  i.strftime('%H-%M-%S')
    return xdate, xtime
z = logTime()
try:
    with con:
        cur = con.cursor()
        #cur.execute('INSERT INTO DT(Date, Time) Values (?,?)', (z[0],z[1]))
        cur.execute('select * from DT')
        data = cur.fetchone()
        print (data)
        con.commit()
except:
    with con:
        cur=con.sursor()
        cur.execute('CREATE TABLE DT(Date, Time)')
        cur.commit()
