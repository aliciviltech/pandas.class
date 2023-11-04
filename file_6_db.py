import mysql.connector as mysql

conn = mysql.connect(
    host = "192.168.1.35",
    user = "root",
    password = "accessme",
    database = "python_class1"
)
# conn.connect()
cur = conn.cursor()
a = cur.execute("select * from empinfo")
a = cur.fetchall()
for i in a:
    print(i)
cur.close()
conn.close()