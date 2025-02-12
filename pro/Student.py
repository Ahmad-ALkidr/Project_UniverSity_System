import io
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector as mc
import tkinter.messagebox as mb
from datetime import datetime
from tkinter import filedialog

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
        self.ButtonStudent = Button(self.studentFrame, command=self.openstudentwindo, text="Student Management",
                                    bg='#1b9ea4', fg='white', padx=10, pady=10, font=("tahoma", 10, 'bold'), bd=5)
        self.ButtonStudent.pack()

    def openstudentwindo(self):
        stdw = StudentWindow()


class StudentWindow:
    def __init__(self):
        self.master = Toplevel()
        self.master.title('ƪ(˘⌣˘)ʃStudent Management Systemƪ(˘⌣˘)ʃ')
        self.master.geometry("1200x600+0+0")
        # -------------------------------------------------------#
        #  side  تسمح خاصية باخذ العنصر لاقصى اليسار للوسط
        self.frameleft = Frame(self.master, width=400, bg='#1b9ea4')
        self.frameleft.pack(side=LEFT, fill=Y)
        # -------------------------------------------------------#
        self.FirstName = Label(self.frameleft, text='FirstName', font=('tahoma', 10, 'bold'), width=12, bg='#54b4e8')
        self.FirstName.place(x=10, y=202)
        self.LastName = Label(self.frameleft, text='LastName', font=('tahoma', 10, 'bold'), width=12, bg='#54b4e8')
        self.LastName.place(x=10, y=262)
        self.CIN = Label(self.frameleft, text='CIN', font=('tahoma', 10, 'bold'), width=12, bg='#54b4e8')
        self.CIN.place(x=10, y=322)
        self.Email = Label(self.frameleft, text='Email', font=('tahoma', 10, 'bold'), width=12, bg='#54b4e8')
        self.Email.place(x=10, y=382)
        self.Phone = Label(self.frameleft, text='Phone', font=('tahoma', 10, 'bold'), width=12, bg='#54b4e8')
        self.Phone.place(x=10, y=442)
        self.Date = Label(self.frameleft, text='Date', font=('tahoma', 10, 'bold'), width=12, bg='#54b4e8')
        self.Date.place(x=10, y=502)
        self.id_collegesL = Label(self.frameleft, text='id_colleges', font=('tahoma', 10, 'bold'), width=12,
                                  bg='#54b4e8')
        self.id_collegesL.place(x=10, y=562)
        self.id_TecherL = Label(self.frameleft, text='id_Techer', font=('tahoma', 10, 'bold'), width=12, bg='#54b4e8')
        self.id_TecherL.place(x=10, y=622)

        # الحصول على \
        # الدالة StringVar() في بايثون هي دالة لإنشاء متغير نصي. يمكن استخدام هذا المتغير لربطه بعناصر واجهة المستخدم الرسومية، مثل الحقول النصية، لإنشاء ربط ديناميكي بين عنصر واجهة المستخدم وبيانات التطبيق.
        self.first = StringVar()
        self.last = StringVar()
        self.cin = StringVar()
        self.email = StringVar()
        self.phone = StringVar()
        self.date = StringVar()
        self.id_Teacher1 = StringVar()
        self.id_colleges1 = StringVar()

        self.FirstNameEntry = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'), textvariable=self.first, bd=2)
        self.FirstNameEntry.place(x=120, y=200, width=200, height=30)
        self.LastNameEntry = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'), textvariable=self.last, bd=2)
        self.LastNameEntry.place(x=120, y=260, width=200, height=30)
        self.CINEntry = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'), textvariable=self.cin, bd=2)
        self.CINEntry.place(x=120, y=320, width=200, height=30)
        self.EmailEntry = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'), textvariable=self.email, bd=2)
        self.EmailEntry.place(x=120, y=380, width=200, height=30)
        self.PhoneEntry = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'), textvariable=self.phone, bd=2)
        self.PhoneEntry.place(x=120, y=440, width=200, height=30)
        self.DateEntry = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'), textvariable=self.date, bd=2)
        self.DateEntry.place(x=120, y=500, width=200, height=30)
        self.id_colleges = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'),
                                 textvariable=self.id_colleges1, bd=2)
        self.id_colleges.place(x=120, y=560, width=200, height=30)
        self.id_Teacher = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'),
                                textvariable=self.id_Teacher1, bd=2)
        self.id_Teacher.place(x=120, y=620, width=200, height=30)

        self.var = IntVar()
        self.ra = Radiobutton(self.frameleft, text='Female', font=('Tahoma', 12, 'bold'), variable=self.var, value=1, bg='#54b4e8')
        self.ra.place(x=100, y=680)

        self.ra1 = Radiobutton(self.frameleft, text='Male', font=('Tahoma', 12, 'bold'), variable=self.var, value=2,
                               bg='#54b4e8')
        self.ra1.place(x=200, y=680)

        self.img0 = Image.open('image/delete.png')
        self.img0.thumbnail((30, 30))
        self.new_im0 = ImageTk.PhotoImage(self.img0)

        self.img1 = Image.open('image/add-file.png')
        self.img1.thumbnail((30, 30))
        self.new_im1 = ImageTk.PhotoImage(self.img1)

        self.img2 = Image.open('image/rotation.png')
        self.img2.thumbnail((30, 30))
        self.new_im2 = ImageTk.PhotoImage(self.img2)

        self.img3 = Image.open('image/cleaning.png')
        self.img3.thumbnail((30, 30))
        self.new_im3 = ImageTk.PhotoImage(self.img3)

        self.img4 = Image.open('image/visual.png')
        self.img4.thumbnail((30, 30))
        self.new_im4 = ImageTk.PhotoImage(self.img4)

        self.img00 = Image.open('image/new_add_user_16734.png')
        self.img00.thumbnail((200, 200))
        self.new_im00 = ImageTk.PhotoImage(self.img00)

        self.lab = Label(self.frameleft, height=150, width=150, image=self.new_im00, bd=5)
        self.lab.place(x=10, y=20)

        self.ptp = Button(self.frameleft, text="أضافة صورة", command=self.open_files1, bg='#54b4e8',
                          activeforeground='white', activebackground='#750E21', font=('tahoma', 10, 'bold'),
                          cursor='plus', bd=10)
        self.ptp.place(x=250, y=80, height=50, width=100)

        self.add = Button(self.frameleft, command=self.add, image=self.new_im1, bg='#E5E7E9', activeforeground='white',
                          activebackground='#750E21', font=('tahoma', 10, 'bold'), cursor='plus',bd=15)
        self.add.place(x=30, y=750, width=60, height=60)
        self.Update = Button(self.frameleft, command=self.update, image=self.new_im2, bg='#E5E7E9',
                             activeforeground='white', activebackground='#750E21', font=('tahoma', 10, 'bold'),
                             cursor='plus',bd=15)
        self.Update.place(x=105, y=750, width=60, height=60)
        self.Delete = Button(self.frameleft, command=self.delete, image=self.new_im0, bg='#E5E7E9',
                             activeforeground='white', activebackground='#750E21', font=('tahoma', 10, 'bold'),
                             cursor='mouse',bd=15)
        self.Delete.place(x=180, y=750, width=60, height=60)
        self.Show = Button(self.frameleft, command=self.read, image=self.new_im4, bg='#E5E7E9',
                           activeforeground='white', activebackground='#750E21', font=('tahoma', 10, 'bold'),
                           cursor='plus',bd=15)
        self.Show.place(x=255, y=750, width=60, height=60)
        self.Rest = Button(self.frameleft, command=self.Reset, image=self.new_im3, bg='#E5E7E9',
                           activeforeground='white', activebackground='#750E21', font=('tahoma', 10, 'bold'),
                           cursor='plus',bd=15)
        self.Rest.place(x=330, y=750, width=60, height=60)

        # ------------Start right top -----------------------#
        self.frameright = Frame(self.master, bg='#D0D3D4')
        self.frameright.pack(side=LEFT, fill=BOTH)
        # ------------Start right top -----------------------#
        self.framerighttop = Frame(self.frameright, height=50, pady=5, padx=5, bg='#E5E7E9')
        self.framerighttop.pack(fill=X)

        self.searchStudent = Entry(self.framerighttop, fg='#4F4F4F', font=('tahoma', 12, 'bold'), width=110)
        self.searchStudent.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
        self.ButtonSearch = Button(self.framerighttop, command=self.search, text="Search", fg='#4F4F4F',
                                   font=('tahoma', 12, 'bold'), width=50, bd=15 ,bg='#54b4e8')
        self.ButtonSearch.grid(row=0, column=1, sticky='nsew', pady=10, padx=10)

        self.framerighttop.grid_columnconfigure(0, weight=1)
        self.framerighttop.grid_columnconfigure(1, weight=1)

        # -------------------------- Frame Top View --------------------------#
        self.frameview = Frame(self.frameright)
        self.frameview.pack(fill=BOTH)
        self.scrollbar = Scrollbar(self.frameview, orient=VERTICAL)
        self.table = ttk.Treeview(self.frameview, columns=("ID", "FirstName", "LastName", "CIN", "Email", "Phone", "Date", "id_colleges", "id_Teacher", "Gender", 'photo'), show='headings', yscrollcommand=self.scrollbar.set, height=500)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.table.pack(fill=BOTH)
        # self.img111 = Image.open('C:\\Users\\ahmed\\Desktop\\image\\paython.png')
        # self.img111.thumbnail((200, 200))
        # self.ph = ImageTk.PhotoImage(self.img111)
        # data = self.img111.tobytes()
        # self.ph = PhotoImage(file="C:\\Users\\ahmed\\Desktop\\image\\paython.png")
        # self.lF = LabelFrame(self.frameleft)
        # self.lF.place(x=40, y=10)




        self.table.heading("ID", text="ID")
        self.table.heading("FirstName", text="FirstName")
        self.table.heading("LastName", text="LastName")
        self.table.heading("CIN", text="CIN")
        self.table.heading("Email", text="Email")
        self.table.heading("Phone", text="Phone")
        self.table.heading("Date", text="Date")
        self.table.heading("id_colleges", text="id_colleges")
        self.table.heading("id_Teacher", text="id_Teacher")
        self.table.heading("Gender", text="Gender")
        self.table.heading("photo", text="photo")

        self.table.column("ID", anchor=W, width=10)  # بلظهار القيم في الجدول في الجانب الايسر وضعنا w
        self.table.column("FirstName", anchor=W, width=130)
        self.table.column("LastName", anchor=W, width=130)
        self.table.column("CIN", anchor=W, width=80)
        self.table.column("Email", anchor=W, width=150)
        self.table.column("Phone", anchor=W, width=100)
        self.table.column("Date", anchor=W, width=130)
        self.table.column("id_Teacher", anchor=W, width=40)
        self.table.column("id_colleges", anchor=W, width=40)
        self.table.column("Gender", anchor=W, width=40)
        self.table.column("photo", anchor=W, width=40)
        # self.read()
        self.table.bind('<ButtonRelease-1>', self.show)

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

        # self.ptp.bind("<Button-1>", self.open_files1)

    def open_files1(self):
        try:
            f_type = [('Png files','*.png'),('Jpg files', '*.jpg')]
            # فتح نافذة تحديد الملفات
            self.filenames = filedialog.askopenfilename(filetypes=f_type , parent=self.master)
            # معالجة الملفات
            # قراءة الصورة
            if self.filenames:
                self.image = Image.open(self.filenames)
                self.image.thumbnail((150, 150))
                # إنشاء صورة tkinter
                self.tkimage = ImageTk.PhotoImage(self.image)
                # if hasattr(self, 'lab'):
                #     # إذا كان هناك صورة معروضة بالفعل، قم بإزالتها
                #     self.lab.pack_forget()
                # # إضافة الصورة إلى النافذة
                self.lab["image"]=self.tkimage
                self.lab.image = self.tkimage
        except:
            mb.showerror('error', 'لم يتم اضافة صورة',parent = self.master)
    def on_enter(self, ev):
        self.add['background'] = '#213363'

    def on_leve(self, ev):
        self.add['background'] = '#E5E7E9'

    def on_enter1(self, ev):
        self.Update['background'] = '#213363'

    def on_leve1(self, ev):
        self.Update['background'] = '#E5E7E9'

    def on_enter2(self, ev):
        self.Delete['background'] = '#213363'

    def on_leve2(self, ev):
        self.Delete['background'] = '#E5E7E9'

    def on_enter3(self, ev):
        self.Show['background'] = '#213363'

    def on_leve3(self, ev):
        self.Show['background'] = '#E5E7E9'

    def on_enter4(self, ev):
        self.Rest['background'] = '#213363'

    def on_leve4(self, ev):
        self.Rest['background'] = '#E5E7E9'

    def add(self):
        mydp = mc.connect(host='localhost',
                          user='root',
                          password='',
                          database="un")
        mycursor = mydp.cursor()
        sql = 'insert into student(FirstName,LastName,CIN,Email,Phone,Date,id_colleges,id_Techer,Gender,image) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        if (len(self.FirstNameEntry.get()) == 0 or len(self.LastNameEntry.get()) == 0 or len(
                self.CINEntry.get()) == 0 or len(self.EmailEntry.get()) == 0 or len(self.PhoneEntry.get()) == 0 or len(
                self.DateEntry.get()) == 0 or len(self.id_colleges.get()) == 0 or len(self.id_Teacher.get()) == 0):
            mb.showerror('Error', 'all Data is Empty', parent=self.master)
        else:
            st = self.EmailEntry.get().find('@gmail.com')
            # الحصول على التاريخ
            if self.FirstNameEntry.get().isalpha():
                if self.LastNameEntry.get().isalpha():
                    if self.CINEntry.get().isdigit():
                        if (self.EmailEntry.get()[st] == '@' and st != -1):
                            if self.PhoneEntry.get().isdigit():
                                if self.is_valid_date(self.DateEntry.get()):
                                    if self.var.get() != 0:
                                        if self.lab['image']:
                                            aa = 0
                                            if self.var.get() == 1:
                                                aa = 'Female'
                                            elif self.var.get() == 2:
                                                aa = 'Male'
                                            try:
                                                fb = open(self.filenames, 'rb')
                                                fb = fb.read()

                                                val = (self.FirstNameEntry.get(), self.LastNameEntry.get(),
                                                       self.CINEntry.get(), self.EmailEntry.get(),
                                                       self.PhoneEntry.get(), self.DateEntry.get(),
                                                       self.id_colleges.get(), self.id_Teacher.get(), aa,
                                                       fb)
                                                mycursor.execute(sql, val)
                                                mydp.commit()
                                            except:
                                                mb.showerror('error', 'لم يتم تغيير الصورة')
                                            # id1 = mycursor.lastrowid  # للحصول على اخر id اضيف للجدول
                                            # query = "SELECT * FROM student ORDER BY id DESC LIMIT 1"
                                            # mycursor.execute(query)
                                            # row = mycursor.fetchone()
                                            # if row[6] == None:
                                            #     self.delete1(row[6], id1)
                                            #     mb.showerror("Error","التاريخ الذي ادخلته خاطئ يا حبيبي رجاع دخل بهيك صيغة 2002-5 -1",parent=self.master)
                                            mb.showinfo("Successfully added", 'Data inserted Successfully', parent=self.master)
                                            self.read()
                                            self.Reset()
                                            mydp.close()
                                        else:
                                            mb.showerror('error', 'لم يتم اضافة صورة', parent=self.master)
                                    else:
                                        mb.showerror('Error', "لم يتم اختيار الجنس", parent=self.master)
                                else:
                                    mb.showerror('Error', "التاريخ بياناته غير صحيحة", parent=self.master)
                            else:
                                mb.showerror('Error', "الرقم بياناته غير صحيحة", parent=self.master)
                        else:
                            mb.showerror('Error', "الاسم الأول بياناته غير صحيحة", parent=self.master)
                    else:
                        mb.showerror('Error', "الرقم الجامعي بياناته غير صحيحة", parent=self.master)

                else:
                    mb.showerror('Error', "الاسم الأخير بياناته غير صحيحة", parent=self.master)
            else:
                mb.showerror('Error', "الاسم الأول بياناته غير صحيحة", parent=self.master)

    def read(self):
        mydp = mc.connect(host='localhost',
                          user='root',
                          password='',
                          database="un")
        mycursor = mydp.cursor()
        sql = 'select * from student'
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        self.table.delete(*self.table.get_children())  # كانت سبب في حدوث خطا اثناء استدعاء الدالة
        for mr in myresult:
            self.table.insert('', 'end', iid=mr[0], values=mr)  # الحصول على قيمة iidالمفتاح من القاعدة # على علاقة focus مع
        # execute a select statement to get the date of the last inserted record
        self.iid = None
    def show(self, ev):
        mydp = mc.connect(host='localhost', user='root', password='', database="un")
        mycursor = mydp.cursor()
        try:
            self.iid = self.table.focus()  # الحصول على id الصف المحدد عليه في الجدول
            alldata = self.table.item(self.iid)  # الحصول على العناصر من الصف ووضعها في قاموس
            val = alldata['values']  # قائمة عناصر
            self.first.set(val[1])
            self.last.set(val[2])
            self.cin.set(val[3])
            self.email.set(val[4])
            self.phone.set(val[5])
            self.date.set(val[6])
            self.id_colleges1.set(val[7])
            self.id_Teacher1.set(val[8])
            if val[9] == 'Male':
                a = 2
            elif val[9] == 'Female':
                a = 1
            else:
                a = 0
            self.var.set(a)
            sql = "select image from student where id = '"+self.iid+"'"
            mycursor.execute(sql)
            pho = mycursor.fetchone()
            img = Image.open(io.BytesIO(pho[0]))
            img = img.resize((150, 150))
            phot = ImageTk.PhotoImage(img)

            self.lab["image"] = phot
            self.lab.image = phot
            mydp.close()
        except:
            mb.showerror('error',"لم يتم تحديد سطر",parent=self.master)

    def Reset(self):
        self.FirstNameEntry.delete(0, 'end')
        self.LastNameEntry.delete(0, 'end')
        self.CINEntry.delete(0, 'end')
        self.EmailEntry.delete(0, 'end')
        self.PhoneEntry.delete(0, 'end')
        self.DateEntry.delete(0, 'end')
        self.id_Teacher.delete(0, 'end')
        self.id_colleges.delete(0, 'end')
        self.var.set(-1)

    def delete(self):
        mydp = mc.connect(host='localhost',
                          user='root',
                          password='',
                          database="un")
        mycursor = mydp.cursor()
        try:
            sql = ('delete from student where id = ' + self.iid)
        except:
            mb.showerror('Error', 'لم يتم تجديد سطر', parent =self.master)
            return 0
        try:
            mycursor.execute(sql)
            mydp.commit()
            self.read()
            self.Reset()
            mb.showinfo("Deleted ", 'the Student Deleted', parent=self.master)
        except:
            mb.showerror('Error', 'لايمكن حذف السجل لارتباطه بجداول اخرى', parent =self.master)

        # في حال التاريخ خاطئ

    # def delete1(self, r, id):
    #     mydp = mc.connect(host='localhost',
    #                       user='root',
    #                       password='',
    #                       database="un")
    #     mycursor = mydp.cursor()
    #     query = "SELECT * FROM student ORDER BY id DESC LIMIT 1"
    #     mycursor.execute(query)
    #     row = mycursor.fetchone()
    #     sql = ('delete from student where id = ' + str(row[0]))
    #     mycursor.execute(sql)
    #     mydp.commit()

    def update(self):
        mydp = mc.connect(host='localhost',
                          user='root',
                          password='',
                          database="un")
        mycursor = mydp.cursor()
        try:
            sql = (
                        'update student set FirstName=%s,LastName=%s,CIN=%s,Email=%s,Phone=%s,Date=%s,id_colleges=%s,id_Techer=%s and Gender=%s where id = ' + self.iid)
        except:
            mb.showerror('Error', 'لم يتم تحديد سطر', parent =self.master)
            return 0
        if (len(self.FirstNameEntry.get()) == 0 or len(self.LastNameEntry.get()) == 0 or len(
                self.CINEntry.get()) == 0 or len(self.EmailEntry.get()) == 0 or len(self.PhoneEntry.get()) == 0 or len(
                self.DateEntry.get()) == 0 or len(self.id_colleges.get()) == 0 or len(self.id_Teacher.get()) == 0):
            mb.showerror('Error', 'all Data is Empty', parent=self.master)
        else:
            st = self.EmailEntry.get().find('@gmail.com')
            # الحصول على التاريخ
            if self.FirstNameEntry.get().isalpha():
                if self.LastNameEntry.get().isalpha():
                    if self.CINEntry.get().isdigit():
                        if (self.EmailEntry.get()[st] == '@' and st != -1):
                            if self.PhoneEntry.get().isdigit():
                                if not (self.DateEntry.get().isalpha()):
                                    if self.var != 0:
                                        if self.lab["image"]:
                                            a=''
                                            if self.is_valid_date(self.DateEntry.get()):
                                                if self.var.get() == 1:
                                                    a = "Female"
                                                elif self.var.get() == 2:
                                                    a = 'Male'
                                                val = (
                                                self.first.get(), self.last.get(), self.cin.get(), self.email.get(),
                                                self.phone.get(), self.date.get(), self.id_colleges.get(),
                                                self.id_Teacher.get(), a)
                                                mycursor.execute(sql, val)
                                                mydp.commit()
                                                self.read()
                                                self.Reset()
                                                mb.showinfo("Update ", 'the Student is Update', parent=self.master)

                                            else:
                                                mb.showerror('Error','لم تقم بتحديد صورة', parent =self.master)

                                        else:
                                            mb.showerror('error','لم يتم ادخال صورة',parent = self.master)
                                    else:
                                        mb.showerror('Error', "لم يتم اختيار الجنس", parent=self.master)
                                else:
                                    mb.showerror('Error', "التاريخ بياناته غير صحيحة", parent=self.master)
                            else:
                                mb.showerror('Error', "الرقم بياناته غير صحيحة", parent=self.master)
                        else:
                            mb.showerror('Error', "الاسم الأول بياناته غير صحيحة", parent=self.master)
                    else:
                        mb.showerror('Error', "الرقم الجامعي بياناته غير صحيحة", parent=self.master)

                else:
                    mb.showerror('Error', "الاسم الأخير بياناته غير صحيحة", parent=self.master)
            else:
                mb.showerror('Error', "الاسم الأول بياناته غير صحيحة", parent=self.master)

    def search(self):
        mydp = mc.connect(host='localhost',
                          user='root',
                          password='',
                          database="un")
        mycursor = mydp.cursor()
        if (len(self.searchStudent.get()) != 0):
            if self.searchStudent.get().isdigit():
                try:
                    sql = ('select * from student where id = ' + self.searchStudent.get())
                    mycursor.execute(sql)
                    myresult = mycursor.fetchone()
                    self.table.delete(
                        *self.table.get_children())  # كانت سبب في حدوث خطا اثناء استدعاء الدالة هي لحذف كل سجلات الجدول
                    self.table.insert('', 'end', iid=myresult[0], values=myresult)
                    mydp.commit()
                    mydp.close()
                except:
                    mb.showerror("Error", "الرقم الذي ادخلته غير موجود", parent=self.master)
            else:
                mb.showerror("Error", "البيانات التي ادخلتها غير صحيحة", parent=self.master)
        else:
            mb.showerror('Error', "لم يتم تحديد قيمة", parent=self.master)

    def is_valid_date(self, date_str):
        try:
            # تحويل النص إلى تاريخ
            datetime_obj = datetime.strptime(date_str, '%Y-%m-%d')  # تنسيق التاريخ (YYYY-MM-DD)
            return True  # إذا كان التحويل ناجحًا، يعني أن البيانات صحيحة
        except ValueError:
            return False  # في حالة حدوث خطأ أثناء التحويل، يعني ذلك أن البيانات غير صحيحة