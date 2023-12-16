from tkinter import *
from PIL import Image,ImageTk
import Student as s
import Staff as st
import Library as l
import Exam as e
import InfoUniversity as i
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
        # ---------- Frame Top End Here ----------------------------

        # #---------- Frame Center Start Here -----------------------##
        self.centerFrame = Frame(self.master)
        self.centerFrame.pack(fill=X)

        # ---------- Frame University info ----------------------------
        info = i.InfoUniversity(self.centerFrame)
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


        self.bottomFrame.grid_columnconfigure(0, weight=1)
        self.bottomFrame.grid_columnconfigure(1, weight=1)

























if (__name__ == '__main__'):
    window = Tk()
    std = University(window)
    print(window.winfo_screenheight())
    print(window.winfo_screenwidth())
    mainloop()