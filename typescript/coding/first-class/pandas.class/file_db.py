from md_mysql_file import MyExeNonQuery
from md_mysql_file import MyReaadData
# x = MyReaadData("select * from tbl_depart")
# print(x)
# print(MyReaadData("select * from tbl_depart"))
id = input("Enter ID : ")
details = input("Enter details : ")
a = MyExeNonQuery(f"insert into tbl_depart values({id}, '{details}')")
print(a)