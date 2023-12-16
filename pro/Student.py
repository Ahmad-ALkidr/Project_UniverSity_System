from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
class Student:
    def __init__(self, centerFrame):
        self.centerFrame = centerFrame
        self.studentFrame = Frame(self.centerFrame, pady=10, padx=10)
        self.studentFrame.grid(row=0, column=1, sticky='senw', pady=5)
        self.img1 = Image.open('image/2-removebg-preview.png')
        self.img1.thumbnail((200, 200))
        self.new_img1 = ImageTk.PhotoImage(self.img1)

        self.imgStudent = Label(self.studentFrame, image=self.new_img1, pady=10, padx=10)
        self.imgStudent.pack()
        self.ButtonStudent = Button(self.studentFrame, command=self.openstudentwindo, text="Student Management",
                                    bg='#1b9ea4', fg='white', padx=10,
                                    pady=10, font=("tahoma", 10, 'bold'))
        self.ButtonStudent.pack()

    def openstudentwindo(self):
        stdw=StudentWindow()

class StudentWindow:
    def __init__(self):
        self.master = Toplevel()
        self.master.title('Student Management System')
        self.master.geometry("1200x600+0+0")
        # -------------------------------------------------------#
        #  side  تسمح خاصية باخذ العنصر لاقصى اليسار للوسط
        self.frameleft = Frame(self.master, width=400)
        self.frameleft.pack(side=LEFT, fill=Y)
        # -------------------------------------------------------#
        self.FirstName = Label(self.frameleft , text='FirstName',font=('tahoma',10,'bold'))
        self.FirstName.place(x=10,y=20)
        self.LastName = Label(self.frameleft, text='LastName',font=('tahoma',10,'bold'))
        self.LastName.place(x=10, y=60)
        self.CIN = Label(self.frameleft, text='CIN',font=('tahoma',10,'bold'))
        self.CIN.place(x=10, y=100)
        self.Email = Label(self.frameleft, text='Email',font=('tahoma',10,'bold'))
        self.Email.place(x=10, y=140)


        self.FirstName = Entry(self.frameleft)
        self.FirstName.place(x=100, y=20,width=150,height=30)
        self.LastName = Entry(self.frameleft)
        self.LastName.place(x=100, y=60,width=150,height=30)
        self.CIN = Entry(self.frameleft)
        self.CIN.place(x=100, y=100,width=150,height=30)
        self.Email = Entry(self.frameleft)
        self.Email.place(x=100, y=140,width=150,height=30)


        self.add = Button(self.frameleft , text="add",bg='#1b9ea4')
        self.add.place(x=30,y=300,width=60,height=40)
        self.Update = Button(self.frameleft, text="Update",bg='#1b9ea4')
        self.Update.place(x=120, y=300,width=60,height=40)
        self.Delete = Button(self.frameleft, text="Delete",bg='#1b9ea4')
        self.Delete.place(x=210, y=300,width=60,height=40)

        # ------------Start right top -----------------------#
        self.frameright = Frame(self.master, width=800, bg='blue')
        self.frameright.pack(side=LEFT, fill=BOTH)
        # ------------Start right top -----------------------#
        self.framerighttop=Frame(self.frameright , height=50 , pady=5,padx=5)
        self.framerighttop.pack(fill=X)

        self.searchStudent = Entry(self.framerighttop,fg='#4F4F4F',font=('tahoma',12,'bold'),width=110)
        self.searchStudent.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
        self.ButtonSearch = Button(self.framerighttop,text="Search",fg='#4F4F4F',font=('tahoma',12,'bold'),width=50)
        self.ButtonSearch.grid(row=0,column=1,sticky='nsew',pady=10,padx=10)

        self.framerighttop.grid_columnconfigure(0, weight=1)
        self.framerighttop.grid_columnconfigure(1, weight=1)

        # -------------------------- Frame Top View --------------------------#
        self.frameview = Frame(self.frameright,bg='red')
        self.frameview.pack(fill=BOTH)

        self.table = ttk.Treeview(self.frameview,columns=("ID","FirstName","LastName","CIN","Email"),show='headings')
        self.table.pack(fill=BOTH )

        self.table.heading("ID",text="ID")
        self.table.heading("FirstName", text="FirstName")
        self.table.heading("LastName", text="LastName")
        self.table.heading("CIN", text="CIN")
        self.table.heading("Email", text="Email")

        self.table.column("ID",anchor=W)
        self.table.column("FirstName",anchor=W)
        self.table.column("LastName",anchor=W)
        self.table.column("CIN",anchor=W)
        self.table.column("Email",anchor=W)