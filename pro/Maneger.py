from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector as mc
import tkinter.messagebox as mb
from tkcalendar import Calendar
from datetime import datetime

class Maneger:
    def __init__(self,bottomFrame):
        self.bottomFrame=bottomFrame
        self.ManegerFrame = Frame(self.bottomFrame, pady=10, padx=10)
        self.ManegerFrame.grid(row=1, column=2, sticky='senw', pady=5)
        self.img6 = Image.open('image/images-removebg-preview (1).png')
        self.img6.thumbnail((150, 150))
        self.new_img6 = ImageTk.PhotoImage(self.img6)

        self.imgLibrary = Label(self.ManegerFrame, image=self.new_img6, pady=10, padx=10)
        self.imgLibrary.pack()
        self.ButtonLibrary = Button(self.ManegerFrame, command=self.open_maneger, text="Manager",
                                    bg='#1b9ea4', fg='white', padx=10,
                                    pady=10, font=("tahoma", 10, 'bold'))
        self.ButtonLibrary.pack()
    def open_maneger(self):
        mn = maneger()
class maneger :
    def __init__(self):
        self.master = Toplevel()
        self.master.title("Add user")
        self.height = self.master.winfo_screenheight()
        self.width = self.master.winfo_screenwidth()
        self.master.geometry("600x600+400+150")
        self.img = Image.open("image/clipart2409514.png")
        self.img.thumbnail((200,200))
        self.new_img=ImageTk.PhotoImage(self.img)
        self.imglabel = Label(self.master , image=self.new_img)
        self.imglabel.pack()

        self.frameEnter = Frame(self.master, height=200 , width= 500 )
        self.frameEnter.pack()

        self.EntryUser = Entry(self.frameEnter , width=25, font=('Tahoma',12))
        self.EntryUser.grid(row=0 , column=1,pady=20)
        self.Entrypass = Entry(self.frameEnter , width=25, font=('Tahoma',12) , show='*')
        self.Entrypass.grid(row=1 , column=1 , pady=20 )

        self.UserLabel = Label(self.frameEnter , text="UserName :" , font=('Tahoma',12,'bold'))
        self.UserLabel.grid(row = 0 , column =0 )
        self.passLabel = Label(self.frameEnter, text="Password :", font=('Tahoma',12,'bold'))
        self.passLabel.grid(row=1 , column=0)

        self.Enter = Button(self.frameEnter,command=self.login1 , width=25 , text="Add user" , pady=10 ,bg='#1b9ea4')
        self.Enter.grid(row=2 , column=0 ,columnspan=2 ,sticky='snew',pady= 7 , padx=7)


    def login1(self):
        mydp = mc.connect(host='localhost',
                          user='root',
                          password='',
                          database="un")
        mycursor = mydp.cursor()
        try:
            sql = "select id from loginadmi where Username = '" + self.EntryUser.get() + "' and Password = '" + self.Entrypass.get() + "' "
            mycursor.execute(sql)
            id1 = mycursor.fetchone()
            if (id1[0] == 1):
                window = Toplevel()
                uni = Add_User(window)
                self.master.withdraw()
                mydp.close()
            else:
                mb.showerror("Error" ,"هذا ليس حساب المدير أحمد الخضر" , parent = self.master)
        except:
            mb.showerror("Error", "هذا ليس حساب المدير أحمد الخضر", parent = self.master)
