import sqlite3

conn = sqlite3.connect('example.db') #creates db set to variable conn
print("Opened database SuccessfullY")
#creating a table commands

conn.execute('''CREATE TABLE COMPANY2(
    ID INT PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL,
    AGE INT NOT NULL,
    ADDRESS CHAR(50),
    SALARY REAL);''')
# NOTICE THE TRPLLE QUOTES #space twice italeta command
print("Table Created Successfully")
conn.close()
#kuweka rows