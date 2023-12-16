from tkinter import *
from PIL import Image,ImageTk
class Staff:
    def __init__(self ,centerFrame):
        self.centerFrame=centerFrame
        self.staffFrame = Frame(self.centerFrame, pady=10, padx=10)
        self.staffFrame.grid(row=0, column=2,sticky='senw',pady=5)
        self.img2 = Image.open('image/2-removebg-preview.png')
        self.img2.thumbnail((200, 200))
        self.new_img2 = ImageTk.PhotoImage(self.img2)

        self.imgStaff = Label(self.staffFrame, image=self.new_img2,pady=10,padx=10)
        self.imgStaff.pack()
        self.ButtonStaff= Button(self.staffFrame,command=self.opensstaffwindo, text="Staff Management", bg='#1b9ea4', fg='white', padx=10,
                                       pady=10,font=("tahoma",10 , 'bold'))
        self.ButtonStaff.pack()

    def opensstaffwindo(self):
        self.master = Toplevel()
        self.master.title('Staff Management System')
        self.master.geometry("800x600+150+150")
