import tkinter.messagebox as mb
from datetime import datetime
from tkinter import *
from tkinter import ttk

import mysql.connector as mc
from PIL import Image, ImageTk
from tkcalendar import Calendar


class Exam:
    def __init__(self, bottom_frame):
        self.bottomFrame = bottom_frame
        self.examFrame = Frame(self.bottomFrame, pady=10, padx=10)
        self.examFrame.grid(row=1, column=1, sticky='senw', pady=5) #تعني أن العنصر يتمدد في كل الاتجاهات: شمالًا وجنوبًا
        self.img4 = Image.open('image/4662967.png')
        self.img4.thumbnail((150, 150))
        self.new_img4 = ImageTk.PhotoImage(self.img4)

        self.imgExam = Label(self.examFrame, image=self.new_img4, pady=10, padx=10)
        self.imgExam.pack()
        self.ButtonExam = Button(self.examFrame, command=self.openexamwindo, text="Exam Management", bg='#1b9ea4',
                                 fg='white', padx=10,
                                 pady=10, font=("tahoma", 10, 'bold'))
        self.ButtonExam.pack()

    def openexamwindo(self):
        ex = exam()


class exam:
    def __init__(self):
        self.master = Toplevel()
        self.master.title('Exam Management System')
        self.master.geometry("1200x600+0+0")
        # -------------------------------------------------------#
        #  side  تسمح خاصية باخذ العنصر لاقصى اليسار للوسط
        self.frameleft = Frame(self.master, width=400)
        self.frameleft.pack(side=LEFT, fill=Y)
        # -------------------------------------------------------#
        self.nameLable = Label(self.frameleft, text='HallName :', font=('tahoma', 10, 'bold'))
        self.nameLable.place(x=10, y=20)
        self.phonLabel = Label(self.frameleft, text='NumClassRoom :', font=('tahoma', 10, 'bold'))
        self.phonLabel.place(x=10, y=80)
        self.BookLabel = Label(self.frameleft, text='Professor :', font=('tahoma', 10, 'bold'))
        self.BookLabel.place(x=10, y=140)
        self.id_CollegesLabel = Label(self.frameleft, text='id_Colleges :', font=('tahoma', 10, 'bold'))
        self.id_CollegesLabel.place(x=10, y=200)
        self.DateLabel = Label(self.frameleft, text='Date :', font=('tahoma', 10, 'bold'))
        self.DateLabel.place(x=10, y=250)
        self.TimeLabel = Label(self.frameleft, text='Time :', font=('tahoma', 10, 'bold'))
        self.TimeLabel.place(x=10, y=500)

        # الحصول على \
        # الدالة StringVar() في بايثون هي دالة لإنشاء متغير نصي. يمكن استخدام هذا المتغير لربطه بعناصر واجهة المستخدم الرسومية، مثل الحقول النصية، لإنشاء ربط ديناميكي بين عنصر واجهة المستخدم وبيانات التطبيق.
        self.name = StringVar()
        self.class1 = StringVar()
        self.professor1 = StringVar()
        self.time = StringVar()
        self.id_Colleges1 = StringVar()

        self.nameGroup = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'), textvariable=self.name)
        self.nameGroup.place(x=130, y=20, width=250, height=30)
        self.classRoom = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'), textvariable=self.class1)
        self.classRoom.place(x=130, y=80, width=250, height=30)
        self.professor = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'), textvariable=self.professor1)
        self.professor.place(x=130, y=140, width=250, height=30)
        self.id_Colleges = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'),
                                 textvariable=self.id_Colleges1)
        self.id_Colleges.place(x=130, y=200, width=250, height=30)

        # الحصول على تاريخ اليوم
        t = datetime.today()
        s = str(t).split('-')
        ss = s[2].split(' ')

        self.DateExam = Calendar(self.frameleft, mindate=datetime.today())
        self.DateExam.place(x=130, y=250, width=250, height=200)
        self.Time = ttk.Combobox(self.frameleft, values=['', '7:00', '8:00', '9:00', '10:00', '11:00', '12:00', '1:00'],
                                 font=('tahoma', 10, 'bold'), width=29, state='readonly',
                                 textvariable=self.time)
        self.Time.place(x=125, y=500)

        self.add = Button(self.frameleft, command=self.add, text="add", bg='#1b9ea4',activeforeground='white',activebackground='#750E21' , font=('tahoma',10,'bold'),cursor='plus')
        self.add.place(x=30, y=600, width=60, height=60)
        self.Update = Button(self.frameleft, command=self.update, text="Update", bg='#1b9ea4',activeforeground='white',activebackground='#750E21' , font=('tahoma',10,'bold'),cursor='plus')
        self.Update.place(x=105, y=600, width=60, height=60)
        self.Delete = Button(self.frameleft, command=self.delete, text="Delete", bg='#1b9ea4',activeforeground='white',activebackground='#750E21' , font=('tahoma',10,'bold'),cursor='mouse')
        self.Delete.place(x=180, y=600, width=60, height=60)
        self.Show = Button(self.frameleft, command=self.read, text="Show", bg='#1b9ea4',activeforeground='white',activebackground='#750E21' , font=('tahoma',10,'bold'),cursor='plus')
        self.Show.place(x=255, y=600, width=60, height=60)
        self.Rest = Button(self.frameleft, command=self.Reset, text="Rest", bg='#1b9ea4',activeforeground='white',activebackground='#750E21' , font=('tahoma',10,'bold'),cursor='plus')
        self.Rest.place(x=330, y=600, width=60, height=60)

        # ------------Start right top -----------------------#
        self.frameright = Frame(self.master, width=800, bg='red')
        self.frameright.pack(side=LEFT, fill=Y)
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
        self.frameview = Frame(self.frameright, bg='blue', height=600)
        self.frameview.pack(fill=BOTH)
        self.scrollbar = Scrollbar(self.frameview, orient=VERTICAL)
        self.table = ttk.Treeview(self.frameview,
                                  columns=(
                                  "ID", "HallName", "ClassRoom", "Professor", "DataExam", "Time", "id_Colleges"),
                                  show='headings', yscrollcommand=self.scrollbar.set, height=600)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.table.pack(fill=BOTH)

        self.table.heading("ID", text="ID")
        self.table.heading("HallName", text="HallName")
        self.table.heading("ClassRoom", text="ClassRoom")
        self.table.heading("Professor", text="Professor")
        self.table.heading("DataExam", text="DataExam")
        self.table.heading("Time", text="Time")
        self.table.heading("id_Colleges", text="id_Colleges")

        self.table.column("ID", anchor=W, width=10)  # بلظهار القيم في الجدول في الجانب الايسر وضعنا w
        self.table.column("HallName", anchor=W, width=130)
        self.table.column("ClassRoom", anchor=W, width=130)
        self.table.column("Professor", anchor=W, width=130)
        self.table.column("DataExam", anchor=W)
        self.table.column("Time", anchor=W)
        self.table.column("id_Colleges", anchor=W, width=15)
        # self.read()
        self.table.bind('<ButtonRelease>', self.show)

        self.add.bind("<Enter>", self.on_enter)
        self.add.bind("<Leave>", self.on_leve)

        self.Update.bind("<Enter>", self.on_enter1)
        self.Update.bind("<Leave>", self.on_leve1)

        self.Delete.bind("<Enter>", self.on_enter2)
        self.Delete.bind("<Leave>", self.on_leve2)

        self.Show.bind("<Enter>", self.on_enter3)
        self.Show.bind("<Leave>", self.on_leve3)

        self.Rest.bind("<Enter>", self.on_enter4)
        self.Rest.bind("<Leave>", self.on_leve4)

    def on_enter(self , ev):
        self.add['background'] = '#213363'
    def on_leve(self , ev):
        self.add['background'] = '#1b9ea4'

    def on_enter1(self , ev):
        self.Update['background'] = '#213363'
    def on_leve1(self , ev):
        self.Update['background'] = '#1b9ea4'

    def on_enter2(self , ev):
        self.Delete['background'] = '#213363'
    def on_leve2(self , ev):
        self.Delete['background'] = '#1b9ea4'

    def on_enter3(self , ev):
        self.Show['background'] = '#213363'
    def on_leve3(self , ev):
        self.Show['background'] = '#1b9ea4'

    def on_enter4(self , ev):
        self.Rest['background'] = '#213363'
    def on_leve4(self , ev):
        self.Rest['background'] = '#1b9ea4'

    def add(self):
        mydp = mc.connect(host='localhost',
                          user='root',
                          password='',
                          database="un")
        mycursor = mydp.cursor()
        sql = 'insert into exam(GroupName,ClassRoom,Professor,DataExam,Time,id_Colleges) values (%s,%s,%s,%s,%s,%s)'
        if (len(self.nameGroup.get()) == 0 or len(self.classRoom.get()) == 0 or len(self.professor.get()) == 0 or len(
                self.DateExam.get_date()) == 0 or len(self.Time.get()) == 0 or len(self.id_Colleges.get()) == 0):
            mb.showerror('Error', 'يوجد حقول فارغة', parent=self.master)
        else:
            if self.nameGroup.get().isalpha():
                if self.classRoom.get().isdigit():
                    if self.professor.get().isalpha():
                        if self.id_Colleges.get().isdigit():
                            try:
                                val = (self.nameGroup.get(), self.classRoom.get(), self.professor.get(),
                                       self.DateExam.get_date(), self.Time.get(), self.id_Colleges.get())
                                mycursor.execute(sql, val)
                                mydp.commit()
                                id1 = mycursor.lastrowid  # للحصول على اخر id اضيف للجدول
                                self.table.insert('', 'end', values=(
                                id1, self.nameGroup.get(), self.classRoom.get(), self.professor.get(),
                                self.DateExam.get_date(), self.Time.get(), self.id_Colleges.get()))
                                mb.showinfo("Successfully added", 'Data inserted Successfully', parent=self.master)
                                self.read()
                                self.Reset()
                                mydp.close()
                            except:
                                mb.showerror('error', 'الرقم الذي ادخلته غير موجود ياحبيبي')
                        else:
                            mb.showerror('Error', "حقل رقم الكلية بياناته غير صحيحة")
                    else:
                        mb.showerror('Error', "حقل اسم المدرس بياناته غير صحيحة")
                else:
                    mb.showerror('Error', "حقل classRoom بياناته غير صحيحة")
            else:
                mb.showerror('Error', "حقل اسم الكلية بياناته غير صحيحة")

            # حذف بيانات الEntry
            # self.nameGroup.delete(0, 'end')
            # self.classRoom.delete(0, 'end')
            # self.professor.delete(0, 'end')
            # self.Date.selection_clear()
            # self.Time.delete(0,'end')
            # self.last_id = mycursor.lastrowid
            # sss="SELECT Date FROM student WHERE id = %s" + str(self.last_id)
            # sqll = mycursor.execute(sss)
            # print(sqll)    print(datetime.today())

    def read(self):
        mydp = mc.connect(host='localhost',
                          user='root',
                          password='',
                          database="un")
        mycursor = mydp.cursor()
        sql = 'select * from exam'
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        self.table.delete(*self.table.get_children())  # كانت سبب في حدوث خطا اثناء استدعاء الدالة
        for mr in myresult:
            self.table.insert('', 'end', iid=mr[0],
                              values=mr)  # الحصول على قيمة iidالمفتاح من القاعدة # على علاقة focus مع

        # execute a select statement to get the date of the last inserted record
        self.iid = None

    def show(self, ev):
        self.iid = self.table.focus()  # الحصول على id الصف المحدد عليه في الجدول
        alldata = self.table.item(self.iid)  # الحصول على العناصر من الصف ووضعها في قاموس
        val = alldata['values']  # قائمة عناصر
        self.name.set(val[1])
        self.class1.set(val[2])
        self.professor1.set(val[3])
        self.DateExam.selection_set(val[4])
        self.time.set(val[5])
        self.id_Colleges1.set(val[6])

    def Reset(self):
        self.nameGroup.delete(0, 'end')
        self.classRoom.delete(0, 'end')
        self.professor.delete(0, 'end')
        self.id_Colleges.delete(0, 'end')
        self.DateExam.selection_clear()
        self.Time.set('')

    def delete(self):
        mydp = mc.connect(host='localhost', user='root', password='', database="un")
        mycursor = mydp.cursor()
        try:
            sql = ('delete from exam where id = ' + self.iid)
        except:
            mb.showerror('Error', 'لم يتم تجديد سطر')
            return 0
        try:
            mycursor.execute(sql)
            mydp.commit()
            self.read()
            self.Reset()
            mb.showinfo("Deleted ", 'the Book Deleted', parent=self.master)
        except:
            mb.showerror('Error', 'لايمكن حذف السجل لارتباطه بجداول اخرى')

    def update(self):
        mydp = mc.connect(host='localhost',
                          user='root',
                          password='',
                          database="un")
        mycursor = mydp.cursor()
        try:
            sql = (
                        'update exam set GroupName=%s,ClassRoom=%s,Professor=%s,DataExam=%s,Time=%s,id_colleges=%s where id = ' + self.iid)
        except:
            mb.showerror('Error', 'لم يتم تجديد سطر')
            return 0
        if (len(self.nameGroup.get()) == 0 or len(self.classRoom.get()) == 0 or len(self.professor.get()) == 0 or len(
                self.DateExam.get_date()) == 0 or len(self.Time.get()) == 0 or len(self.id_Colleges.get()) == 0):
            mb.showerror('Error', 'يوجد حقول فارغة', parent=self.master)
        else:
            try:
                if self.nameGroup.get().isalpha():
                    if self.classRoom.get().isdigit():
                        if self.professor.get().isalpha():
                            if self.id_Colleges.get().isdigit():
                                try:
                                    val = (self.nameGroup.get(), self.classRoom.get(), self.professor.get(),
                                           self.DateExam.get_date(), self.Time.get(), self.id_Colleges.get())
                                    mycursor.execute(sql, val)
                                    mydp.commit()
                                    self.read()
                                    self.Reset()
                                    mb.showinfo("Update ", 'the Exam is Update', parent=self.master)
                                except:
                                    mb.showerror('error', 'الرقم الذي ادخلته غير موجود ياحبيبي')
                            else:
                                mb.showerror('Error', "حقل رقم الكلية بياناته غير صحيحة")
                        else:
                            mb.showerror('Error', "حقل اسم المدرس بياناته غير صحيحة")
                    else:
                        mb.showerror('Error', "حقل classRoom بياناته غير صحيحة")
                else:
                    mb.showerror('Error', "حقل اسم الكلية بياناته غير صحيحة")
            except:
                mb.showerror('Error', 'رقم الكلية غير موجود في جدول الكلية')

    def search(self):
        mydp = mc.connect(host='localhost',
                          user='root',
                          password='',
                          database="un")
        mycursor = mydp.cursor()
        if (len(self.searchStudent.get()) != 0):
            if self.searchStudent.get().isdigit():
                try:
                    sql = ('select * from exam where id = ' + self.searchStudent.get())
                    mycursor.execute(sql)
                    myresult = mycursor.fetchone()
                    self.table.delete(
                        *self.table.get_children())  # كانت سبب في حدوث خطا اثناء استدعاء الدالة هي لحذف كل سجلات الجدول
                    self.table.insert('', 'end', iid=myresult[0], values=myresult)
                    mydp.commit()
                    mydp.close()
                except:
                    mb.showerror("Error", "الرقم الذي ادخلته غير موجود")
            else:
                mb.showerror("Error", "البيانات التي ادخلتها غير صحيحة")
        else:
            mb.showerror('Error', "لم يتم تحديد قيمة")
