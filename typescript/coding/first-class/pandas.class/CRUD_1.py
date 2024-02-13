from database_connection import MyExeNonQuery
from database_connection import MyReadData
from tkinter import *

def MyCommand():
    str = (f"insert into temp (id, ename, salary) values({txt1.get()}, '{txt2.get()}' , {txt3.get()})")
    MyExeNonQuery(str)

win =Tk()
win.geometry("800x400")
win.title('My CURD App')
lbl1 = Label(text = 'Enter ID')
lbl2 = Label(text = 'Enter Name')
lbl3 = Label(text = 'Enter Salary')

lbl1.place(x=5, y=5)
lbl2.place(x=5,y=40)
lbl3.place(x=5,y=75)


txt1 = Entry(font=('Arial',15))
txt2 = Entry(font=('Arial',15))
txt3 = Entry(font=('Arial',15))

txt1.place(x=90,y=5)
txt2.place(x=90,y=40)
txt3.place(x=90,y=75)

btn1 = Button(text='Insert',font =('Arial',15),
              command = MyCommand)
btn1.place(x=110,y=120)

win.mainloop()