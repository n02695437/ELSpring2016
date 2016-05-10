#!/usr/bin/python
import os
import time
from datetime import datetime
import sqlite3 as mydb
import sys

def readTemp():
    tempfile = open("/sys/bus/w1/devices/28-000007892847/w1_slave")
    tempfile2 = open("/sys/bus/w1/devices/28-80000003aaf1/w1_slave")
    tempfile_text = tempfile.read()
    tempfile2_text = tempfile2.read()
    currentTime = time.strftime('%x %X %Z')
    tempfile.close()
    tempfile2.close()
    tempC = float(tempfile_text.split("\n")[1].split("t=")[1])/1000
    tempC2 = float(tempfile2_text.split("\n")[1].split("t=")[1])/1000
    tempF = tempC*9.0/5.0+32.0
    tempF2 = tempC2*9.0/5.0+32.0
    return [ currentTime, tempC, tempF, tempC2, tempF2]
z=readTemp()
con = mydb.connect('/home/pi/Desktop/Final/Final.db')
try:
    with con:
        cur=con.cursor()
        cur.execute('INSERT INTO DT(DateTime, TempC1m, TempF1m, TempC2m, TempF2m) Values (?,?,?,?,?)', (z[0],z[1],z[2],z[3],z[4]))
        con.commit
except:
    cur = con.cursor()
    cur.execute('CREATE TABLE DT(DateTime, TempC1m, TempF1m, TempC2m, TempF2m)')
    cur.execute('INSERT INTO DT(DateTime, TempC1m, TempF1m,TempC2m, TempF2m) Values(?,?,?,?,?)', (z[0],z[1],z[2],z[3],z[4]))
    con.commit()
