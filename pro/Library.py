from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector as mc
import tkinter.messagebox as mb
from tkcalendar import Calendar
from datetime import datetime
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
        lib = library()

class library:
    def __init__(self):
        self.master = Toplevel()
        self.master.title('Library Management System')
        self.master.geometry("1200x600+0+0")
        # -------------------------------------------------------#
        #  side  تسمح خاصية باخذ العنصر لاقصى اليسار للوسط
        self.frameleft = Frame(self.master, width=400)
        self.frameleft.pack(side=LEFT, fill=Y)
        # -------------------------------------------------------#
        self.nameLable = Label(self.frameleft, text='StudentName :', font=('tahoma', 10, 'bold'))
        self.nameLable.place(x=10, y=20)
        self.phonLabel = Label(self.frameleft, text='Phone :', font=('tahoma', 10, 'bold'))
        self.phonLabel.place(x=10, y=80)
        self.BookLabel = Label(self.frameleft, text='NameBook :', font=('tahoma', 10, 'bold'))
        self.BookLabel.place(x=10, y=140)
        self.DeliveryLabel = Label(self.frameleft, text='DeliveryDate :', font=('tahoma', 10, 'bold'))
        self.DeliveryLabel.place(x=10, y=200)
        self.ReturnLabel = Label(self.frameleft, text='ReturnDate :', font=('tahoma', 10, 'bold'))
        self.ReturnLabel.place(x=10, y=420)

        # الحصول على \
        # الدالة StringVar() في بايثون هي دالة لإنشاء متغير نصي. يمكن استخدام هذا المتغير لربطه بعناصر واجهة المستخدم الرسومية، مثل الحقول النصية، لإنشاء ربط ديناميكي بين عنصر واجهة المستخدم وبيانات التطبيق.
        self.name = StringVar()
        self.phone = StringVar()
        self.book = StringVar()
        self.delivery = StringVar()
        self.returnn = StringVar()

        self.nameStudent = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'), textvariable=self.name)
        self.nameStudent.place(x=130, y=20, width=250, height=30)
        self.phoneStudent = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'), textvariable=self.phone)
        self.phoneStudent.place(x=130, y=80, width=250, height=30)
        self.BookEntry = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'), textvariable=self.book)
        self.BookEntry.place(x=130, y=140, width=250, height=30)

        # الحصول على تاريخ اليوم
        t = datetime.today()
        s = str(t).split('-')
        ss = s[2].split(' ')

        self.DeliveryDate = Calendar(self.frameleft ,selectmode='day', year=int(s[0]),month=int(s[1]),day=int(ss[0]))
        self.DeliveryDate.place(x=130, y=200, width=250, height=200)
        self.ReturnDate = Calendar(self.frameleft,selectmode='day', year=int(s[0]),month=int(s[1]),day=int(ss[0]))
        self.ReturnDate.place(x=130, y=420, width=250, height=200)


        self.add = Button(self.frameleft, command=self.add, text="add", bg='#1b9ea4')
        self.add.place(x=30, y=650, width=60, height=60)
        self.Update = Button(self.frameleft, command=self.update, text="Update", bg='#1b9ea4')
        self.Update.place(x=105, y=650, width=60, height=60)
        self.Delete = Button(self.frameleft, command=self.delete, text="Delete", bg='#1b9ea4')
        self.Delete.place(x=180, y=650, width=60, height=60)
        self.Show = Button(self.frameleft, command=self.read, text="Show", bg='#1b9ea4')
        self.Show.place(x=255, y=650, width=60, height=60)
        self.Rest = Button(self.frameleft, command=self.Reset, text="Rest", bg='#1b9ea4')
        self.Rest.place(x=330, y=650, width=60, height=60)

        # ------------Start right top -----------------------#
        self.frameright = Frame(self.master, width=800)
        self.frameright.pack(side=LEFT, fill=BOTH)
        # ------------Start right top -----------------------#
        self.framerighttop = Frame(self.frameright, height=50, pady=5, padx=5)
        self.framerighttop.pack(fill=X)

        self.searchStudent = Entry(self.framerighttop, fg='#4F4F4F', font=('tahoma', 12, 'bold'), width=110)
        self.searchStudent.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
        self.ButtonSearch = Button(self.framerighttop, command=self.search, text="Search", fg='#4F4F4F',
                                   font=('tahoma', 12, 'bold'), width=50)
        self.ButtonSearch.grid(row=0, column=1, sticky='nsew', pady=10, padx=10)

        self.framerighttop.grid_columnconfigure(0, weight=1)
        self.framerighttop.grid_columnconfigure(1, weight=1)

        # -------------------------- Frame Top View --------------------------#
        self.frameview = Frame(self.frameright, bg='red')
        self.frameview.pack(fill=BOTH)
        self.scrollbar = Scrollbar(self.frameview, orient=VERTICAL)
        self.table = ttk.Treeview(self.frameview,
                                  columns=("ID", "Name", "Phone", "Book","DeliveryDate","ReturnDate"),
                                  show='headings', yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.table.pack(fill=BOTH)

        self.table.heading("ID", text="ID")
        self.table.heading("Name", text="Name")
        self.table.heading("Phone", text="Phone")
        self.table.heading("Book", text="Book")
        self.table.heading("DeliveryDate", text="DeliveryDate")
        self.table.heading("ReturnDate", text="ReturnDate")

        self.table.column("ID", anchor=W, width=10)  # بلظهار القيم في الجدول في الجانب الايسر وضعنا w
        self.table.column("Name", anchor=W)
        self.table.column("Phone", anchor=W)
        self.table.column("Book", anchor=W)
        self.table.column("DeliveryDate", anchor=W)
        self.table.column("ReturnDate", anchor=W)
        # self.read()
        self.table.bind('<ButtonRelease>', self.show)

    def add(self):
        mydp = mc.connect(host='localhost',
                          user='root',
                          password='',
                          database="un")
        mycursor = mydp.cursor()
        sql = 'insert into library(StudentName,Phone,Book,DeliveryDate,ReturnDate) values (%s,%s,%s,%s,%s)'
        if (len(self.nameStudent.get()) == 0 or len(self.phoneStudent.get()) == 0  or len(self.BookEntry.get())==0 or len(self.DeliveryDate.get_date())==0 or len(self.ReturnDate.get_date())==0):
            mb.showerror('Error', 'all Data is Empty')
        else:
            if (self.nameStudent.get().isalpha() and self.phoneStudent.get().isdigit() and self.BookEntry.get().isalpha()):
                val = (self.nameStudent.get(), self.phoneStudent.get(), self.BookEntry.get(), self.DeliveryDate.get_date(),self.ReturnDate.get_date())
                mycursor.execute(sql, val)
                mydp.commit()
                id1 = mycursor.lastrowid  # للحصول على اخر id اضيف للجدول
                self.table.insert('', 'end', values=(id1, self.nameStudent.get(), self.phoneStudent.get(), self.BookEntry.get(),
                self.DeliveryDate.get_date(), self.ReturnDate.get_date()))
                mb.showinfo("Successfully added", 'Data inserted Successfully', parent=self.master)
                # حذف بيانات الEntry
                self.nameStudent.delete(0, 'end')
                self.phoneStudent.delete(0, 'end')
                self.BookEntry.delete(0, 'end')
                # self.last_id = mycursor.lastrowid
                # sss="SELECT Date FROM student WHERE id = %s" + str(self.last_id)
                # sqll = mycursor.execute(sss)
                # print(sqll)    print(datetime.today())
                self.read()
                self.Reset()
                mydp.close()
            else:
                mb.showerror('Error', 'يوجد قيمة او اكثر ليست من نوع البيانات المطلوبة')

    def read(self):
        mydp = mc.connect(host='localhost',
                          user='root',
                          password='',
                          database="un")
        mycursor = mydp.cursor()
        sql = 'select * from library'
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        self.table.delete(*self.table.get_children())  # كانت سبب في حدوث خطا اثناء استدعاء الدالة
        for mr in myresult:
            self.table.insert('', 'end', iid=mr[0],
                              values=mr)  # الحصول على قيمة iidالمفتاح من القاعدة # على علاقة focus مع

        # execute a select statement to get the date of the last inserted record

    def show(self, ev):
        self.iid = self.table.focus()  # الحصول على id الصف المحدد عليه في الجدول
        alldata = self.table.item(self.iid)  # الحصول على العناصر من الصف ووضعها في قاموس
        val = alldata['values']  # قائمة عناصر
        self.name.set(val[1])
        self.phone.set(val[2])
        self.book.set(val[3])
        self.ReturnDate.selection_set(val[5])
        self.DeliveryDate.selection_set(val[4])

    def Reset(self):
        self.nameStudent.delete(0, 'end')
        self.phoneStudent.delete(0, 'end')
        self.BookEntry.delete(0, 'end')
        self.DeliveryDate.selection_clear()
        self.ReturnDate.selection_clear()

    def delete(self):
        mydp = mc.connect(host='localhost',
                          user='root',
                          password='',
                          database="un")
        mycursor = mydp.cursor()
        sql = ('delete from library where id = ' + self.iid)
        mycursor.execute(sql)
        mydp.commit()
        self.read()
        self.Reset()
        mb.showinfo("Deleted ", 'the Book Deleted', parent=self.master)

    def update(self):
        mydp = mc.connect(host='localhost',
                          user='root',
                          password='',
                          database="un")
        mycursor = mydp.cursor()
        sql = ('update library set StudentName=%s,Phone=%s,Book=%s,DeliveryDate=%s,ReturnDate=%s where id = ' + self.iid)
        val = (self.nameStudent.get(), self.phoneStudent.get(), self.BookEntry.get(),self.DeliveryDate.get_date(), self.ReturnDate.get_date())
        mycursor.execute(sql, val)
        mydp.commit()
        self.read()
        self.Reset()
        mb.showinfo("Update ", 'the Book is Update', parent=self.master)

    def search(self):
        mydp = mc.connect(host='localhost',
                          user='root',
                          password='',
                          database="un")
        mycursor = mydp.cursor()
        sql = ('select * from student where id = ' + self.searchStudent.get())
        mycursor.execute(sql)
        myresult = mycursor.fetchone()
        self.table.delete(
            *self.table.get_children())  # كانت سبب في حدوث خطا اثناء استدعاء الدالة هي لحذف كل سجلات الجدول
        self.table.insert('', 'end', iid=myresult[0], values=myresult)
        mydp.commit()
        mydp.close()


