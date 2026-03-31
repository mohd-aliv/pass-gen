#!/usr/bin/python3.8
import mysql.connector

# Create connection
conn = mysql.connector.connect(
    host="localhost",       # Your MySQL host
    user="aliv",            # Your MySQL username
    password="123456",  # Your MySQL password
    database="mydb"   # Your database name
)

# Check connection
if conn.is_connected():
    print("Connected to MySQL successfully!")

# Create cursor
cursor = conn.cursor()
# Example queri
for i in range(1,5):
    cursor.execute("insert into data_table values('aliv',01,9149106668);")
    conn.commit()
# Close connection
cursor.close()
conn.close()
