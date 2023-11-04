from md_mysql_file import MyExeNonQuery
from md_mysql_file import MyReaadData

def MyInsert():
    DT = MyReaadData('Select Max(emp_code),0 from empinfo')
    i = DT[0][0]
    i = += 1
    eName = input('Enter Emplyee Name: ')
    eDPT = input('Enter Depart :')
    MyExeNonQuery(f"insert into empinfo (emp_code, emp_name, dpt_id) values ({i}), '{eName}', {eDPT}")

def MyUpdate():
    eName = ('Enter Emp Name : ')
    eDPT = ('Enter Emp Depart : ')
    eCode = ('Enter Emp Code : ')
    MyExeNonQuery(f"update empinfo set dpt_id = {eDPT} where")



while(True):
    print("1) Insert \2) Update \3) Delete, \4) Search by id \5) Search by Name \6) Execute ")
    x = input("Enter Number : ")
    if(x == 1):
    break
    elif(x == 2):
    MyInsert()

