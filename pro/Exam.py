from tkinter import *
from PIL import Image,ImageTk
class Exam:
    def __init__(self,bottomFrame):
        self.bottomFrame=bottomFrame
        self.examFrame = Frame(self.bottomFrame, pady=10, padx=10)
        self.examFrame.grid(row=1, column=1, sticky='senw', pady=5)
        self.img4 = Image.open('image/university-education-book-icon-library-dictionary-vector-47047374.jpg')
        self.img4.thumbnail((200, 200))
        self.new_img4 = ImageTk.PhotoImage(self.img4)

        self.imgExam = Label(self.examFrame, image=self.new_img4, pady=10, padx=10)
        self.imgExam.pack()
        self.ButtonExam = Button(self.examFrame, command=self.openexamwindo, text="Exam Management", bg='#1b9ea4',
                                 fg='white', padx=10,
                                 pady=10, font=("tahoma", 10, 'bold'))
        self.ButtonExam.pack()

    def openexamwindo(self):
        self.master = Toplevel()
        self.master.title('Exam Management System')
        self.master.geometry("800x600+150+150")
