from tkinter import *
from PIL import Image,ImageTk

class InfoUniversity:
    def __init__(self,centerFrame):
        self.centerFrame=centerFrame
        self.universityInfo = Frame(self.centerFrame, pady=10, padx=10, bg='#f0f0f0')
        self.universityInfo.grid(row=0, column=0, sticky='senw', pady=5)
        self.img = Image.open('image/Sham-removebg-preview.png')
        self.img.thumbnail((200, 200))
        self.new_img = ImageTk.PhotoImage(self.img)

        self.imgUniversity = Label(self.universityInfo, image=self.new_img, pady=10, padx=10)
        self.imgUniversity.pack()
        self.ButtonUniversity = Button(self.universityInfo,command=self.openInfowindo ,text="About University", bg='#1b9ea4', fg='white', padx=10,
                                       pady=10, font=("tahoma", 10, 'bold'))
        self.ButtonUniversity.pack()

    def openInfowindo(self):
        self.master = Toplevel()
        self.master.title('Student Management System')
        self.master.geometry("800x600+150+150")