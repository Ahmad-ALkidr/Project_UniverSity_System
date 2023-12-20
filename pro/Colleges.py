from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector as mc
import tkinter.messagebox as mb

class colleges:
    def __init__(self,centerFrame):
        self.centerFrame=centerFrame
        self.universityInfo = Frame(self.centerFrame, pady=10, padx=10, bg='#f0f0f0')
        self.universityInfo.grid(row=0, column=0, sticky='senw', pady=5)
        self.img = Image.open('image/Sham-removebg-preview.png')
        self.img.thumbnail((200, 200))
        self.new_img = ImageTk.PhotoImage(self.img)

        self.imgUniversity = Label(self.universityInfo, image=self.new_img, pady=10, padx=10)
        self.imgUniversity.pack()
        self.ButtonUniversity = Button(self.universityInfo,command=self.openInfowindo ,text="College Management", bg='#1b9ea4', fg='white', padx=10,
                                       pady=10, font=("tahoma", 10, 'bold'))
        self.ButtonUniversity.pack()

    def openInfowindo(self):
        inf = InfoWindow()

class InfoWindow:
    def __init__(self):
        self.master = Toplevel()
        self.master.title('Colleges Management System')
        self.master.geometry("800x600+150+150")
        #  side  تسمح خاصية باخذ العنصر لاقصى اليسار للوسط
        self.frameleft = Frame(self.master, width=400)
        self.frameleft.pack(side=LEFT, fill=Y)
        self.frameleft.configure(bg='#EEF0E5')
        # -------------------------------------------------------#
        self.FirstName = Label(self.frameleft, text='NameColleges', font=('tahoma', 10, 'bold'))
        self.FirstName.place(x=10, y=50)
        self.LastName = Label(self.frameleft, text='NumCourse', font=('tahoma', 10, 'bold'))
        self.LastName.place(x=10, y=120)
        self.CIN = Label(self.frameleft, text='NumTeacher', font=('tahoma', 10, 'bold'))
        self.CIN.place(x=10, y=190)



        # الحصول على \
        # الدالة StringVar() في بايثون هي دالة لإنشاء متغير نصي. يمكن استخدام هذا المتغير لربطه بعناصر واجهة المستخدم الرسومية، مثل الحقول النصية، لإنشاء ربط ديناميكي بين عنصر واجهة المستخدم وبيانات التطبيق.
        self.NameCollege = StringVar()
        self.NumCourse = StringVar()
        self.NumTeacher = StringVar()

        self.NameCollegeE = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'), textvariable=self.NameCollege)
        self.NameCollegeE.place(x=100, y=50, width=200, height=30)
        self.NumCourseE = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'), textvariable=self.NumCourse)
        self.NumCourseE.place(x=100, y=120, width=200, height=30)
        self.NumTeacherE = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'), textvariable=self.NumTeacher)
        self.NumTeacherE.place(x=100, y=190, width=200, height=30)

        self.add = Button(self.frameleft, command=self.add, text="add", bg='#1b9ea4')
        self.add.place(x=30, y=350, width=60, height=60)
        self.Update = Button(self.frameleft, command=self.update, text="Update", bg='#1b9ea4')
        self.Update.place(x=105, y=350, width=60, height=60)
        self.Delete = Button(self.frameleft, command=self.delete, text="Delete", bg='#1b9ea4')
        self.Delete.place(x=180, y=350, width=60, height=60)
        self.Show = Button(self.frameleft, command=self.read, text="Show", bg='#1b9ea4')
        self.Show.place(x=255, y=350, width=60, height=60)
        self.Rest = Button(self.frameleft, command=self.Reset, text="Rest", bg='#1b9ea4')
        self.Rest.place(x=330, y=350, width=60, height=60)

        # ------------Start right top -----------------------#
        self.frameright = Frame(self.master, width=800)
        self.frameright.pack(side=LEFT, fill=BOTH)
        self.frameright.configure(bg='#EEF0E5')
        # ------------Start right top -----------------------#
        self.framerighttop = Frame(self.frameright, height=50, pady=5, padx=5)
        self.framerighttop.pack(fill=X)
        self.framerighttop.configure(bg='#EEF0E5')

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
                                  columns=("ID", "NameCollege", "NumCourse", "NumTeacher"),
                                  show='headings', yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.table.pack(fill=BOTH)

        self.table.heading("ID", text="ID")
        self.table.heading("NameCollege", text="NameCollege")
        self.table.heading("NumCourse", text="NumCourse")
        self.table.heading("NumTeacher", text="NumTeacher")

        self.table.column("ID", anchor=W, width=10)  # بلظهار القيم في الجدول في الجانب الايسر وضعنا w
        self.table.column("NameCollege", anchor=W , width=140)
        self.table.column("NumCourse", anchor=W , width=140)
        self.table.column("NumTeacher", anchor=W , width=100)

        # self.read()
        self.table.bind('<ButtonRelease>', self.show)

    def add(self):
        mydp = mc.connect(host='localhost',
                          user='root',
                          password='',
                          database="un")
        mycursor = mydp.cursor()
        sql = 'insert into colleges(NameCollage,NumCourse,NumTecher) values (%s,%s,%s)'
        if (len(self.NameCollege.get() )== 0 or len(self.NumCourse.get())== 0 or len(self.NumTeacher.get()) == 0):
            mb.showerror('Error', 'all Data is Empty' ,parent = self.master)
        else:
            if self.NameCollege.get().isalpha():
                if self.NumCourse.get().isdigit():
                    if self.NumTeacher.get().isdigit():
                        try:
                            val = (self.NameCollege.get(), self.NumCourse.get(), self.NumTeacher.get())
                            mycursor.execute(sql, val)
                            mydp.commit()
                            id1 = mycursor.lastrowid
                            self.table.insert('', 'end', values=(id1, self.NameCollege.get(), self.NumCourse.get(), self.NumTeacher.get()))
                            mb.showinfo("Successfully added", 'Data inserted Successfully', parent=self.master)
                            # حذف بيانات الEntry
                            self.read()
                            self.Reset()
                            # self.last_id = mycursor.lastrowid
                            # sss="SELECT Date FROM student WHERE id = %s" + str(self.last_id)
                            # sqll = mycursor.execute(sss)
                            # print(sqll)
                            mydp.close()
                        except:
                            mb.showerror('Error',"يوجد خطا",parent =self.master)
                else:
                    mb.showerror('Error',"حقل عدد المواد بياناته غير صحيحة",parent =self.master)
            else:
                mb.showerror('Error', "حقل عدد المدرسين بياناته غير صحيحة",parent =self.master)

    def read(self):
        mydp = mc.connect(host='localhost',
                          user='root',
                          password='',
                          database="un")
        mycursor = mydp.cursor()
        sql = 'select * from Colleges'
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        self.table.delete(*self.table.get_children())  # كانت سبب في حدوث خطا اثناء استدعاء الدالة
        for mr in myresult:
            self.table.insert('', 'end', iid=mr[0],values=mr)  # الحصول على قيمة iidالمفتاح من القاعدة # على علاقة focus مع
        # execute a select statement to get the date of the last inserted record
        self.iid=None

    def show(self, ev):

        self.iid = self.table.focus()  # الحصول على id الصف المحدد عليه في الجدول
        alldata = self.table.item(self.iid)  # الحصول على العناصر من الصف ووضعها في قاموس
        val = alldata['values']  # قائمة عناصر
        self.NameCollege.set(val[1])
        self.NumCourse.set(val[2])
        self.NumTeacher.set(val[3])

    def Reset(self):
        self.NameCollegeE.delete(0, 'end')
        self.NumCourseE.delete(0, 'end')
        self.NumTeacherE.delete(0, 'end')
    def delete(self):
        mydp = mc.connect(host='localhost',
                          user='root',
                          password='',
                          database="un")
        mycursor = mydp.cursor()
        try:
            sql = ('delete from Colleges where id = ' + self.iid)
        except:
            mb.showerror('Error', "لم يتم تحديد سطر",parent =self.master)
            return 0
        try:
            mycursor.execute(sql)
            mydp.commit()
            self.read()
            self.Reset()
            mb.showinfo("Deleted ", 'the Student Deleted', parent=self.master)
            self.iid =None
        except:
            mb.showerror('Error','لايمكن حذف السجل لارتباطه بجداول اخرى',parent =self.master)

        # في حال التاريخ خاطئ
    def update(self):
        mydp = mc.connect(host='localhost',
                          user='root',
                          password='',
                          database="un")
        mycursor = mydp.cursor()
        try:
            sql = ('update Colleges set NameCollage=%s,NumCourse=%s,NumTecher=%s where id = ' + self.iid)
        except:
            mb.showerror('Error', 'لم يتم تحديد سطر',parent =self.master)
            return 0
        if (len(self.NameCollege.get() )== 0 or len(self.NumCourse.get())== 0 or len(self.NumTeacher.get()) == 0):
            mb.showerror('Error', 'all Data is Empty' ,parent = self.master)
        else:
            if self.NameCollege.get().isalpha():
                if self.NumCourse.get().isdigit():
                    if self.NumTeacher.get().isdigit():
                        try:
                            val = (self.NameCollegeE.get(), self.NumCourseE.get(), self.NumTeacherE.get())
                            mycursor.execute(sql, val)
                            mydp.commit()
                            self.read()
                            self.Reset()
                            mb.showinfo("Update ", 'the Staff is Update', parent=self.master)
                        except:
                            mb.showerror('Error', "عندك خطأ",parent =self.master)
                    else:
                        mb.showerror('Error', "حقل عدد المدرسين بياناته غير صحيحة",parent =self.master)
                else:
                    mb.showerror('Error', "حقل عدد المواد بياناته غير صحيحة",parent =self.master)
            else:
                 mb.showerror('Error',"اسم الكلية خاطئ" ,parent =self.master)


    def search(self):
        mydp = mc.connect(host='localhost',
                          user='root',
                          password='',
                          database="un")
        mycursor = mydp.cursor()
        if (len(self.searchStudent.get()) != 0):
            if self.searchStudent.get().isdigit():
                try:
                    sql = ('select * from Colleges where id = ' + self.searchStudent.get())
                    mycursor.execute(sql)
                    myresult = mycursor.fetchone()
                    self.table.delete(*self.table.get_children())  # كانت سبب في حدوث خطا اثناء استدعاء الدالة هي لحذف كل سجلات الجدول
                    self.table.insert('', 'end', iid=myresult[0], values=myresult)
                    mydp.commit()
                    mydp.close()
                except:
                    mb.showerror("Error","الرقم الذي ادخلته غير موجود" ,parent =self.master)
            else:
                mb.showerror("Error","البيانات التي ادخلتها غير صحيحة" ,parent =self.master)
        else:
            mb.showerror('Error',"لم يتم تحديد قيمة",parent =self.master)


