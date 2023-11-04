import mysql.connector as mysql
conn = mysql.connect(
    host = "localhost",
    user = "root",
    password = "12345",
    database = "python_class1"
)
def MyExeNonQuery(WriteSQL):
    conn.connect()
    cur = conn.cursor()
    cur.execute(WriteSQL)
    conn.commit()
    conn.close()

def MyReaadData(ReadSQL):
    conn.connect()
    cur = conn.cursor()
    cur.execute(ReadSQL)
    DT = cur.fetchall()
    conn.close()
    return DT