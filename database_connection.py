import mysql.connector as mysql
db = mysql.connect(
    host="localhost",
    user="root",
    password="12345",
    database="python_class1"
)

def MyExeNonQuery(WriteSQL):
    db.connect()
    cur = db.cursor()
    cur.execute(WriteSQL)
    db.commit()
    db.close()

def MyReadData(ReadSQL):
    db.connect()
    cur = db.cursor()
    cur.execute(ReadSQL)
    DT = cur.fetchall()
    db.close()
    return DT
