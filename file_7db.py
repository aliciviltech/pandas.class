import mysql.connector as mysql

conn = mysql.connect(
    host = "localhost",
    user = "root",
    password = "12345",
    database = "python_class1"
)

cur = conn.cursor()
# cur.execute("insert into tbl_depart values (5, 'Python Depart')")
# cur.execute("update tbl_depart set details = 'tset_depart' where id = 5 ")
cur.execute("delete from tbl_depart where id = 5")
conn.commit()
conn.close()