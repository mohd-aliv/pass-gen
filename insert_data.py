#!/bin/usr/python3.08
with open("emp.csv","r") as file:
    for line in file:
        data={"empno": int(line[0]),"ename":line[1],"job":line[2],"mgr":int(line[3]),"hiredate":datetime.strptime(line[4],"%d-%b-%y").date(),"sal":int(line[5]),"comm": None if line[6] == "" else int(line[6]),"deptno":int(line[7]) }
       import mysql.connector
       conn = mysql.connector.connect(
            host="localhost",
            user="aliv",
            password="123456",
            database="mydb"
        )
       cursor = conn.cursor()
       cursor.execute(""" insert into emp values(%(empno)s,%(ename)s,%(job)s,%(mgr)s,%(hiredate)s,%(sal)s,%(comm)s,%(deptno)s) """,data)
