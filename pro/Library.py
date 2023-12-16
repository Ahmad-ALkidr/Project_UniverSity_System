from tkinter import *
from PIL import Image,ImageTk
class Library:
    def __init__(self,bottomFrame):
        self.bottomFrame=bottomFrame
        self.libraryFrame = Frame(self.bottomFrame, pady=10, padx=10)
        self.libraryFrame.grid(row=1, column=0, sticky='senw', pady=5)
        self.img3 = Image.open('image/university-education-book-icon-library-dictionary-vector-47047374.jpg')
        self.img3.thumbnail((200, 200))
        self.new_img3 = ImageTk.PhotoImage(self.img3)

        self.imgLibrary = Label(self.libraryFrame, image=self.new_img3, pady=10, padx=10)
        self.imgLibrary.pack()
        self.ButtonLibrary = Button(self.libraryFrame, command=self.openlibrarywindo, text="Library Management",
                                    bg='#1b9ea4', fg='white', padx=10,
                                    pady=10, font=("tahoma", 10, 'bold'))
        self.ButtonLibrary.pack()

    def openlibrarywindo(self):
        self.master = Toplevel()
        self.master.title('Library Management System')
        self.master.geometry("800x600+150+150")
