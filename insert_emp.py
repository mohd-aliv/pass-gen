#!/usr/bin/python3.8
import mysql.connector
from datetime import datetime
conn = mysql.connector.connect(
    host="localhost",
    user="aliv",     
    password="123456",
    database="mydb" 
)
cursor = conn.cursor()
with open("emp.csv","r") as file:
    for line in file:
        line=line.strip().split(',')
        data=(int(line[0]),line[1],line[2],None if line[3]=="" else int(line[3]),datetime.strptime(line[4],"%d-%b-%y").date(),int(line[5]), None if line[6] == "" else int(line[6]),int(line[7]) )
        cursor.execute("insert into emp values(%s,%s,%s,%s,%s,%s,%s,%s)",data)
conn.commit()
cursor.close()
conn.close()
