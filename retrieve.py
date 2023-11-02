import sqlite3

conn = sqlite3.connect('example.db')
print("Opened DB Successfully")

cursor = conn.execute("SELECT id, name, age, address, salary from COMPANY2") #STORED BY A

for row in cursor:
    print("ID =",row[0])
    print("NAME =",row[1])
    print("AGE =",row[2])
    print("ADDRESS =",row[3])
    print("SALARY =",row[4])

print("Mission Passed, Respek")
conn.close()


#for loop ensures kila index positiion iko printed