class Add_User:
    def __init__(self ,window):
        self.master = window
        self.master.title("Add user")
        self.height = self.master.winfo_screenheight()
        self.width = self.master.winfo_screenwidth()
        self.master.geometry("600x600+400+150")
        self.img = Image.open("image/clipart2409514.png")
        self.img.thumbnail((200, 200))
        self.new_img = ImageTk.PhotoImage(self.img)
        self.imglabel = Label(self.master, image=self.new_img)
        self.imglabel.pack()
        self.frameEnter = Frame(self.master, height=200, width=500)
        self.frameEnter.pack()

        self.EntryUser1 = Entry(self.frameEnter, width=25, font=('Tahoma', 12))
        self.EntryUser1.grid(row=0, column=1, pady=20)
        self.Entrypass1 = Entry(self.frameEnter, width=25, font=('Tahoma', 12), show='*')
        self.Entrypass1.grid(row=1, column=1, pady=20)
        self.NameAdmin = Entry(self.frameEnter, width=25, font=('Tahoma', 12))
        self.NameAdmin.grid(row=2, column=1, pady=20)


        self.UserLabel = Label(self.frameEnter, text="UserName :", font=('Tahoma', 12, 'bold'))
        self.UserLabel.grid(row=0, column=0)
        self.passLabel = Label(self.frameEnter, text="Password :", font=('Tahoma', 12, 'bold'))
        self.passLabel.grid(row=1, column=0)
        self.NameLabel = Label(self.frameEnter, text="NameAdmin :", font=('Tahoma', 12, 'bold'))
        self.NameLabel.grid(row=2, column=0)


        self.Enter = Button(self.frameEnter, command=self.Log, width=25, text="Add user", pady=10, bg='#1b9ea4',activeforeground='white',activebackground='#750E21' , font=('tahoma',10,'bold'))
        self.Enter.grid(row=3, column=0, sticky='snew', pady=7, padx=7)
        self.Enter1 = Button(self.frameEnter, command=self.delete_user, width=25, text="delete user", pady=10, bg='#1b9ea4',activeforeground='white',activebackground='#750E21' , font=('tahoma',10,'bold'))
        self.Enter1.grid(row=3, column=1, sticky='snew', pady=7, padx=7)

        self.Enter.bind("<Enter>", self.on_enter)
        self.Enter.bind("<Leave>", self.on_leve)

        self.Enter1.bind("<Enter>", self.on_enter1)
        self.Enter1.bind("<Leave>", self.on_leve1)

    def on_enter(self , ev):
        self.Enter['background'] = '#213363'
    def on_leve(self , ev):
        self.Enter['background'] = '#1b9ea4'

    def on_enter1(self , ev):
        self.Enter1['background'] = '#213363'
    def on_leve1(self , ev):
        self.Enter1['background'] = '#1b9ea4'

    def Log(self):
        mydp = mc.connect(host='localhost',
                          user='root',
                          password='',
                          database="un")
        mycursor = mydp.cursor()
        sql = "insert into loginadmi(Username,Password ,NameAdmin) values (%s,%s,%s) "

        if (len( self.EntryUser1.get()) ==0 or len(self.EntryUser1.get()) ==0  or len(self.NameAdmin.get() ) ==0 ):
            mb.showerror('Error','يوجد حقول فارغة')
        else:
            sql1 = ("select id from loginadmi where Username = '" + self.EntryUser1.get() + "' and Password = '" + self.Entrypass1.get() + "' and NameAdmin = '" + self.NameAdmin.get() + "' ")
            mycursor.execute(sql1)
            qq= mycursor.fetchone()
            if qq == None:
                if self.NameAdmin.get().isalpha():
                    val = (self.EntryUser1.get(), self.Entrypass1.get(), self.NameAdmin.get())
                    mycursor.execute(sql,val)
                    mydp.commit()
                    mb.showinfo('Message',"تمت اضافة الحساب" , parent = self.master)
                    mydp.close()
                else:
                    mb.showerror('Error', 'الاسم غير صحيح' , parent = self.master)
                self.Reset1()
            else:
                mb.showerror('Error', 'الحساب موجود بالفعل' , parent = self.master)
                self.Reset1()
    def delete_user(self):
        mydp = mc.connect(host='localhost',
                          user='root',
                          password='',
                          database="un")
        mycursor = mydp.cursor()
        try:
            a = ("select id from loginadmi where Username = '"+self.EntryUser1.get()+"' and Password = '"+self.Entrypass1.get()+"' and NameAdmin = '"+self.NameAdmin.get()+"' ")
            mycursor.execute(a)
            mb1 = mycursor.fetchone()
            if mb1 != None:
                sql = ("delete from loginadmi  where Username = '"+self.EntryUser1.get()+"' and Password = '"+self.Entrypass1.get()+"' and NameAdmin = '"+self.NameAdmin.get()+"'")
                mycursor.execute(sql)
                mydp.commit()
                mb.showinfo('Message',"نم حذف الحساب" , parent =self.master )
                mydp.close()
            else:
                mb.showerror('Message', "الحساب غير موجود", parent=self.master)
            self.Reset1()
        except:
            mb.showerror('Message', "الحساب غير موجود", parent=self.master)
    def Reset1(self):
        self.EntryUser1.delete(0, 'end')
        self.Entrypass1.delete(0, 'end')
        self.NameAdmin.delete(0, 'end')




