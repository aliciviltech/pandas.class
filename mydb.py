import mysql.connector
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "12345",
    database = "python_class1"
)
cur = db.cursor()
a = cur.execute("select dpt_id from empinfo")
a = cur.fetchall()
for i in a:
    print(i)
cur.close()
db.close()