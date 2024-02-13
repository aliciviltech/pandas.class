import mysql.connector as mysql

conn = mysql.connect(
    host = "localhost",
    user = "root",
    password = "12345",
    database = "python_class1"
)
conn.connect()
cur = conn.cursor()
cur.execute("select * from  empinfo")
DT = cur.fetchall()
print(DT[2][3])
for i in DT:
    print(i[1])
conn.close()