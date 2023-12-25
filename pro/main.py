from tkinter import *

#import keyboard

import Student as s
import Staff as st
import Subject as l
import Exam as e
import Maneger as mn
from PIL import Image,ImageTk
import mysql.connector as mc
import tkinter.messagebox as mb
import webbrowser as web


import Colleges as i
class University():
    def __init__(self, window):
        self.master = window
        self.master.title("University Management System ")
        self.height = self.master.winfo_screenheight()
        self.width = self.master.winfo_screenwidth()
        self.master.geometry("{w}x{h}+0+0".format(w=self.width, h=self.height))
        self.master.state('zoomed')
        # ---------- Frame Top Start Here ----------------------------
        self.frametop = Frame(self.master,bg="#1b9ea4",height=150)
        self.frametop.pack(fill=X)
        self.sms = Label(self.frametop,text="University Management System",bg='#1b9ea4',fg='white',font=("tahoma",50),pady=50)
        self.sms.pack()
        self.img =Image.open('image/login-icon-logout-icon-blue-azure-text-electric-blue-line-arrow-material-property-png-clipart-removebg-preview.png')
        self.img.thumbnail((50,50))
        self.new_im = ImageTk.PhotoImage(self.img)
        self.buttonlogout = Button(self.frametop , text="Logout" , command=self.logout ,image=self.new_im)
        self.buttonlogout.place(y=120, x=1450)
        # ---------- Frame Top End Here ----------------------------

        # #---------- Frame Center Start Here -----------------------##
        self.centerFrame = Frame(self.master)
        self.centerFrame.pack(fill=X)

        # ---------- Frame University info ----------------------------
        info = i.colleges(self.centerFrame)
        # ---------- Frame Student info ----------------------------
        std = s.Student(self.centerFrame)
        # ---------- Frame Staff  ----------------------------
        stf = st.Staff(self.centerFrame)
        # # ---------- Frame Top End Here ----------------------------##
        self.centerFrame.grid_columnconfigure(0,weight=1)
        self.centerFrame.grid_columnconfigure(1, weight=1)
        self.centerFrame.grid_columnconfigure(2, weight=1)
        # #---------- Frame Bottom Start Here -----------------------##
        self.bottomFrame = Frame(self.master, height=200)
        self.bottomFrame.pack(fill=X)
        # ---------- Frame Library Here ----------------------------#
        li = l.Library(self.bottomFrame)
        # ---------- Frame exam Here -------------------------------#
        ex = e.Exam(self.bottomFrame)
        # #---------- Frame Bottom End Here -------------------------##
        mn1 = mn.Maneger(self.bottomFrame)

        self.bottomFrame.grid_columnconfigure(0, weight=1)
        self.bottomFrame.grid_columnconfigure(1, weight=1)
        self.bottomFrame.grid_columnconfigure(2, weight=1)
    def logout(self):
        self.master.destroy()



class Login:
    def __init__(self,window):
        self.master = window
        self.master.title("Login System ")
        self.height = self.master.winfo_screenheight()
        self.width = self.master.winfo_screenwidth()
        self.master.geometry("600x600+400+150")
        self.master.resizable(width=False , height=False)
        self.laF = LabelFrame(self.master,width=550,height=500,text='(❁´◡`❁)-Login System-(❁´◡`❁)',font=('Tahoma',12,'bold'))
        self.laF.pack()
        self.img = Image.open("image/clipart2409514.png")
        self.img.thumbnail((200,200))
        self.new_img=ImageTk.PhotoImage(self.img)
        self.imglabel = Label(self.laF , image=self.new_img)
        self.imglabel.pack()

        self.frameEnter = Frame(self.laF, height=200 , width= 500 )
        self.frameEnter.pack()

        self.EntryUser = Entry(self.frameEnter , width=23, font=('Tahoma',12))
        self.EntryUser.grid(row=0 , column=1,pady=10)
        self.Entrypass = Entry(self.frameEnter , width=23, font=('Tahoma',12) , show='*')
        self.Entrypass.grid(row=1 , column=1 , pady=15 )

        self.UserLabel = Label(self.frameEnter , text="UserName :" , font=('Tahoma',12,'bold'))
        self.UserLabel.grid(row = 0 , column =0 )
        self.passLabel = Label(self.frameEnter, text="Password :", font=('Tahoma',12,'bold'))
        self.passLabel.grid(row=1 , column=0)

        self.ch1 = IntVar()

        self.ch = Checkbutton(self.master, text='Forget Password !', font=('Courier', 15, 'bold'), bg='whitesmoke',variable=self.ch1)
        self.ch.place(x=140 , y=340)

        self.Enter = Button(self.frameEnter,command=self.login1 , width=25 , text="Login", pady=10 ,bg='#1b9ea4',activeforeground='white',activebackground='#750E21' , font=('tahoma',10,'bold'),cursor='mouse')
        self.Enter.grid(row=3 , column=0, sticky='snew',pady=100 , padx=7)
        self.mess = Button(self.frameEnter, command=self.search, width=25, text="Emergency", pady=10, bg='#1b9ea4',activeforeground='white', activebackground='#750E21', font=('tahoma', 10, 'bold'), cursor='mouse')
        self.mess.grid(row=3, column=1, sticky='snew', pady=100, padx=7)

        self.lab = Label(self.master , text='Log in to the system 2024', font=('Courier',11 ,'bold'),bg='whitesmoke')
        self.lab.place(x=180 , y=555)


        self.Enter.bind("<Enter>", self.on_enter)
        self.Enter.bind("<Leave>", self.on_leve)
        #keyboard.on_press_key("enter", self.on_enter_pressed)

    def login1(self):
        mydp = mc.connect(host='localhost',
                          user='root',
                          password='',
                          database="un")
        mycursor = mydp.cursor()
        sql = "select * from loginadmi where Username = '" + self.EntryUser.get() + "' and Password = '" + self.Entrypass.get() + "' "
        mycursor.execute(sql)
        res = mycursor.fetchone()
        if(res == None):
            mb.showerror("Error", "Invalid Username and Password ! Please Try again", parent = self.master)
        else:
            window = Toplevel()
            uni = University(window)
            self.master.withdraw()
            mydp.close()
    def on_enter(self , ev):
        self.Enter['background']='#213363'
    def on_leve(self , ev):
        self.Enter['background']='#1b9ea4'

    def search(self):
        if self.ch1.get() == 1 :
            e = 'https://api.whatsapp.com/send/?phone=%2B963991853387&text&type=phone_number&app_absent=0'
            web.open(e)
        else:
            mb.showerror('Error', "لم يتم تفعيل خيار نسيت كلمة المرور")

    # def on_enter_pressed(self, event):
    #     self.Enter.invoke()







if (__name__ == '__main__'):
    window = Tk()
    std = Login(window)
    mainloop()