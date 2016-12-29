import mysql.connector

conn = mysql.connector.connect(
    user ='root',
    password = 'myfirstsql',
    host = '127.0.0.1',
    database = 'demo'
    )

cur = conn.cursor()

query = "SELECT id, name FROM student"

cur.execute(query)

for (studentId, studentName) in cur:
    print "%s. %s" % (studentId, studentName)
