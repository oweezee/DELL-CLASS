import sqlite3
conn = sqlite3.connect('example.db')
print("Opened Successfully")
conn.execute("INSERT INTO COMPANY2(ID, NAME,AGE, ADDRESS, SALARY)\
             VALUES(1, 'EMOBILIS', 7, 'WESTLANDS',25000.00)");

conn.execute("INSERT INTO COMPANY2(ID, NAME,AGE, ADDRESS, SALARY)\
             VALUES(2, 'SAFARICOM', 7, 'WESTLANDS',25000.00)");

conn.execute("INSERT INTO COMPANY2(ID, NAME,AGE, ADDRESS, SALARY)\
             VALUES(3, 'MICROSOFT', 7, 'WESTLANDS',25000.00)");

conn.execute("INSERT INTO COMPANY2(ID, NAME,AGE, ADDRESS, SALARY)\
             VALUES(4, 'ORACLE', 7, 'WESTLANDS',25000.00)");

conn.execute("INSERT INTO COMPANY2(ID, NAME,AGE, ADDRESS, SALARY)\
             VALUES(5, 'NAIVAS', 7, 'WESTLANDS',25000.00)");

conn.commit()
print("Records created successfully")
conn.close()