from tkinter import *
from md_mysql_file import *

def MyCommand():
    print(chk_status1.get())
    print(chk_status2.get())
    print(chk_status3.get())
    print(rd_s1.get())
    print(rd_s2.get())
    # print('Hello Submit')
    # print(txt1.get())
    # lbl1.configure(text = txt1.get(), foreground= 'green')
    # txt1.delete(first:0,END)
    # txt1.insert(0, 'TEsT Data')
    # txt1.insert (index:0, txt2.get())
    str = (f"insert into empinfo (emp_name,salary, dpt_id) values('{txt1.get()}', '{txt2.get()}', {txt3.get()}) ")
    # print
    MyExeNonQuery(str)


win = Tk()
win.geometry('800x400')
win.title('Hello Tkinter')
lbl1 = Label(text='Enter Employee Name',
            font =('Arial',20), foreground= 'red', background= 'yellow', width=22,
            # height=20,
            anchor='nw'
            )


lbl2 = Label(text='Enter Employee Salary',
            font =('Arial',20), foreground= 'red', background= 'yellow', width=22,
            # height=20,
            anchor='nw'
            )


lbl3 = Label(text='Enter Employee Department',
            font =('Arial',20), foreground= 'red', background= 'yellow', width=22,
            # height=20,
            anchor='nw'
            )

lbl1.place(x=50,y=50)
lbl2.place(x=50,y=100)
lbl3.place(x=50,y=150)

txt1 = Entry (font=('Arial',20))
txt2 = Entry (font=('Arial',20))
txt3 = Entry (font=('Arial',20))

txt1.place(x=450,y=50)
txt2.place(x=450,y=100)
txt3.place(x=450,y=150)

btn1 = Button(
    command=MyCommand,
    # print(lbl1)
    text='Insert',font =('Arial',15))
btn1.place(x=400,y=200)

rd_s1 = IntVar()

rd_s2 = IntVar()

rd1 = Radiobutton(value=1, text="Python", font=('Arial',20), variable=rd_s1)
rd1.place(x=10, y=350)

rd2 = Radiobutton(value=2, text="Java", font=('Arial',20), variable=rd_s1)
rd2.place(x=10, y=310)

rd3 = Radiobutton(value=3, text="C#", font=('Arial',20), variable=rd_s1)
rd3.place(x=10, y=450)


rd1 = Radiobutton(value=4, text="Morning", font=('Arial',20), variable=rd_s2)
rd1.place(x=10, y=400)

rd2 = Radiobutton(value=5, text="Evening", font=('Arial',20), variable=rd_s2)
rd2.place(x=10, y=400)

rd3 = Radiobutton(value=6, text="Night", font=('Arial',20), variable=rd_s2)
rd3.place(x=300, y=400)



chk1 = Checkbutton (text = "Check1",font('Arial',20),variable =chk_status1)
chk1.place(x=250,y=400)

chk2 = Checkbutton (text = "Check2", font('Arial',20), variable =chk_status2)
chk2.place(x=200,y=450)

chk3 = Checkbutton (text = "Check3", font('Arial',20), variable =chk_status3)
chk3.place(x=350,y=450)

tab_obj = ttk.Notbook(width=300, height=250)
tab1= ttk.Fram()
tab_obj.add(tab1,text='My Tab1')
tab2= ttk.Fram()
tab_obj.add(tab2,text='My Tab2')
tab2= ttk.Fram()
tab_obj.place(x=10, y=350)




win.mainloop()