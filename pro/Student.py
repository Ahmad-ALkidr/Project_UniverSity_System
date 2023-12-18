import re
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector as mc
import tkinter.messagebox as mb
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
        self.ButtonStudent = Button(self.studentFrame, command=self.openstudentwindo, text="Student Management", bg='#1b9ea4', fg='white', padx=10,pady=10, font=("tahoma", 10, 'bold'))
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
        self.FirstName = Label(self.frameleft , text='FirstName', font=('tahoma',10,'bold'))
        self.FirstName.place(x=10,y=20)
        self.LastName = Label(self.frameleft, text='LastName',font=('tahoma',10,'bold'))
        self.LastName.place(x=10, y=60)
        self.CIN = Label(self.frameleft, text='CIN',font=('tahoma',10,'bold'))
        self.CIN.place(x=10, y=100)
        self.Email = Label(self.frameleft, text='Email',font=('tahoma',10,'bold'))
        self.Email.place(x=10, y=140)
        self.Phone = Label(self.frameleft, text='Phone', font=('tahoma', 10, 'bold'))
        self.Phone.place(x=10, y=180)
        self.Date = Label(self.frameleft, text='Date', font=('tahoma', 10, 'bold'))
        self.Date.place(x=10, y=220)

        # الحصول على \
        #الدالة StringVar() في بايثون هي دالة لإنشاء متغير نصي. يمكن استخدام هذا المتغير لربطه بعناصر واجهة المستخدم الرسومية، مثل الحقول النصية، لإنشاء ربط ديناميكي بين عنصر واجهة المستخدم وبيانات التطبيق.
        self.first = StringVar()
        self.last = StringVar()
        self.cin = StringVar()
        self.email = StringVar()
        self.phone = StringVar()
        self.date = StringVar()

        self.FirstNameEntry = Entry(self.frameleft, fg='#4F4F4F',font=('tahoma',12,'bold'),textvariable=self.first)
        self.FirstNameEntry.place(x=100, y=20,width=150,height=30)
        self.LastNameEntry = Entry(self.frameleft, fg='#4F4F4F',font=('tahoma',12,'bold'),textvariable=self.last)
        self.LastNameEntry.place(x=100, y=60,width=150,height=30)
        self.CINEntry = Entry(self.frameleft, fg='#4F4F4F',font=('tahoma',12,'bold'),textvariable=self.cin)
        self.CINEntry.place(x=100, y=100,width=150,height=30)
        self.EmailEntry = Entry(self.frameleft, fg='#4F4F4F',font=('tahoma',12,'bold'),textvariable=self.email)
        self.EmailEntry.place(x=100, y=140,width=150,height=30)
        self.PhoneEntry = Entry(self.frameleft, fg='#4F4F4F',font=('tahoma',12,'bold'),textvariable=self.phone)
        self.PhoneEntry.place(x=100, y=180, width=150, height=30)
        self.DateEntry = Entry(self.frameleft, fg='#4F4F4F',font=('tahoma',12,'bold'),textvariable=self.date)
        self.DateEntry.place(x=100, y=220, width=150, height=30)

        self.add = Button(self.frameleft,command=self.add, text="add",bg='#1b9ea4')
        self.add.place(x=30,y=350,width=60,height=60)
        self.Update = Button(self.frameleft,command=self.update ,text="Update",bg='#1b9ea4')
        self.Update.place(x=105, y=350,width=60,height=60)
        self.Delete = Button(self.frameleft,command=self.delete, text="Delete",bg='#1b9ea4')
        self.Delete.place(x=180, y=350,width=60,height=60)
        self.Show = Button(self.frameleft, command=self.read, text="Show", bg='#1b9ea4')
        self.Show.place(x=255, y=350, width=60, height=60)
        self.Rest = Button(self.frameleft, command=self.Reset, text="Rest", bg='#1b9ea4')
        self.Rest.place(x=330, y=350, width=60, height=60)

        # ------------Start right top -----------------------#
        self.frameright = Frame(self.master, width=800)
        self.frameright.pack(side=LEFT, fill=BOTH)
        # ------------Start right top -----------------------#
        self.framerighttop=Frame(self.frameright , height=50 , pady=5,padx=5)
        self.framerighttop.pack(fill=X)

        self.searchStudent = Entry(self.framerighttop,fg='#4F4F4F',font=('tahoma',12,'bold'),width=110)
        self.searchStudent.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
        self.ButtonSearch = Button(self.framerighttop,command=self.search , text="Search",fg='#4F4F4F',font=('tahoma',12,'bold'),width=50)
        self.ButtonSearch.grid(row=0,column=1,sticky='nsew',pady=10,padx=10)

        self.framerighttop.grid_columnconfigure(0, weight=1)
        self.framerighttop.grid_columnconfigure(1, weight=1)

        # -------------------------- Frame Top View --------------------------#
        self.frameview = Frame(self.frameright,bg='red')
        self.frameview.pack(fill=BOTH)
        self.scrollbar = Scrollbar(self.frameview,orient=VERTICAL)
        self.table = ttk.Treeview(self.frameview,columns=("ID","FirstName","LastName","CIN","Email","Phone","Date"),show='headings',yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=RIGHT,fill=Y)
        self.table.pack(fill=BOTH)

        self.table.heading("ID",text="ID")
        self.table.heading("FirstName", text="FirstName")
        self.table.heading("LastName", text="LastName")
        self.table.heading("CIN", text="CIN")
        self.table.heading("Email", text="Email")
        self.table.heading("Phone", text="Phone")
        self.table.heading("Date", text="Date")

        self.table.column("ID",anchor=W,width=10) # بلظهار القيم في الجدول في الجانب الايسر وضعنا w
        self.table.column("FirstName",anchor=W)
        self.table.column("LastName",anchor=W)
        self.table.column("CIN",anchor=W)
        self.table.column("Email",anchor=W)
        self.table.column("Phone", anchor=W,width=130)
        self.table.column("Date", anchor=W)
        #self.read()
        self.table.bind('<ButtonRelease>',self.show)


    def add(self):
        mydp=mc.connect(host='localhost',
                        user = 'root',
                        password='',
                        database="un")
        mycursor=mydp.cursor()
        sql='insert into student(FirstName,LastName,CIN,Email,Phone,Date) values (%s,%s,%s,%s,%s,%s)'
        if(self.FirstNameEntry.get()==''or self.LastNameEntry.get()=='' or self.CINEntry.get()=='' or self.EmailEntry.get() == '' or self.PhoneEntry.get()=='' or self.DateEntry.get()==''):
            mb.showerror('Error','all Data is Empty')
        else:

            st = self.EmailEntry.get().find('@gmail.com')
            # الحصول على التاريخ
            if(self.FirstNameEntry.get().isalpha() and self.LastNameEntry.get().isalpha() and self.CINEntry.get().isdigit() and (self.EmailEntry.get()[st]=='@' and st != -1) and self.PhoneEntry.get().isdigit() and not(self.DateEntry.get().isalpha())):
                    val=(self.FirstNameEntry.get(),self.LastNameEntry.get(),self.CINEntry.get(),self.EmailEntry.get(),self.PhoneEntry.get(),self.DateEntry.get())
                    mycursor.execute(sql,val)
                    mydp.commit()
                    id1 = mycursor.lastrowid #للحصول على اخر id اضيف للجدول

                    query = "SELECT * FROM student ORDER BY id DESC LIMIT 1"
                    mycursor.execute(query)
                    row = mycursor.fetchone()

                    if row[6] == None:
                        self.delete1(row[6],id1)
                        mb.showerror("Error","التاريخ الذي ادخلته خاطئ يا حبيبي رجاع دخل بهيك صيغة 2002-5 -1")
                    else:
                        self.table.insert('','end',values=(id1,self.FirstNameEntry.get(),self.LastNameEntry.get(),self.CINEntry.get(),self.EmailEntry.get(),self.PhoneEntry.get(),self.DateEntry.get()))
                        mb.showinfo("Successfully added",'Data inserted Successfully',parent = self.master)
                        #حذف بيانات الEntry
                        self.FirstNameEntry.delete(0,'end')
                        self.LastNameEntry.delete(0, 'end')
                        self.CINEntry.delete(0, 'end')
                        self.EmailEntry.delete(0, 'end')
                        self.PhoneEntry.delete(0, 'end')
                        self.DateEntry.delete(0, 'end')
                        #self.last_id = mycursor.lastrowid
                        # sss="SELECT Date FROM student WHERE id = %s" + str(self.last_id)
                        # sqll = mycursor.execute(sss)
                        # print(sqll)
                        mydp.close()
            else:
                mb.showerror('Error', 'يوجد قيمة او اكثر ليست من نوع البيانات المطلوبة')
    def read(self):
        mydp = mc.connect(host='localhost',
                          user='root',
                          password='',
                          database="un")
        mycursor = mydp.cursor()
        sql='select * from student'
        mycursor.execute(sql)
        myresult=mycursor.fetchall()
        self.table.delete(*self.table.get_children()) # كانت سبب في حدوث خطا اثناء استدعاء الدالة
        for mr in myresult:
            self.table.insert('','end',iid=mr[0],values=mr) # الحصول على قيمة iidالمفتاح من القاعدة # على علاقة focus مع

        # execute a select statement to get the date of the last inserted record

    def show(self,ev):
        self.iid = self.table.focus() # الحصول على id الصف المحدد عليه في الجدول
        alldata = self.table.item(self.iid) # الحصول على العناصر من الصف ووضعها في قاموس
        val =alldata['values'] #قائمة عناصر
        self.first.set(val[1])
        self.last.set(val[2])
        self.cin.set(val[3])
        self.email.set(val[4])
        self.phone.set(val[5])
        self.date.set(val[6])
    def Reset(self):
        self.FirstNameEntry.delete(0, 'end')
        self.LastNameEntry.delete(0, 'end')
        self.CINEntry.delete(0, 'end')
        self.EmailEntry.delete(0, 'end')
        self.PhoneEntry.delete(0, 'end')
        self.DateEntry.delete(0, 'end')
    def delete(self):
        mydp = mc.connect(host='localhost',
                          user='root',
                          password='',
                          database="un")
        mycursor = mydp.cursor()
        sql = ('delete from student where id = ' + self.iid)
        mycursor.execute(sql)
        mydp.commit()
        self.read()
        self.Reset()
        mb.showinfo("Deleted " , 'the Student Deleted',parent = self.master)
        # في حال التاريخ خاطئ
    def delete1(self , r , id):
        mydp = mc.connect(host='localhost',
                          user='root',
                          password='',
                          database="un")
        mycursor = mydp.cursor()
        query = "SELECT * FROM student ORDER BY id DESC LIMIT 1"
        mycursor.execute(query)
        row = mycursor.fetchone()
        sql = ('delete from student where id = ' + str(row[0]))
        mycursor.execute(sql)
        mydp.commit()
    def update(self):
        mydp = mc.connect(host='localhost',
                          user='root',
                          password='',
                          database="un")
        mycursor = mydp.cursor()
        sql = ('update student set FirstName=%s,LastName=%s,CIN=%s,Email=%s,Phone=%s,Date=%s where id = ' + self.iid)
        val=(self.first.get(),self.last.get(),self.cin.get(),self.email.get(),self.phone.get(),self.date.get())
        mycursor.execute(sql,val)
        mydp.commit()
        self.read()
        self.Reset()
        mb.showinfo("Update ", 'the Student is Update',parent = self.master)

    def search(self):
        mydp = mc.connect(host='localhost',
                          user='root',
                          password='',
                          database="un")
        mycursor = mydp.cursor()
        sql = ('select * from student where id = ' + self.searchStudent.get())
        mycursor.execute(sql)
        myresult = mycursor.fetchone()
        self.table.delete(*self.table.get_children())  # كانت سبب في حدوث خطا اثناء استدعاء الدالة هي لحذف كل سجلات الجدول
        self.table.insert('' , 'end' , iid=myresult[0] , values=myresult)
        mydp.commit()
        mydp.close()

