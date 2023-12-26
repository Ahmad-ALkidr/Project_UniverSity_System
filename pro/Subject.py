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
        self.img3 = Image.open('image/png-transparent-subject-international-english-computer-icons-symbol-english-miscellaneous-blue-english-removebg-preview.png')
        self.img3.thumbnail((150, 150))
        self.new_img3 = ImageTk.PhotoImage(self.img3)

        self.imgLibrary = Label(self.libraryFrame, image=self.new_img3, pady=10, padx=10)
        self.imgLibrary.pack()
        self.ButtonLibrary = Button(self.libraryFrame, command=self.openlibrarywindo, text="Subject Management",
                                    bg='#1b9ea4', fg='white', padx=10,
                                    pady=10, font=("tahoma", 10, 'bold'))
        self.ButtonLibrary.pack()
    def openlibrarywindo(self):
        lib = library()

class library:
    def __init__(self):
        self.master = Toplevel()
        self.master.title('(✿◡‿◡)Subject Management(✿◡‿◡)')
        self.master.geometry("1200x600+0+0")
        # -------------------------------------------------------#
        #  side  تسمح خاصية باخذ العنصر لاقصى اليسار للوسط
        self.frameleft = Frame(self.master, width=400,bg='#1b9ea4')
        self.frameleft.pack(side=LEFT, fill=Y)
        # -------------------------------------------------------#
        self.nameLable = Label(self.frameleft, text='NameSubject :', font=('tahoma', 10, 'bold'),width=12)
        self.nameLable.place(x=10, y=20)
        self.UnitLabel = Label(self.frameleft, text='UnitSubject :', font=('tahoma', 10, 'bold'),width=12)
        self.UnitLabel.place(x=10, y=80)

        self.id_teacherL = Label(self.frameleft, text='id_teacher :', font=('tahoma', 10, 'bold'),width=12)
        self.id_teacherL.place(x=10, y=140)

        self.id_collegeL = Label(self.frameleft, text='id_college :', font=('tahoma', 10, 'bold'),width=12)
        self.id_collegeL.place(x=10, y=200)

        self.StartDateLabel = Label(self.frameleft, text='StartDate :', font=('tahoma', 10, 'bold'),width=12)
        self.StartDateLabel.place(x=10, y=250)
        self.EndDateLabel = Label(self.frameleft, text='EndDate :', font=('tahoma', 10, 'bold'),width=12)
        self.EndDateLabel.place(x=10, y=470)

        # الحصول على \
        # الدالة StringVar() في بايثون هي دالة لإنشاء متغير نصي. يمكن استخدام هذا المتغير لربطه بعناصر واجهة المستخدم الرسومية، مثل الحقول النصية، لإنشاء ربط ديناميكي بين عنصر واجهة المستخدم وبيانات التطبيق.
        self.name = StringVar()
        self.unit = StringVar()
        self.id_teacher1 = StringVar()
        self.id_college1 = StringVar()

        self.nameSubject = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'), textvariable=self.name)
        self.nameSubject.place(x=130, y=20, width=250, height=30)
        self.unitSubject= Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'), textvariable=self.unit)
        self.unitSubject.place(x=130, y=80, width=250, height=30)
        self.id_teacherE = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'), textvariable=self.id_teacher1)
        self.id_teacherE.place(x=130, y=140, width=250, height=30)
        self.id_college = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'), textvariable=self.id_college1)
        self.id_college.place(x=130, y=200, width=250, height=30)

        # الحصول على تاريخ اليوم
        # t = datetime.today()
        # s = str(t).split('-')
        # ss = s[2].split(' ')

        self.StartDate = Calendar(self.frameleft ,mindate=datetime.today())
        self.StartDate.place(x=130, y=250, width=250, height=200)
        self.EndDate = Calendar(self.frameleft,selectmode='day',mindate=datetime.today())
        self.EndDate.place(x=130, y=470, width=250, height=200)



        # ------------Start right top -----------------------#
        self.frameright = Frame(self.master, width=800,bg='#E5E7E9')
        self.frameright.pack(side=LEFT, fill=BOTH)
        # ------------Start right top -----------------------#
        self.framerighttop = Frame(self.frameright, height=50, pady=5, padx=5,bg='#E5E7E9')
        self.framerighttop.pack(fill=X)

        self.searchStudent = Entry(self.framerighttop, fg='#4F4F4F', font=('tahoma', 12, 'bold'), width=110)
        self.searchStudent.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
        self.ButtonSearch = Button(self.framerighttop, command=self.search, text="Search", fg='#4F4F4F',
                                   font=('tahoma', 12, 'bold'), width=50)
        self.ButtonSearch.grid(row=0, column=1, sticky='nsew', pady=10, padx=10)

        self.framerighttop.grid_columnconfigure(0, weight=1)
        self.framerighttop.grid_columnconfigure(1, weight=1)

        # -------------------------- Frame Top View --------------------------#
        self.frameview = Frame(self.frameright)
        self.frameview.pack(fill=BOTH)
        self.scrollbar = Scrollbar(self.frameview, orient=VERTICAL)
        self.table = ttk.Treeview(self.frameview,
                                  columns=("ID", "NameSubject", "Units", "StartDate","EndDate","id_teacher","id_collage"),
                                  show='headings', yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.table.pack(fill=BOTH)

        self.table.heading("ID", text="ID")
        self.table.heading("NameSubject", text="NameSubject")
        self.table.heading("Units", text="Units")
        self.table.heading("StartDate", text="StartDate")
        self.table.heading("EndDate", text="EndDate")
        self.table.heading("id_teacher", text="id_teacher")
        self.table.heading("id_collage", text="id_collage")

        self.table.column("ID", anchor=W, width=10)  # بلظهار القيم في الجدول في الجانب الايسر وضعنا w
        self.table.column("NameSubject", anchor=W)
        self.table.column("Units", anchor=W , width=20)
        self.table.column("StartDate", anchor=W)
        self.table.column("EndDate", anchor=W)
        self.table.column("id_teacher", anchor=W,width=30)
        self.table.column("id_collage", anchor=W , width=30)
        # self.read()
        self.img2 = Image.open('image/delete.png')
        self.img2.thumbnail((30, 30))
        self.new_im2 = ImageTk.PhotoImage(self.img2)

        self.img0 = Image.open('image/add-file.png')
        self.img0.thumbnail((30, 30))
        self.new_im0 = ImageTk.PhotoImage(self.img0)

        self.img1 = Image.open('image/rotation.png')
        self.img1.thumbnail((30, 30))
        self.new_im1 = ImageTk.PhotoImage(self.img1)

        self.img4 = Image.open('image/cleaning.png')
        self.img4.thumbnail((30, 30))
        self.new_im4 = ImageTk.PhotoImage(self.img4)

        self.img3 = Image.open('image/visual.png')
        self.img3.thumbnail((30, 30))
        self.new_im3 = ImageTk.PhotoImage(self.img3)


        self.add = Button(self.frameleft, command=self.add,image=self.new_im0, bg='#D0D3D4'  , activebackground='#750E21', activeforeground='white' , font=('Tahoma',10 , 'bold'),cursor='plus')
        self.add.place(x=30, y=700, width=60, height=60)
        self.Update = Button(self.frameleft, command=self.update, image=self.new_im1, bg='#D0D3D4',activeforeground='white',activebackground='#750E21' , font=('tahoma',10,'bold'),cursor='plus')
        self.Update.place(x=105, y=700, width=60, height=60)
        self.Delete = Button(self.frameleft, command=self.delete, image=self.new_im2, bg='#D0D3D4',activeforeground='white',activebackground='#750E21' , font=('tahoma',10,'bold'),cursor='mouse')
        self.Delete.place(x=180, y=700, width=60, height=60)
        self.Show = Button(self.frameleft, command=self.read, image=self.new_im3, bg='#D0D3D4',activeforeground='white',activebackground='#750E21' , font=('tahoma',10,'bold'),cursor='plus')
        self.Show.place(x=255, y=700, width=60, height=60)
        self.Rest = Button(self.frameleft, command=self.Reset, image=self.new_im4, bg='#D0D3D4',activeforeground='white',activebackground='#750E21' , font=('tahoma',10,'bold'),cursor='plus')
        self.Rest.place(x=330, y=700, width=60, height=60)
        self.Re = Button(self.frameright, command=self.registration, text="registration", bg='#D0D3D4',activeforeground='white',activebackground='#750E21' , font=('tahoma',10,'bold'),cursor='plus')
        self.Re.place(x=50, y=300, width=80, height=60)



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
        self.add['background'] = '#D0D3D4'

    def on_enter1(self , ev):
        self.Update['background'] = '#213363'
    def on_leve1(self , ev):
        self.Update['background'] = '#D0D3D4'

    def on_enter2(self , ev):
        self.Delete['background'] = '#213363'
    def on_leve2(self , ev):
        self.Delete['background'] = '#D0D3D4'

    def on_enter3(self , ev):
        self.Show['background'] = '#213363'
    def on_leve3(self , ev):
        self.Show['background'] = '#D0D3D4'

    def on_enter4(self , ev):
        self.Rest['background'] = '#213363'
    def on_leve4(self , ev):
        self.Rest['background'] = '#D0D3D4'


    def add(self):
        mydp = mc.connect(host='localhost',
                          user='root',
                          password='',
                          database="un")
        mycursor = mydp.cursor()
        sql = 'insert into Subject(Name_Subject,Units,StartDate,EndDate,id_techer , id_colleges) values (%s,%s,%s,%s,%s,%s)'
        if (len(self.nameSubject.get()) == 0 or len(self.unitSubject.get()) == 0  or len(self.StartDate.get_date())==0 or len(self.EndDate.get_date())==0 or len(self.id_college.get())==0 or len(self.id_teacherE.get()) == 0):
            mb.showerror('Error', 'all Data is Empty')
        else:
            # الحصول على التاريخ
            if self.nameSubject.get().isalpha():
                if self.unitSubject.get().isdigit():
                    try:
                        val = (self.nameSubject.get(), self.unitSubject.get(), self.StartDate.get_date(), self.EndDate.get_date(),self.id_teacherE.get(),self.id_college.get())
                        mycursor.execute(sql, val)
                        mydp.commit()
                        id1 = mycursor.lastrowid  # للحصول على اخر id اضيف للجدول
                        self.table.insert('', 'end', values=(id1, self.nameSubject.get(), self.unitSubject.get(), self.StartDate.get_date(),self.EndDate.get_date(), self.id_teacherE.get(),self.id_college.get()))
                        mb.showinfo("Successfully added", 'Data inserted Successfully', parent=self.master)
                        # حذف بيانات الEntry
                        # self.nameStudent.delete(0, 'end')
                            # self.phoneStudent.delete(0, 'end')
                        # self.BookEntry.delete(0, 'end')
                        # self.last_id = mycursor.lastrowid
                        # sss="SELECT Date FROM student WHERE id = %s" + str(self.last_id)
                        # sqll = mycursor.execute(sss)
                        # print(sqll)    print(datetime.today())
                        self.read()
                        self.Reset()
                        mydp.close()
                    except:
                        mb.showinfo('Error' ,  " رقم المدرس او رقم الكلية غير صحيح" ,parent =self.master)
                else:
                    mb.showerror('Error', "عدد الوحدات بياناته غير صحيحة")
            else:
                mb.showerror('Error', "الاسم المادة بياناته غير صحيحة")

    def read(self):
        mydp = mc.connect(host='localhost',
                          user='root',
                          password='',
                          database="un")
        mycursor = mydp.cursor()
        sql = 'select * from subject'
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
        self.unit.set(val[2])
        self.StartDate.selection_set(val[3])
        self.EndDate.selection_set(val[4])
        self.id_teacher1.set(val[5])
        self.id_college1.set(val[6])

    def Reset(self):
        self.nameSubject.delete(0, 'end')
        self.unitSubject.delete(0, 'end')
        self.StartDate.selection_clear()
        self.EndDate.selection_clear()
        self.id_college.delete(0 , 'end')
        self.id_teacherE.delete(0 , 'end')

    def delete(self):
        mydp = mc.connect(host='localhost',
                          user='root',
                          password='',
                          database="un")
        mycursor = mydp.cursor()
        try:
            sql = ('delete from subject where id = ' + self.iid)
        except:
            mb.showerror('Error',   'لم يتم تجديد سطر' ,parent =self.master)
            return 0
        try:
            mycursor.execute(sql)
            mydp.commit()
            self.read()
            self.Reset()
            mb.showinfo("Deleted ", 'the Book Deleted', parent=self.master)
        except:
            mb.showerror('Error',  'لايمكن حذف السجل لارتباطه بجداول اخرى' ,parent =self.master)
    def update(self):
        mydp = mc.connect(host='localhost',
                          user='root',
                          password='',
                          database="un")
        mycursor = mydp.cursor()
        try:
            sql = ('update subject set Name_Subject=%s,Units=%s,StartDate=%s,EndDate=%s,id_techer=%s,id_colleges=%s where id = ' + self.iid)
        except:
            mb.showerror('Error', 'لم يتم تحديد سطر' ,parent = self.master)
            return 0
        try:
            val = (self.nameSubject.get(), self.unitSubject.get(), self.StartDate.get_date(),self.EndDate.get_date(), self.id_teacherE.get(),self.id_college.get())
            mycursor.execute(sql, val)
            mydp.commit()
            self.read()
            self.Reset()
            mb.showinfo("Update ", 'the Book is Update', parent=self.master)
        except:
            mb.showerror('Error','رقم المدرس او رقم الكلية غير موجود' ,parent =self.master)

    def search(self):
        mydp = mc.connect(host='localhost',
                          user='root',
                          password='',
                          database="un")
        mycursor = mydp.cursor()
        if (len(self.searchStudent.get()) != 0):
            if self.searchStudent.get().isdigit():
                try:
                    sql = ('select * from Subject where id = ' + self.searchStudent.get())
                    mycursor.execute(sql)
                    myresult = mycursor.fetchone()
                    self.table.delete(*self.table.get_children())  # كانت سبب في حدوث خطا اثناء استدعاء الدالة هي لحذف كل سجلات الجدول
                    self.table.insert('', 'end', iid=myresult[0], values=myresult)
                    mydp.commit()
                    mydp.close()
                except:
                    mb.showerror("Error", "الرقم الذي ادخلته غير موجود")
            else:
                mb.showerror("Error", "البيانات التي ادخلتها غير صحيحة")
        else:
            mb.showerror('Error', "لم يتم تحديد قيمة" , parent = self.master)
    def registration(self):
        self.reg = Frame(self.frameright, width=400)
        self.reg.pack(side=RIGHT, fill=BOTH, pady=100, padx=100)

        self.table1 = ttk.Treeview(self.reg,columns=("id_Student", "id_Subject", "Result"),
                                  show='headings', height=400)

        self.table1.grid(row=0, column=0 )
        self.regL = Frame(self.frameright,  width=600,bg='#E5E7E9')
        self.regL.pack(side=LEFT, fill=BOTH, pady=100)

        self.table1.heading("id_Student", text="id_Student")
        self.table1.heading("id_Subject", text="id_Subject")
        self.table1.heading("Result", text="Result")

        self.table1.column("id_Student", anchor=W, width=130)
        self.table1.column("id_Subject", anchor=W, width=130)
        self.table1.column("Result", anchor=W, width=130)

        self.id_St1=StringVar()
        self.id_Sub1=StringVar()
        self.result1=StringVar()

        self.labAdd = Label(self.regL , text="id_Student",width=10 )
        self.labAdd.place(x=10 , y=10 , height=30)
        self.id_St = Entry(self.regL, width=50 , textvariable=self.id_St1)
        self.id_St.place(x=150,  y=10 , height=30)

        self.labAd= Label(self.regL, text="id_Subject", width=10)
        self.labAd.place(x=10, y=60, height=30)
        self.id_Sub = Entry(self.regL, width=50 , textvariable=self.id_Sub1)
        self.id_Sub.place(x=150, y=60, height=30)

        self.lab = Label(self.regL, text="Result", width=10)
        self.lab.place(x=10, y=110, height=30)
        self.result = Entry(self.regL, width=50 , textvariable= self.result1)
        self.result.place(x=150, y=110, height=30)


        self.add1 = Button(self.regL, command=self.add_registration, text="Add", bg='#1b9ea4', width=7, pady=10)
        self.add1.place(x=50, y=200)
        self.Update1 = Button(self.regL, command=self.update1, text="Update", bg='#1b9ea4', width=7, pady=10)
        self.Update1.place(x=125, y=200)
        self.Delete1 = Button(self.regL, command=self.delete1, text="Delete", bg='#1b9ea4', width=7, pady=10)
        self.Delete1.place(x=50, y=270)
        self.Show1 = Button(self.regL, command=self.read1, text="Show", bg='#1b9ea4', width=7, pady=10)
        self.Show1.place(x=125, y=270)
        self.rest = Button(self.regL, command=self.Reset1, text="Rest", bg='#1b9ea4', width=7, pady=10)
        self.rest.place(x=200, y=200)

        self.table1.bind('<ButtonRelease>', self.show1)

    def add_registration(self):
        mydp = mc.connect(host='localhost',
                          user='root',
                          password='',
                          database="un")
        mycursor = mydp.cursor()
        if (len(self.id_St.get()) == 0 or len(self.id_Sub.get()) == 0 or len(self.result.get()) == 0):
            mb.showerror('Error', 'يوجد حقول فارغة', parent=self.master)
            return 0
        else:
            if self.id_St.get().isdigit():
                if self.id_Sub.get().isdigit():
                    if self.result.get().isdigit():
                        try:
                            mycursor = mydp.cursor()
                            sql = 'insert into students_grades(id_Student,id_Subject,result) values (%s,%s,%s)'
                            val = (self.id_St.get(), self.id_Sub.get(), self.result.get())
                            mycursor.execute(sql, val)
                            mydp.commit()
                            self.table1.insert('', 'end',
                                               values=(self.id_St.get(), self.id_Sub.get(), self.result.get()))
                        except :
                            mb.showerror('Error','رقم الطالب او رقم المادة غير موجود او تم تكرير البيانات')
                            return 0
                        try:
                            sq = "select DataExam from exam , colleges , subject where subject.id ='"+self.id_Sub.get()+"' and subject.id_colleges = colleges.id and colleges.id = exam.id_colleges "
                            mycursor.execute(sq)
                            aa = mycursor.fetchone()
                            aa1 = aa[0].split('/')
                            aa2 = ''
                            for i in range(len(aa1)):
                                if i == 2:
                                    continue
                                else:
                                    aa2 += aa1[i]
                            today1 = datetime.today()
                            aa3 = str(today1).split(' ')
                            aa4 = aa3[0].split('-')
                            aa5 = ''
                            for i in range(len(aa4)):
                                if i == 0:
                                    continue
                                else:
                                    aa5 += aa4[i]
                            if int(aa2) >= int(aa5):
                                sql1 = ("delete from students_grades where id_student = '" + self.id_St.get() + "' and id_Subject = '" + self.id_Sub.get() + "' ")
                                mycursor.execute(sql1)
                                mydp.commit()
                                self.read1()
                                self.Reset1()
                                mb.showerror('Error', 'لم يتم تقديم المادة')
                                return 0
                            mb.showinfo("Successfully added", 'Data inserted Successfully', parent=self.master)
                            self.read1()
                            self.Reset1()
                            mydp.close()
                        except:
                            mb.showerror("Error",'لم يتم تقديم المادة')
                    else:
                        mb.showerror('Error', "حقل رقم الطالب بياناته غير صحيحة")
                else:
                    mb.showerror('Error', "حقل رقم المادة بياناته غير صحيحة")
            else:
                mb.showerror('Error', "حقل النتيجة بياناته غير صحيحة")
    def read1(self):
        mydp = mc.connect(host='localhost',
                          user='root',
                          password='',
                          database="un")
        mycursor = mydp.cursor()
        sql = 'select * from students_grades'
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        self.table1.delete(*self.table1.get_children())  # كانت سبب في حدوث خطا اثناء استدعاء الدالة
        for mr in myresult:
            self.table1.insert('', 'end',
                              values=mr)  # الحصول على قيمة iidالمفتاح من القاعدة # على علاقة focus مع
        self.iid=None
    def show1(self, ev):
        iid = self.table1.focus()  # الحصول على id الصف المحدد عليه في الجدول
        alldata = self.table1.item(iid)  # الحصول على العناصر من الصف ووضعها في قاموس        print(alldata)
        self.val = alldata['values']  # قائمة عناصر
        self.id_St1.set(self.val[0])
        self.id_Sub1.set(self.val[1])
        self.result1.set(self.val[2])
    def Reset1(self):
        self.id_St.delete(0, 'end')
        self.id_Sub.delete(0, 'end')
        self.result.delete(0, 'end')
    def delete1(self):
        mydp = mc.connect(host='localhost',user='root',password='',database="un")
        mycursor = mydp.cursor()
        try:
            if self.val[0] != '':
                sql = ("delete from students_grades where id_student = '"+ str(self.val[0]) +"' and id_Subject = '"+str(self.val[1]) +"' " )
                mycursor.execute(sql)
                mydp.commit()
                self.read1()
                self.Reset1()
                mb.showinfo("Deleted ", 'Deleted Successfully', parent=self.master)
                self.val[0]=''
                self.val[1]=''
            else:
                mb.showerror('Error','لم يتم تحديد سطر' ,parent = self.master)
        except:
            mb.showerror('Error', "لم يتم تحديد سطر" , parent=self.master)
    def update1(self):
        mydp = mc.connect(host='localhost',
                          user='root',
                          password='',
                          database="un")
        mycursor = mydp.cursor()
        try:
            sql = ("update students_grades set id_student=%s,id_Subject=%s,result=%s where id_student = '"+ str(self.val[0]) +"' and id_Subject = '"+str(self.val[1]) +"' " )
        except:
            mb.showerror('Error', 'لم يتم تجديد سطر')
            return 0
        try:
            if self.id_St.get().isdigit():
                if self.id_Sub.get().isdigit():
                    if self.result.get().isdigit():
                        try:
                            val = (self.id_St.get(), self.id_Sub.get(), self.result.get())
                            mycursor.execute(sql, val)
                            mydp.commit()
                        except:
                            mb.showerror('Error','رقم الطالب او رقم المادة غير موجود او تم تكرير البيانات')
                        try:
                            sq = "select DataExam from exam , colleges , subject where subject.id ='" + self.id_Sub.get() + "' and subject.id_colleges = colleges.id and colleges.id = exam.id_colleges "
                            mycursor.execute(sq)
                            aa = mycursor.fetchone()
                            aa1 = aa[0].split('/')
                            aa2 = ''
                            for i in range(len(aa1)):
                                if i == 2:
                                    continue
                                else:
                                    aa2 += aa1[i]
                            today1 = datetime.today()
                            aa3 = str(today1).split(' ')
                            aa4 = aa3[0].split('-')
                            aa5 = ''
                            for i in range(len(aa4)):
                                if i == 0:
                                    continue
                                else:
                                    aa5 += aa4[i]
                            if int(aa2) >= int(aa5):
                                sql1 = ("delete from students_grades where id_student = '" + self.id_St.get() + "' and id_Subject = '" + self.id_Sub.get() + "' ")
                                mycursor.execute(sql1)
                                mydp.commit()
                                self.read1()
                                self.Reset1()
                                mb.showerror('Error', 'لم يتم تقديم المادة')
                                return 0
                            self.read1()
                            self.Reset1()
                            mb.showinfo("Update ", 'Updated successfully', parent=self.master)
                        except:
                            mb.showerror('error',   'رقم الطالب او رقم المادة غير موجود او تم تكرير المفتاح الرئيسي' , parent=self.master)
                    else:
                        mb.showerror('Error', "حقل رقم الطالب بياناته غير صحيحة")
                else:
                    mb.showerror('Error', "حقل رقم المادة بياناته غير صحيحة")
            else:
                mb.showerror('Error', "حقل النتيجة بياناته غير صحيحة")
        except:
            mb.showerror('Error','رقم الطالب او رقم المادة غير موجود' , parent = self.master)

