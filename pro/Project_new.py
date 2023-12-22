from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector as mc
import tkinter.messagebox as mb
from datetime import datetime
from tkcalendar import Calendar


class University():
    def __init__(self, window):
        self.master = window
        self.master.title("University Management System ")
        self.height = self.master.winfo_screenheight()
        self.width = self.master.winfo_screenwidth()
        self.master.geometry("{w}x{h}+0+0".format(w=self.width, h=self.height))
        self.master.state('zoomed')
        # ---------- Frame Top Start Here ----------------------------
        self.frametop = Frame(self.master, bg="#1b9ea4", height=150)
        self.frametop.pack(fill=X)
        self.sms = Label(self.frametop, text="University Management System", bg='#1b9ea4', fg='white',
                         font=("tahoma", 50), pady=50)
        self.sms.pack()

        self.bo = ttk.Notebook(self.master , padding=5, takefocus='bottom')
        style = ttk.Style()
        style.configure("TNotebook.Tab", bg='#blue', fg='#17202A', font=('cairo', 15))
        self.tab1 = ttk.Frame(self.bo, width=30)
        self.tab2 = ttk.Frame(self.bo, width=30)
        self.tab3 = ttk.Frame(self.bo, width=30)
        self.tab4 = ttk.Frame(self.bo, width=30)
        self.tab5 = ttk.Frame(self.bo, width=30)
        self.tab6 = ttk.Frame(self.bo, width=30)

        self.bo.add(self.tab1, text='Student')
        self.bo.add(self.tab2, text='Staff')
        self.bo.add(self.tab3, text='Exam')
        self.bo.add(self.tab4, text='Subject')
        self.bo.add(self.tab5, text='College')
        self.bo.add(self.tab6, text='Manegar')

        self.bo.pack(expand=1, fill='both')
        StudentWindow(self.tab1)
        StaffWindow(self.tab2)
        examWindow(self.tab3)
        Subject(self.tab4)
        College(self.tab5)
        maneger(self.tab6)
        self.master.bind("<Right>", self.switch_tab)
        self.master.bind("<Left>", self.switch_tab)

    def switch_tab(self, event):
        current_tab_index = self.bo.index(self.bo.select())
        if event.keysym == "Right":
            next_tab_index = current_tab_index + 1 if current_tab_index < self.bo.index("end") - 1 else 0
        elif event.keysym == "Left":
            next_tab_index = current_tab_index - 1 if current_tab_index > 0 else self.bo.index("end") - 1
        else:
            return

        self.bo.select(next_tab_index)


class StudentWindow:
    def __init__(self, window):
        self.master = window
        # -------------------------------------------------------#
        #  side  تسمح خاصية باخذ العنصر لاقصى اليسار للوسط
        self.frameleft = Frame(self.master, width=400)
        self.frameleft.pack(side=LEFT, fill=Y)
        # -------------------------------------------------------#
        self.FirstName = Label(self.frameleft, text='FirstName', font=('tahoma', 10, 'bold'))
        self.FirstName.place(x=10, y=20)
        self.LastName = Label(self.frameleft, text='LastName', font=('tahoma', 10, 'bold'))
        self.LastName.place(x=10, y=60)
        self.CIN = Label(self.frameleft, text='CIN', font=('tahoma', 10, 'bold'))
        self.CIN.place(x=10, y=100)
        self.Email = Label(self.frameleft, text='Email', font=('tahoma', 10, 'bold'))
        self.Email.place(x=10, y=140)
        self.Phone = Label(self.frameleft, text='Phone', font=('tahoma', 10, 'bold'))
        self.Phone.place(x=10, y=180)
        self.Date = Label(self.frameleft, text='Date', font=('tahoma', 10, 'bold'))
        self.Date.place(x=10, y=220)
        self.id_collegesL = Label(self.frameleft, text='id_colleges', font=('tahoma', 10, 'bold'))
        self.id_collegesL.place(x=10, y=260)
        self.id_TecherL = Label(self.frameleft, text='id_Techer', font=('tahoma', 10, 'bold'))
        self.id_TecherL.place(x=10, y=300)

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

        self.FirstNameEntry = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'), textvariable=self.first)
        self.FirstNameEntry.place(x=100, y=20, width=150, height=30)
        self.LastNameEntry = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'), textvariable=self.last)
        self.LastNameEntry.place(x=100, y=60, width=150, height=30)
        self.CINEntry = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'), textvariable=self.cin)
        self.CINEntry.place(x=100, y=100, width=150, height=30)
        self.EmailEntry = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'), textvariable=self.email)
        self.EmailEntry.place(x=100, y=140, width=150, height=30)
        self.PhoneEntry = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'), textvariable=self.phone)
        self.PhoneEntry.place(x=100, y=180, width=150, height=30)
        self.DateEntry = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'), textvariable=self.date)
        self.DateEntry.place(x=100, y=220, width=150, height=30)
        self.id_colleges = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'),
                                 textvariable=self.id_colleges1)
        self.id_colleges.place(x=100, y=260, width=150, height=30)
        self.id_Teacher = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'),
                                textvariable=self.id_Teacher1)
        self.id_Teacher.place(x=100, y=300, width=150, height=30)

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

        self.add = Button(self.frameleft, command=self.add, image=self.new_im1, bg='#1b9ea4', activeforeground='white',
                          activebackground='#750E21', font=('tahoma', 10, 'bold'), cursor='plus')
        self.add.place(x=30, y=350, width=60, height=60)
        self.Update = Button(self.frameleft, command=self.update, image=self.new_im2, bg='#1b9ea4',
                             activeforeground='white', activebackground='#750E21', font=('tahoma', 10, 'bold'),
                             cursor='plus')
        self.Update.place(x=105, y=350, width=60, height=60)
        self.Delete = Button(self.frameleft, command=self.delete, image=self.new_im0, bg='#1b9ea4',
                             activeforeground='white', activebackground='#750E21', font=('tahoma', 10, 'bold'),
                             cursor='mouse')
        self.Delete.place(x=180, y=350, width=60, height=60)
        self.Show = Button(self.frameleft, command=self.read, image=self.new_im4, bg='#1b9ea4',
                           activeforeground='white', activebackground='#750E21', font=('tahoma', 10, 'bold'),
                           cursor='plus')
        self.Show.place(x=255, y=350, width=60, height=60)
        self.Rest = Button(self.frameleft, command=self.Reset, image=self.new_im3, bg='#1b9ea4',
                           activeforeground='white', activebackground='#750E21', font=('tahoma', 10, 'bold'),
                           cursor='plus')
        self.Rest.place(x=330, y=350, width=60, height=60)

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
        self.table = ttk.Treeview(self.frameview, columns=(
        "ID", "FirstName", "LastName", "CIN", "Email", "Phone", "Date", "id_colleges", "id_Teacher"), show='headings',
                                  yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.table.pack(fill=BOTH)

        self.table.heading("ID", text="ID")
        self.table.heading("FirstName", text="FirstName")
        self.table.heading("LastName", text="LastName")
        self.table.heading("CIN", text="CIN")
        self.table.heading("Email", text="Email")
        self.table.heading("Phone", text="Phone")
        self.table.heading("Date", text="Date")
        self.table.heading("id_colleges", text="id_colleges")
        self.table.heading("id_Teacher", text="id_Teacher")

        self.table.column("ID", anchor=W, width=10)  # بلظهار القيم في الجدول في الجانب الايسر وضعنا w
        self.table.column("FirstName", anchor=W, width=130)
        self.table.column("LastName", anchor=W, width=130)
        self.table.column("CIN", anchor=W, width=80)
        self.table.column("Email", anchor=W, width=150)
        self.table.column("Phone", anchor=W, width=100)
        self.table.column("Date", anchor=W, width=130)
        self.table.column("id_Teacher", anchor=W, width=40)
        self.table.column("id_colleges", anchor=W, width=40)
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

    def on_enter(self, ev):
        self.add['background'] = '#213363'

    def on_leve(self, ev):
        self.add['background'] = '#1b9ea4'

    def on_enter1(self, ev):
        self.Update['background'] = '#213363'

    def on_leve1(self, ev):
        self.Update['background'] = '#1b9ea4'

    def on_enter2(self, ev):
        self.Delete['background'] = '#213363'

    def on_leve2(self, ev):
        self.Delete['background'] = '#1b9ea4'

    def on_enter3(self, ev):
        self.Show['background'] = '#213363'

    def on_leve3(self, ev):
        self.Show['background'] = '#1b9ea4'

    def on_enter4(self, ev):
        self.Rest['background'] = '#213363'

    def on_leve4(self, ev):
        self.Rest['background'] = '#1b9ea4'

    def add(self):
        mydp = mc.connect(host='localhost',
                          user='root',
                          password='',
                          database="un")
        mycursor = mydp.cursor()
        sql = 'insert into student(FirstName,LastName,CIN,Email,Phone,Date,id_colleges,id_Techer) values (%s,%s,%s,%s,%s,%s,%s,%s)'
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
                                    try:
                                        val = (self.FirstNameEntry.get(), self.LastNameEntry.get(), self.CINEntry.get(),
                                               self.EmailEntry.get(), self.PhoneEntry.get(), self.DateEntry.get(),
                                               self.id_colleges.get(), self.id_Teacher.get())
                                        mycursor.execute(sql, val)
                                        mydp.commit()
                                        id1 = mycursor.lastrowid  # للحصول على اخر id اضيف للجدول
                                        query = "SELECT * FROM student ORDER BY id DESC LIMIT 1"
                                        mycursor.execute(query)
                                        row = mycursor.fetchone()
                                        if row[6] == None:
                                            self.delete1(row[6], id1)
                                            mb.showerror("Error",
                                                         "التاريخ الذي ادخلته خاطئ يا حبيبي رجاع دخل بهيك صيغة 2002-5 -1",
                                                         parent=self.master)
                                        else:
                                            self.table.insert('', 'end', values=(
                                            id1, self.FirstNameEntry.get(), self.LastNameEntry.get(),
                                            self.CINEntry.get(), self.EmailEntry.get(), self.PhoneEntry.get(),
                                            self.DateEntry.get(), self.id_Teacher.get(), self.id_colleges.get()))
                                            mb.showinfo("Successfully added", 'Data inserted Successfully',
                                                        parent=self.master)
                                            self.read()
                                            self.Reset()
                                            mydp.close()
                                            # حذف بيانات الEntry
                                            # self.FirstNameEntry.delete(0, 'end')
                                            # self.LastNameEntry.delete(0, 'end')
                                            # self.CINEntry.delete(0, 'end')
                                            # self.EmailEntry.delete(0, 'end')
                                            # self.PhoneEntry.delete(0, 'end')
                                            # self.DateEntry.delete(0, 'end')
                                            # self.last_id = mycursor.lastrowid
                                            # sss="SELECT Date FROM student WHERE id = %s" + str(self.last_id)
                                            # sqll = mycursor.execute(sss)
                                            # print(sqll)
                                    except:
                                        mb.showerror("Error", "رقم المدرس أو رقم الكلية غير موجود")
                                else:
                                    mb.showerror('Error', "التاريخ بياناته غير صحيحة")
                            else:
                                mb.showerror('Error', "الرقم بياناته غير صحيحة")
                        else:
                            mb.showerror('Error', "الاسم الأول بياناته غير صحيحة")
                    else:
                        mb.showerror('Error', "الرقم الجامعي بياناته غير صحيحة")

                else:
                    mb.showerror('Error', "الاسم الأخير بياناته غير صحيحة")
            else:
                mb.showerror('Error', "الاسم الأول بياناته غير صحيحة")

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
            self.table.insert('', 'end', iid=mr[0],
                              values=mr)  # الحصول على قيمة iidالمفتاح من القاعدة # على علاقة focus مع
        # execute a select statement to get the date of the last inserted record
        self.iid = None

    def show(self, ev):
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

    def Reset(self):
        self.FirstNameEntry.delete(0, 'end')
        self.LastNameEntry.delete(0, 'end')
        self.CINEntry.delete(0, 'end')
        self.EmailEntry.delete(0, 'end')
        self.PhoneEntry.delete(0, 'end')
        self.DateEntry.delete(0, 'end')
        self.id_Teacher.delete(0, 'end')
        self.id_colleges.delete(0, 'end')

    def delete(self):
        mydp = mc.connect(host='localhost',
                          user='root',
                          password='',
                          database="un")
        mycursor = mydp.cursor()
        try:
            sql = ('delete from student where id = ' + self.iid)
        except:
            mb.showerror('Error', 'لم يتم تجديد سطر')
            return 0
        try:
            mycursor.execute(sql)
            mydp.commit()
            self.read()
            self.Reset()
            mb.showinfo("Deleted ", 'the Student Deleted', parent=self.master)
        except:
            mb.showerror('Error', 'لايمكن حذف السجل لارتباطه بجداول اخرى')

        # في حال التاريخ خاطئ

    def delete1(self, r, id):
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
        try:
            sql = (
                        'update student set FirstName=%s,LastName=%s,CIN=%s,Email=%s,Phone=%s,Date=%s,id_colleges=%s,id_Techer=%s where id = ' + self.iid)
        except:
            mb.showerror('Error', 'لم يتم تحديد سطر')
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
                                    try:
                                        if self.is_valid_date(self.DateEntry.get()):
                                            val = (self.first.get(), self.last.get(), self.cin.get(), self.email.get(),
                                                   self.phone.get(), self.date.get(), self.id_colleges.get(),
                                                   self.id_Teacher.get())
                                            mycursor.execute(sql, val)
                                            mydp.commit()
                                            self.read()
                                            self.Reset()
                                            mb.showinfo("Update ", 'the Student is Update', parent=self.master)
                                        else:
                                            mb.showerror('Error', 'التاريخ غير صحيح')
                                    except:
                                        mb.showerror("Error", "رقم المدرس أو رقم الكلية غير موجود", parent=self.master)
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
                    mb.showerror("Error", "الرقم الذي ادخلته غير موجود")
            else:
                mb.showerror("Error", "البيانات التي ادخلتها غير صحيحة")
        else:
            mb.showerror('Error', "لم يتم تحديد قيمة")

    def is_valid_date(self, date_str):
        try:
            # تحويل النص إلى تاريخ
            datetime_obj = datetime.strptime(date_str, '%Y-%m-%d')  # تنسيق التاريخ (YYYY-MM-DD)
            return True  # إذا كان التحويل ناجحًا، يعني أن البيانات صحيحة
        except ValueError:
            return False  # في حالة حدوث خطأ أثناء التحويل، يعني ذلك أن البيانات غير صحيحة


class StaffWindow:
    def __init__(self, window):
        self.master = window
        #  side  تسمح خاصية باخذ العنصر لاقصى اليسار للوسط
        self.frameleft = Frame(self.master, width=400)
        self.frameleft.pack(side=LEFT, fill=Y)
        # -------------------------------------------------------#
        self.FirstName = Label(self.frameleft, text='FirstName', font=('tahoma', 10, 'bold'))
        self.FirstName.place(x=10, y=20)
        self.LastName = Label(self.frameleft, text='LastName', font=('tahoma', 10, 'bold'))
        self.LastName.place(x=10, y=60)
        self.CIN = Label(self.frameleft, text='CIN', font=('tahoma', 10, 'bold'))
        self.CIN.place(x=10, y=100)
        self.Email = Label(self.frameleft, text='Email', font=('tahoma', 10, 'bold'))
        self.Email.place(x=10, y=140)
        self.Phone = Label(self.frameleft, text='Phone', font=('tahoma', 10, 'bold'))
        self.Phone.place(x=10, y=180)
        self.Date = Label(self.frameleft, text='Date', font=('tahoma', 10, 'bold'))
        self.Date.place(x=10, y=220)
        self.Jop = Label(self.frameleft, text='Jop', font=('tahoma', 10, 'bold'))
        self.Jop.place(x=10, y=280)

        # الحصول على \
        # الدالة StringVar() في بايثون هي دالة لإنشاء متغير نصي. يمكن استخدام هذا المتغير لربطه بعناصر واجهة المستخدم الرسومية، مثل الحقول النصية، لإنشاء ربط ديناميكي بين عنصر واجهة المستخدم وبيانات التطبيق.
        self.first = StringVar()
        self.last = StringVar()
        self.cin = StringVar()
        self.email = StringVar()
        self.phone = StringVar()
        self.date = StringVar()
        self.jopEntry = StringVar()

        self.FirstNameEntry = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'), textvariable=self.first)
        self.FirstNameEntry.place(x=100, y=20, width=200, height=30)
        self.LastNameEntry = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'), textvariable=self.last)
        self.LastNameEntry.place(x=100, y=60, width=200, height=30)
        self.CINEntry = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'), textvariable=self.cin)
        self.CINEntry.place(x=100, y=100, width=200, height=30)
        self.EmailEntry = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'), textvariable=self.email)
        self.EmailEntry.place(x=100, y=140, width=200, height=30)
        self.PhoneEntry = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'), textvariable=self.phone)
        self.PhoneEntry.place(x=100, y=180, width=200, height=30)
        self.DateEntry = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'), textvariable=self.date)
        self.DateEntry.place(x=100, y=220, width=200, height=30)
        self.JopEntry = ttk.Combobox(self.frameleft, values=['', 'Professor', 'Employee', 'Technicain'],
                                     font=('tahoma', 10, 'bold'), width=22, state='readonly',
                                     textvariable=self.jopEntry)
        self.JopEntry.place(x=100, y=280)

        self.add = Button(self.frameleft, command=self.add, text="add", bg='#1b9ea4', activeforeground='white',
                          activebackground='#750E21', font=('tahoma', 10, 'bold'), cursor='plus')
        self.add.place(x=30, y=350, width=60, height=60)
        self.Update = Button(self.frameleft, command=self.update, text="Update", bg='#1b9ea4', activeforeground='white',
                             activebackground='#750E21', font=('tahoma', 10, 'bold'), cursor='plus')
        self.Update.place(x=105, y=350, width=60, height=60)
        self.Delete = Button(self.frameleft, command=self.delete, text="Delete", bg='#1b9ea4', activeforeground='white',
                             activebackground='#750E21', font=('tahoma', 10, 'bold'), cursor='mouse')
        self.Delete.place(x=180, y=350, width=60, height=60)
        self.Show = Button(self.frameleft, command=self.read, text="Show", bg='#1b9ea4', activeforeground='white',
                           activebackground='#750E21', font=('tahoma', 10, 'bold'), cursor='plus')
        self.Show.place(x=255, y=350, width=60, height=60)
        self.Rest = Button(self.frameleft, command=self.Reset, text="Rest", bg='#1b9ea4', activeforeground='white',
                           activebackground='#750E21', font=('tahoma', 10, 'bold'), cursor='plus')
        self.Rest.place(x=330, y=350, width=60, height=60)

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
        self.frameview = Frame(self.frameright, height=600)
        self.frameview.pack(fill=Y, padx=10)
        self.scrollbar = Scrollbar(self.frameview, orient=VERTICAL)
        self.table = ttk.Treeview(self.frameview,
                                  columns=("ID", "FirstName", "LastName", "CIN", "Email", "Phone", "Date", "Jop"),
                                  show='headings', yscrollcommand=self.scrollbar.set, height=500)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.table.pack(fill=BOTH)

        self.table.heading("ID", text="ID")
        self.table.heading("FirstName", text="FirstName")
        self.table.heading("LastName", text="LastName")
        self.table.heading("CIN", text="CIN")
        self.table.heading("Email", text="Email")
        self.table.heading("Phone", text="Phone")
        self.table.heading("Date", text="Date")
        self.table.heading("Jop", text="Jop")

        self.table.column("ID", anchor=W, width=10)  # بلظهار القيم في الجدول في الجانب الايسر وضعنا w
        self.table.column("FirstName", anchor=W, width=140)
        self.table.column("LastName", anchor=W, width=140)
        self.table.column("CIN", anchor=W, width=100)
        self.table.column("Email", anchor=W)
        self.table.column("Phone", anchor=W, width=120)
        self.table.column("Date", anchor=W)
        self.table.column("Jop", anchor=W)
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

    def on_enter(self, ev):
        self.add['background'] = '#213363'

    def on_leve(self, ev):
        self.add['background'] = '#1b9ea4'

    def on_enter1(self, ev):
        self.Update['background'] = '#213363'

    def on_leve1(self, ev):
        self.Update['background'] = '#1b9ea4'

    def on_enter2(self, ev):
        self.Delete['background'] = '#213363'

    def on_leve2(self, ev):
        self.Delete['background'] = '#1b9ea4'

    def on_enter3(self, ev):
        self.Show['background'] = '#213363'

    def on_leve3(self, ev):
        self.Show['background'] = '#1b9ea4'

    def on_enter4(self, ev):
        self.Rest['background'] = '#213363'

    def on_leve4(self, ev):
        self.Rest['background'] = '#1b9ea4'

    def add(self):
        mydp = mc.connect(host='localhost',
                          user='root',
                          password='',
                          database="un")
        mycursor = mydp.cursor()
        sql = 'insert into staff(FirstName,LastName,CIN,Email,Phone,Date,Job) values (%s,%s,%s,%s,%s,%s,%s)'
        if (
                self.FirstNameEntry.get() == '' or self.LastNameEntry.get() == '' or self.CINEntry.get() == '' or self.EmailEntry.get() == '' or self.PhoneEntry.get() == '' or self.DateEntry.get() == '' or self.JopEntry.get() == ''):
            mb.showerror('Error', 'all Data is Empty', parent=self.master)
        else:
            st = self.EmailEntry.get().find("@gmail.com")
            if self.FirstNameEntry.get().isalpha():
                if self.LastNameEntry.get().isalpha():
                    if self.CINEntry.get().isdigit():
                        if (self.EmailEntry.get()[st] == '@' and st != -1):
                            if self.PhoneEntry.get().isdigit():
                                if self.is_valid_date(self.DateEntry.get()):
                                    try:
                                        val = (self.FirstNameEntry.get(), self.LastNameEntry.get(), self.CINEntry.get(),
                                               self.EmailEntry.get(), self.PhoneEntry.get(), self.DateEntry.get(),
                                               self.JopEntry.get())
                                        mycursor.execute(sql, val)
                                        mydp.commit()
                                        id1 = mycursor.lastrowid  # للحصول على اخر id اضيف للجدول
                                        query = "SELECT * FROM staff ORDER BY id DESC LIMIT 1"
                                        mycursor.execute(query)
                                        row = mycursor.fetchone()
                                        if row[6] == None:
                                            self.delete1(row[6], id1)
                                            mb.showerror("Error", "التاريخ الذي ادخلته خاطئ يا حبيبي رجاع دخل",
                                                         parent=self.master)
                                        else:
                                            self.table.insert('', 'end', values=(
                                            id1, self.FirstNameEntry.get(), self.LastNameEntry.get(),
                                            self.CINEntry.get(),
                                            self.EmailEntry.get(), self.PhoneEntry.get(), self.DateEntry.get(),
                                            self.JopEntry.get()))
                                            mb.showinfo("Successfully added", 'Data inserted Successfully',
                                                        parent=self.master)
                                            # حذف بيانات الEntry
                                            self.read()
                                            self.Reset()
                                            # self.last_id = mycursor.lastrowid
                                            # sss="SELECT Date FROM student WHERE id = %s" + str(self.last_id)
                                            # sqll = mycursor.execute(sss)
                                            # print(sqll)
                                            mydp.close()
                                    except:
                                        mb.showerror('error', 'التاريخ الذي ادخلته غير موجود ياحبيبي',
                                                     parent=self.master)
                                else:
                                    mb.showerror("Error", "التاريخ عير صحيح", parent=self.master)
                            else:
                                mb.showerror('Error', "رقم الجوال غير صحيح", parent=self.master)
                        else:
                            mb.showerror('Error', "الإيميل غير صحيح", parent=self.master)
                    else:
                        mb.showerror('Error', "حقل الرقم الشخصي بياناته غير صحيحة", parent=self.master)
                else:
                    mb.showerror('Error', "الاسم الاخير  غير صحيح", parent=self.master)
            else:
                mb.showerror('Error', "حقل الاسم الاول بياناته غير صحيحة", parent=self.master)

    def read(self):
        mydp = mc.connect(host='localhost',
                          user='root',
                          password='',
                          database="un")
        mycursor = mydp.cursor()
        sql = 'select * from staff'
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
        self.first.set(val[1])
        self.last.set(val[2])
        self.cin.set(val[3])
        self.email.set(val[4])
        self.phone.set(val[5])
        self.date.set(val[6])
        self.jopEntry.set(val[7])

    def Reset(self):
        self.FirstNameEntry.delete(0, 'end')
        self.LastNameEntry.delete(0, 'end')
        self.CINEntry.delete(0, 'end')
        self.EmailEntry.delete(0, 'end')
        self.PhoneEntry.delete(0, 'end')
        self.DateEntry.delete(0, 'end')
        self.JopEntry.current(0)

    def delete(self):
        mydp = mc.connect(host='localhost',
                          user='root',
                          password='',
                          database="un")
        mycursor = mydp.cursor()
        try:
            sql = ('delete from staff where id = ' + self.iid)
        except:
            mb.showerror('Error', "لم يتم تحديد سطر")
            return 0
        try:
            mycursor.execute(sql)
            mydp.commit()
            self.read()
            self.Reset()
            mb.showinfo("Deleted ", 'the Student Deleted', parent=self.master)
        except:
            mb.showerror('Error', 'لايمكن حذف السجل لارتباطه بجداول اخرى')

        # في حال التاريخ خاطئ

    def delete1(self, r, id):
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
        try:
            sql = (
                        'update staff set FirstName=%s,LastName=%s,CIN=%s,Email=%s,Phone=%s,Date=%s,Job = %s where id = ' + self.iid)
        except:
            mb.showerror('Error', 'لم يتم تحديد سطر')
            return 0
        if (
                self.FirstNameEntry.get() == '' or self.LastNameEntry.get() == '' or self.CINEntry.get() == '' or self.EmailEntry.get() == '' or self.PhoneEntry.get() == '' or self.DateEntry.get() == '' or self.JopEntry.get() == ''):
            mb.showerror('Error', 'all Data is Empty', parent=self.master)
        else:
            st = self.EmailEntry.get().find("@gmail.com")
            if self.FirstNameEntry.get().isalpha():
                if self.LastNameEntry.get().isalpha():
                    if self.CINEntry.get().isdigit():
                        if (self.EmailEntry.get()[st] == '@' and st != -1):
                            if self.PhoneEntry.get().isdigit():
                                if self.is_valid_date(self.DateEntry.get()):
                                    val = (self.first.get(), self.last.get(), self.cin.get(), self.email.get(),
                                           self.phone.get(), self.date.get(), self.JopEntry.get())
                                    mycursor.execute(sql, val)
                                    mydp.commit()
                                    self.read()
                                    self.Reset()
                                    mb.showinfo("Update ", 'the Staff is Update', parent=self.master)
                                else:
                                    mb.showerror('Error', "التاريخ عير صحيح", parent=self.master)
                            else:
                                mb.showerror('Error', "رقم الجوال غير صحيح", parent=self.master)
                        else:
                            mb.showerror('Error', "الإيميل غير صحيح", parent=self.master)
                    else:
                        mb.showerror('Error', "حقل الرقم الشخصي بياناته غير صحيحة", parent=self.master)
                else:
                    mb.showerror('Error', "الاسم الاخير  غير صحيح", parent=self.master)
            else:
                mb.showerror('Error', "حقل الاسم الاول بياناته غير صحيحة", parent=self.master)

    def search(self):
        mydp = mc.connect(host='localhost',
                          user='root',
                          password='',
                          database="un")
        mycursor = mydp.cursor()
        if (len(self.searchStudent.get()) != 0):
            if self.searchStudent.get().isdigit():
                try:
                    sql = ('select * from staff where id = ' + self.searchStudent.get())
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

    def is_valid_date(self, date_str):
        try:
            # تحويل النص إلى تاريخ
            datetime_obj = datetime.strptime(date_str, '%Y-%m-%d')  # تنسيق التاريخ (YYYY-MM-DD)
            return True  # إذا كان التحويل ناجحًا، يعني أن البيانات صحيحة
        except ValueError:
            return False  # في حالة حدوث خطأ أثناء التحويل، يعني ذلك أن البيانات غير صحيحة


class examWindow:
    def __init__(self, window):
        self.master = window
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
        self.TimeLabel.place(x=10, y=450)

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
        self.DateExam.place(x=130, y=250, width=250, height=180)
        self.Time = ttk.Combobox(self.frameleft, values=['', '7:00', '8:00', '9:00', '10:00', '11:00', '12:00', '1:00'],
                                 font=('tahoma', 10, 'bold'), width=29, state='readonly',
                                 textvariable=self.time)
        self.Time.place(x=125, y=450)

        self.add = Button(self.frameleft, command=self.add, text="add", bg='#1b9ea4', activeforeground='white',
                          activebackground='#750E21', font=('tahoma', 10, 'bold'), cursor='plus')
        self.add.place(x=30, y=520, width=60, height=60)
        self.Update = Button(self.frameleft, command=self.update, text="Update", bg='#1b9ea4', activeforeground='white',
                             activebackground='#750E21', font=('tahoma', 10, 'bold'), cursor='plus')
        self.Update.place(x=105, y=520, width=60, height=60)
        self.Delete = Button(self.frameleft, command=self.delete, text="Delete", bg='#1b9ea4', activeforeground='white',
                             activebackground='#750E21', font=('tahoma', 10, 'bold'), cursor='mouse')
        self.Delete.place(x=180, y=520, width=60, height=60)
        self.Show = Button(self.frameleft, command=self.read, text="Show", bg='#1b9ea4', activeforeground='white',
                           activebackground='#750E21', font=('tahoma', 10, 'bold'), cursor='plus')
        self.Show.place(x=255, y=520, width=60, height=60)
        self.Rest = Button(self.frameleft, command=self.Reset, text="Rest", bg='#1b9ea4', activeforeground='white',
                           activebackground='#750E21', font=('tahoma', 10, 'bold'), cursor='plus')
        self.Rest.place(x=330, y=520, width=60, height=60)

        # ------------Start right top -----------------------#
        self.frameright = Frame(self.master, width=700)
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
        self.frameview = Frame(self.frameright, height=50)
        self.frameview.pack(fill=X, padx=10)
        self.scrollbar = Scrollbar(self.frameview, orient=VERTICAL)
        self.table = ttk.Treeview(self.frameview,
                                  columns=(
                                  "ID", "HallName", "ClassRoom", "Professor", "DataExam", "Time", "id_Colleges"),
                                  show='headings', yscrollcommand=self.scrollbar.set, height=500)
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
        self.table.column("Time", anchor=W, width=140)
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

    def on_enter(self, ev):
        self.add['background'] = '#213363'

    def on_leve(self, ev):
        self.add['background'] = '#1b9ea4'

    def on_enter1(self, ev):
        self.Update['background'] = '#213363'

    def on_leve1(self, ev):
        self.Update['background'] = '#1b9ea4'

    def on_enter2(self, ev):
        self.Delete['background'] = '#213363'

    def on_leve2(self, ev):
        self.Delete['background'] = '#1b9ea4'

    def on_enter3(self, ev):
        self.Show['background'] = '#213363'

    def on_leve3(self, ev):
        self.Show['background'] = '#1b9ea4'

    def on_enter4(self, ev):
        self.Rest['background'] = '#213363'

    def on_leve4(self, ev):
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


class Subject:
    def __init__(self, window):
        self.master = window
        # -------------------------------------------------------#
        #  side  تسمح خاصية باخذ العنصر لاقصى اليسار للوسط
        self.frameleft = Frame(self.master, width=400)
        self.frameleft.pack(side=LEFT, fill=Y)
        # -------------------------------------------------------#
        self.nameLable = Label(self.frameleft, text='NameSubject :', font=('tahoma', 10, 'bold'))
        self.nameLable.place(x=10, y=20)
        self.UnitLabel = Label(self.frameleft, text='UnitSubject :', font=('tahoma', 10, 'bold'))
        self.UnitLabel.place(x=10, y=80)

        self.id_teacherL = Label(self.frameleft, text='id_teacher :', font=('tahoma', 10, 'bold'))
        self.id_teacherL.place(x=10, y=140)

        self.id_collegeL = Label(self.frameleft, text='id_college :', font=('tahoma', 10, 'bold'))
        self.id_collegeL.place(x=10, y=200)

        self.StartDateLabel = Label(self.frameleft, text='StartDate :', font=('tahoma', 10, 'bold'))
        self.StartDateLabel.place(x=10, y=250)
        self.EndDateLabel = Label(self.frameleft, text='EndDate :', font=('tahoma', 10, 'bold'))
        self.EndDateLabel.place(x=10, y=470)

        # الحصول على \
        # الدالة StringVar() في بايثون هي دالة لإنشاء متغير نصي. يمكن استخدام هذا المتغير لربطه بعناصر واجهة المستخدم الرسومية، مثل الحقول النصية، لإنشاء ربط ديناميكي بين عنصر واجهة المستخدم وبيانات التطبيق.
        self.name = StringVar()
        self.unit = StringVar()
        self.id_teacher1 = StringVar()
        self.id_college1 = StringVar()

        self.nameSubject = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'), textvariable=self.name)
        self.nameSubject.place(x=130, y=20, width=250, height=30)
        self.unitSubject = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'), textvariable=self.unit)
        self.unitSubject.place(x=130, y=80, width=250, height=30)
        self.id_teacherE = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'),
                                 textvariable=self.id_teacher1)
        self.id_teacherE.place(x=130, y=140, width=250, height=30)
        self.id_college = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'),
                                textvariable=self.id_college1)
        self.id_college.place(x=130, y=200, width=250, height=30)

        # الحصول على تاريخ اليوم
        # t = datetime.today()
        # s = str(t).split('-')
        # ss = s[2].split(' ')

        self.StartDate = Calendar(self.frameleft, mindate=datetime.today())
        self.StartDate.place(x=130, y=250, width=250, height=200)
        self.EndDate = Calendar(self.frameleft, selectmode='day', mindate=datetime.today())
        self.EndDate.place(x=130, y=470, width=250, height=200)

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
        self.frameview = Frame(self.frameright)
        self.frameview.pack(fill=BOTH)
        self.scrollbar = Scrollbar(self.frameview, orient=VERTICAL)
        self.table = ttk.Treeview(self.frameview,
                                  columns=(
                                  "ID", "NameSubject", "Units", "StartDate", "EndDate", "id_teacher", "id_collage"),
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
        self.table.column("Units", anchor=W, width=20)
        self.table.column("StartDate", anchor=W)
        self.table.column("EndDate", anchor=W)
        self.table.column("id_teacher", anchor=W, width=30)
        self.table.column("id_collage", anchor=W, width=30)
        # self.read()
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

        self.add = Button(self.frameright, command=self.add, image=self.new_im1, bg='#1b9ea4',
                          activebackground='#750E21', activeforeground='white', font=('Tahoma', 10, 'bold'),
                          cursor='plus')
        self.add.place(x=30, y=300, width=60, height=60)
        self.Update = Button(self.frameright, command=self.update, image=self.new_im2, bg='#1b9ea4',
                             activeforeground='white', activebackground='#750E21', font=('tahoma', 10, 'bold'),
                             cursor='plus')
        self.Update.place(x=105, y=300, width=60, height=60)
        self.Delete = Button(self.frameright, command=self.delete, image=self.new_im0, bg='#1b9ea4',
                             activeforeground='white', activebackground='#750E21', font=('tahoma', 10, 'bold'),
                             cursor='mouse')
        self.Delete.place(x=180, y=300, width=60, height=60)
        self.Show = Button(self.frameright, command=self.read, image=self.new_im4, bg='#1b9ea4',
                           activeforeground='white', activebackground='#750E21', font=('tahoma', 10, 'bold'),
                           cursor='plus')
        self.Show.place(x=255, y=300, width=60, height=60)
        self.Rest = Button(self.frameright, command=self.Reset, image=self.new_im3, bg='#1b9ea4',
                           activeforeground='white', activebackground='#750E21', font=('tahoma', 10, 'bold'),
                           cursor='plus')
        self.Rest.place(x=330, y=300, width=60, height=60)
        self.Re = Button(self.frameright, command=self.registration, text="registration", bg='#0766AD',
                         activeforeground='white', activebackground='#750E21', font=('tahoma', 10, 'bold'),
                         cursor='plus')
        self.Re.place(x=405, y=300, width=80, height=60)

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

    def on_enter(self, ev):
        self.add['background'] = '#213363'

    def on_leve(self, ev):
        self.add['background'] = '#1b9ea4'

    def on_enter1(self, ev):
        self.Update['background'] = '#213363'

    def on_leve1(self, ev):
        self.Update['background'] = '#1b9ea4'

    def on_enter2(self, ev):
        self.Delete['background'] = '#213363'

    def on_leve2(self, ev):
        self.Delete['background'] = '#1b9ea4'

    def on_enter3(self, ev):
        self.Show['background'] = '#213363'

    def on_leve3(self, ev):
        self.Show['background'] = '#1b9ea4'

    def on_enter4(self, ev):
        self.Rest['background'] = '#213363'

    def on_leve4(self, ev):
        self.Rest['background'] = '#1b9ea4'

    def add(self):
        mydp = mc.connect(host='localhost',
                          user='root',
                          password='',
                          database="un")
        mycursor = mydp.cursor()
        sql = 'insert into Subject(Name_Subject,Units,StartDate,EndDate,id_techer , id_colleges) values (%s,%s,%s,%s,%s,%s)'
        if (len(self.nameSubject.get()) == 0 or len(self.unitSubject.get()) == 0 or len(
                self.StartDate.get_date()) == 0 or len(self.EndDate.get_date()) == 0 or len(
                self.id_college.get()) == 0 or len(self.id_teacherE.get()) == 0):
            mb.showerror('Error', 'all Data is Empty')
        else:
            # الحصول على التاريخ
            if self.nameSubject.get().isalpha():
                if self.unitSubject.get().isdigit():
                    try:
                        val = (self.nameSubject.get(), self.unitSubject.get(), self.StartDate.get_date(),
                               self.EndDate.get_date(), self.id_teacherE.get(), self.id_college.get())
                        mycursor.execute(sql, val)
                        mydp.commit()
                        id1 = mycursor.lastrowid  # للحصول على اخر id اضيف للجدول
                        self.table.insert('', 'end', values=(
                        id1, self.nameSubject.get(), self.unitSubject.get(), self.StartDate.get_date(),
                        self.EndDate.get_date(), self.id_teacherE.get(), self.id_college.get()))
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
                        mb.showinfo('Error', " رقم المدرس او رقم الكلية غير صحيح", parent=self.master)
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
        self.id_college.delete(0, 'end')
        self.id_teacherE.delete(0, 'end')

    def delete(self):
        mydp = mc.connect(host='localhost',
                          user='root',
                          password='',
                          database="un")
        mycursor = mydp.cursor()
        try:
            sql = ('delete from subject where id = ' + self.iid)
        except:
            mb.showerror('Error', 'لم يتم تجديد سطر', parent=self.master)
            return 0
        try:
            mycursor.execute(sql)
            mydp.commit()
            self.read()
            self.Reset()
            mb.showinfo("Deleted ", 'the Book Deleted', parent=self.master)
        except:
            mb.showerror('Error', 'لايمكن حذف السجل لارتباطه بجداول اخرى', parent=self.master)

    def update(self):
        mydp = mc.connect(host='localhost',
                          user='root',
                          password='',
                          database="un")
        mycursor = mydp.cursor()
        try:
            sql = (
                        'update subject set Name_Subject=%s,Units=%s,StartDate=%s,EndDate=%s,id_techer=%s,id_colleges=%s where id = ' + self.iid)
        except:
            mb.showerror('Error', 'لم يتم تحديد سطر', parent=self.master)
            return 0
        try:
            val = (self.nameSubject.get(), self.unitSubject.get(), self.StartDate.get_date(), self.EndDate.get_date(),
                   self.id_teacherE.get(), self.id_college.get())
            mycursor.execute(sql, val)
            mydp.commit()
            self.read()
            self.Reset()
            mb.showinfo("Update ", 'the Book is Update', parent=self.master)
        except:
            mb.showerror('Error', 'رقم المدرس او رقم الكلية غير موجود', parent=self.master)

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
            mb.showerror('Error', "لم يتم تحديد قيمة", parent=self.master)

    def registration(self):
        self.reg = Frame(self.frameright, width=400)
        self.reg.pack(side=RIGHT, fill=BOTH, pady=100, padx=100)

        self.table1 = ttk.Treeview(self.reg, columns=("id_Student", "id_Subject", "Result"),
                                   show='headings', height=400)

        self.table1.grid(row=0, column=0)
        self.regL = Frame(self.frameright, width=600)
        self.regL.pack(side=LEFT, fill=BOTH, pady=100)

        self.table1.heading("id_Student", text="id_Student")
        self.table1.heading("id_Subject", text="id_Subject")
        self.table1.heading("Result", text="Result")

        self.table1.column("id_Student", anchor=W, width=130)
        self.table1.column("id_Subject", anchor=W, width=130)
        self.table1.column("Result", anchor=W, width=130)

        self.id_St1 = StringVar()
        self.id_Sub1 = StringVar()
        self.result1 = StringVar()

        self.labAdd = Label(self.regL, text="id_Student", width=10)
        self.labAdd.place(x=10, y=10, height=30)
        self.id_St = Entry(self.regL, width=50, textvariable=self.id_St1)
        self.id_St.place(x=150, y=10, height=30)

        self.labAd = Label(self.regL, text="id_Subject", width=10)
        self.labAd.place(x=10, y=60, height=30)
        self.id_Sub = Entry(self.regL, width=50, textvariable=self.id_Sub1)
        self.id_Sub.place(x=150, y=60, height=30)

        self.lab = Label(self.regL, text="Result", width=10)
        self.lab.place(x=10, y=110, height=30)
        self.result = Entry(self.regL, width=50, textvariable=self.result1)
        self.result.place(x=150, y=110, height=30)

        self.add1 = Button(self.regL, command=self.add_registration, text="Add", bg='#0766AD', width=7, pady=10)
        self.add1.place(x=50, y=200)
        self.Update1 = Button(self.regL, command=self.update1, text="Update", bg='#0766AD', width=7, pady=10)
        self.Update1.place(x=125, y=200)
        self.Delete1 = Button(self.regL, command=self.delete1, text="Delete", bg='#0766AD', width=7, pady=10)
        self.Delete1.place(x=50, y=270)
        self.Show1 = Button(self.regL, command=self.read1, text="Show", bg='#0766AD', width=7, pady=10)
        self.Show1.place(x=125, y=270)
        self.rest = Button(self.regL, command=self.Reset1, text="Rest", bg='#0766AD', width=7, pady=10)
        self.rest.place(x=200, y=200)

        self.table1.bind('<ButtonRelease>', self.show1)

    def add_registration(self):
        mydp = mc.connect(host='localhost',
                          user='root',
                          password='',
                          database="un")
        mycursor = mydp.cursor()
        sql = 'insert into students_grades(id_Student,id_Subject,result) values (%s,%s,%s)'
        if (len(self.id_St.get()) == 0 or len(self.id_Sub.get()) == 0 or len(self.result.get()) == 0):
            mb.showerror('Error', 'يوجد حقول فارغة', parent=self.master)
        else:
            if self.id_St.get().isdigit():
                if self.id_Sub.get().isdigit():
                    if self.result.get().isdigit():
                        try:
                            val = (self.id_St.get(), self.id_Sub.get(), self.result.get())
                            mycursor.execute(sql, val)
                            mydp.commit()
                            id1 = mycursor.lastrowid  # للحصول على اخر id اضيف للجدول
                            self.table1.insert('', 'end',
                                               values=(self.id_St.get(), self.id_Sub.get(), self.result.get()))
                            mb.showinfo("Successfully added", 'Data inserted Successfully', parent=self.master)
                            self.read1()
                            self.Reset1()
                            mydp.close()
                        except:
                            mb.showerror('error', 'رقم الطالب او رقم المادة غير موجود او تم تكرير المفتاح الرئيسي',
                                         parent=self.master)
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
        self.iid = None

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
        mydp = mc.connect(host='localhost', user='root', password='', database="un")
        mycursor = mydp.cursor()
        try:
            if self.val[0] != '':
                sql = ("delete from students_grades where id_student = '" + str(
                    self.val[0]) + "' and id_Subject = '" + str(self.val[1]) + "' ")
                mycursor.execute(sql)
                mydp.commit()
                self.read1()
                self.Reset1()
                mb.showinfo("Deleted ", 'Deleted Successfully', parent=self.master)
                self.val[0] = ''
                self.val[1] = ''
            else:
                mb.showerror('Error', 'لم يتم تحديد سطر', parent=self.master)
        except:
            mb.showerror('Error', "لم يتم تحديد سطر", parent=self.master)

    def update1(self):
        mydp = mc.connect(host='localhost',
                          user='root',
                          password='',
                          database="un")
        mycursor = mydp.cursor()
        try:
            sql = ("update students_grades set id_student=%s,id_Subject=%s,result=%s where id_student = '" + str(
                self.val[0]) + "' and id_Subject = '" + str(self.val[1]) + "' ")
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
                            self.read1()
                            self.Reset1()
                            mb.showinfo("Update ", 'Updated successfully', parent=self.master)
                        except:
                            mb.showerror('error', 'رقم الطالب او رقم المادة غير موجود او تم تكرير المفتاح الرئيسي',
                                         parent=self.master)
                    else:
                        mb.showerror('Error', "حقل رقم الطالب بياناته غير صحيحة")
                else:
                    mb.showerror('Error', "حقل رقم المادة بياناته غير صحيحة")
            else:
                mb.showerror('Error', "حقل النتيجة بياناته غير صحيحة")
        except:
            mb.showerror('Error', 'رقم الطالب او رقم المادة غير موجود', parent=self.master)


class College:
    def __init__(self, window):
        self.master = window
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

        self.NameCollegeE = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'),
                                  textvariable=self.NameCollege)
        self.NameCollegeE.place(x=100, y=50, width=200, height=30)
        self.NumCourseE = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'), textvariable=self.NumCourse)
        self.NumCourseE.place(x=100, y=120, width=200, height=30)
        self.NumTeacherE = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'),
                                 textvariable=self.NumTeacher)
        self.NumTeacherE.place(x=100, y=190, width=200, height=30)

        self.add = Button(self.frameleft, command=self.add, text="add", bg='#1b9ea4', activeforeground='white',
                          activebackground='#750E21', font=('tahoma', 10, 'bold'), cursor='plus')
        self.add.place(x=30, y=350, width=60, height=60)
        self.Update = Button(self.frameleft, command=self.update, text="Update", bg='#1b9ea4', activeforeground='white',
                             activebackground='#750E21', font=('tahoma', 10, 'bold'), cursor='mouse')
        self.Update.place(x=105, y=350, width=60, height=60)
        self.Delete = Button(self.frameleft, command=self.delete, text="Delete", bg='#1b9ea4', activeforeground='white',
                             activebackground='#750E21', font=('tahoma', 10, 'bold'), cursor='mouse')
        self.Delete.place(x=180, y=350, width=60, height=60)
        self.Show = Button(self.frameleft, command=self.read, text="Show", bg='#1b9ea4', activeforeground='white',
                           activebackground='#750E21', font=('tahoma', 10, 'bold'), cursor='mouse')
        self.Show.place(x=255, y=350, width=60, height=60)
        self.Rest = Button(self.frameleft, command=self.Reset, text="Rest", bg='#1b9ea4', activeforeground='white',
                           activebackground='#750E21', font=('tahoma', 10, 'bold'), cursor='mouse')
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
        self.table.column("NameCollege", anchor=W, width=140)
        self.table.column("NumCourse", anchor=W, width=140)
        self.table.column("NumTeacher", anchor=W, width=100)

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

    def on_enter(self, ev):
        self.add['background'] = '#213363'

    def on_leve(self, ev):
        self.add['background'] = '#1b9ea4'

    def on_enter1(self, ev):
        self.Update['background'] = '#213363'

    def on_leve1(self, ev):
        self.Update['background'] = '#1b9ea4'

    def on_enter2(self, ev):
        self.Delete['background'] = '#213363'

    def on_leve2(self, ev):
        self.Delete['background'] = '#1b9ea4'

    def on_enter3(self, ev):
        self.Show['background'] = '#213363'

    def on_leve3(self, ev):
        self.Show['background'] = '#1b9ea4'

    def on_enter4(self, ev):
        self.Rest['background'] = '#213363'

    def on_leve4(self, ev):
        self.Rest['background'] = '#1b9ea4'

    def add(self):
        mydp = mc.connect(host='localhost',
                          user='root',
                          password='',
                          database="un")
        mycursor = mydp.cursor()
        sql = 'insert into colleges(NameCollage,NumCourse,NumTecher) values (%s,%s,%s)'
        if (len(self.NameCollege.get()) == 0 or len(self.NumCourse.get()) == 0 or len(self.NumTeacher.get()) == 0):
            mb.showerror('Error', 'all Data is Empty', parent=self.master)
        else:
            if self.NameCollege.get().isalpha():
                if self.NumCourse.get().isdigit():
                    if self.NumTeacher.get().isdigit():
                        try:
                            val = (self.NameCollege.get(), self.NumCourse.get(), self.NumTeacher.get())
                            mycursor.execute(sql, val)
                            mydp.commit()
                            id1 = mycursor.lastrowid
                            self.table.insert('', 'end', values=(
                            id1, self.NameCollege.get(), self.NumCourse.get(), self.NumTeacher.get()))
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
                            mb.showerror('Error', "يوجد خطا", parent=self.master)
                else:
                    mb.showerror('Error', "حقل عدد المواد بياناته غير صحيحة", parent=self.master)
            else:
                mb.showerror('Error', "حقل عدد المدرسين بياناته غير صحيحة", parent=self.master)

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
            self.table.insert('', 'end', iid=mr[0],
                              values=mr)  # الحصول على قيمة iidالمفتاح من القاعدة # على علاقة focus مع
        # execute a select statement to get the date of the last inserted record
        self.iid = None

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
            mb.showerror('Error', "لم يتم تحديد سطر", parent=self.master)
            return 0
        try:
            mycursor.execute(sql)
            mydp.commit()
            self.read()
            self.Reset()
            mb.showinfo("Deleted ", 'the Student Deleted', parent=self.master)
            self.iid = None
        except:
            mb.showerror('Error', 'لايمكن حذف السجل لارتباطه بجداول اخرى', parent=self.master)

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
            mb.showerror('Error', 'لم يتم تحديد سطر', parent=self.master)
            return 0
        if (len(self.NameCollege.get()) == 0 or len(self.NumCourse.get()) == 0 or len(self.NumTeacher.get()) == 0):
            mb.showerror('Error', 'all Data is Empty', parent=self.master)
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
                            mb.showerror('Error', "عندك خطأ", parent=self.master)
                    else:
                        mb.showerror('Error', "حقل عدد المدرسين بياناته غير صحيحة", parent=self.master)
                else:
                    mb.showerror('Error', "حقل عدد المواد بياناته غير صحيحة", parent=self.master)
            else:
                mb.showerror('Error', "اسم الكلية خاطئ", parent=self.master)

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


class maneger:
    def __init__(self, window):
        self.master = window
        self.height = self.master.winfo_screenheight()
        self.width = self.master.winfo_screenwidth()
        self.img = Image.open("image/clipart2409514.png")
        self.img.thumbnail((200, 200))
        self.new_img = ImageTk.PhotoImage(self.img)
        self.imglabel = Label(self.master, image=self.new_img)
        self.imglabel.pack()

        self.frameEnter = Frame(self.master, height=200, width=500)
        self.frameEnter.pack()

        self.EntryUser = Entry(self.frameEnter, width=25, font=('Tahoma', 12))
        self.EntryUser.grid(row=0, column=1, pady=20)
        self.Entrypass = Entry(self.frameEnter, width=25, font=('Tahoma', 12), show='*')
        self.Entrypass.grid(row=1, column=1, pady=20)

        self.UserLabel = Label(self.frameEnter, text="UserName :", font=('Tahoma', 12, 'bold'))
        self.UserLabel.grid(row=0, column=0)
        self.passLabel = Label(self.frameEnter, text="Password :", font=('Tahoma', 12, 'bold'))
        self.passLabel.grid(row=1, column=0)

        self.Enter = Button(self.frameEnter, command=self.login1, width=25, text="Add user", pady=10, bg='#1b9ea4')
        self.Enter.grid(row=2, column=0, columnspan=2, sticky='snew', pady=7, padx=7)

    def login1(self):
        mydp = mc.connect(host='localhost',
                          user='root',
                          password='',
                          database="un")
        mycursor = mydp.cursor()
        try:
            sql = "select id from loginadmi where Username = '" + self.EntryUser.get() + "' and Password = '" + self.Entrypass.get() + "' "
            mycursor.execute(sql)
            id1 = mycursor.fetchone()
            if (id1[0] == 1):
                window = Toplevel()
                uni = Add_User(window)
                mydp.close()
            else:
                mb.showerror("Error", "هذا ليس حساب المدير أحمد الخضر", parent=self.master)
        except:
            mb.showerror("Error", "هذا ليس حساب المدير أحمد الخضر", parent=self.master)


class Add_User:
    def __init__(self, window):
        self.master = window
        self.height = self.master.winfo_screenheight()
        self.width = self.master.winfo_screenwidth()
        self.master.geometry('600x600+350+100')
        self.master.resizable(width=False, height=False)
        self.img = Image.open("image/clipart2409514.png")
        self.img.thumbnail((200, 200))
        self.new_img = ImageTk.PhotoImage(self.img)
        self.imglabel = Label(self.master, image=self.new_img)
        self.imglabel.pack()
        self.frameEnter = Frame(self.master, height=200, width=500)
        self.frameEnter.pack()

        self.EntryUser1 = Entry(self.frameEnter, width=25, font=('Tahoma', 12))
        self.EntryUser1.grid(row=0, column=1, pady=20)
        self.Entrypass1 = Entry(self.frameEnter, width=25, font=('Tahoma', 12), show='*')
        self.Entrypass1.grid(row=1, column=1, pady=20)
        self.NameAdmin = Entry(self.frameEnter, width=25, font=('Tahoma', 12))
        self.NameAdmin.grid(row=2, column=1, pady=20)

        self.UserLabel = Label(self.frameEnter, text="UserName :", font=('Tahoma', 12, 'bold'))
        self.UserLabel.grid(row=0, column=0)
        self.passLabel = Label(self.frameEnter, text="Password :", font=('Tahoma', 12, 'bold'))
        self.passLabel.grid(row=1, column=0)
        self.NameLabel = Label(self.frameEnter, text="NameAdmin :", font=('Tahoma', 12, 'bold'))
        self.NameLabel.grid(row=2, column=0)

        self.Enter = Button(self.frameEnter, command=self.Log, width=25, text="Add user", pady=10, bg='#1b9ea4',
                            activeforeground='white', activebackground='#750E21', font=('tahoma', 10, 'bold'))
        self.Enter.grid(row=3, column=0, sticky='snew', pady=7, padx=7)
        self.Enter1 = Button(self.frameEnter, command=self.delete_user, width=25, text="delete user", pady=10,
                             bg='#1b9ea4', activeforeground='white', activebackground='#750E21',
                             font=('tahoma', 10, 'bold'))
        self.Enter1.grid(row=3, column=1, sticky='snew', pady=7, padx=7)

        self.Enter.bind("<Enter>", self.on_enter)
        self.Enter.bind("<Leave>", self.on_leve)

        self.Enter1.bind("<Enter>", self.on_enter1)
        self.Enter1.bind("<Leave>", self.on_leve1)

    def on_enter(self, ev):
        self.Enter['background'] = '#213363'

    def on_leve(self, ev):
        self.Enter['background'] = '#1b9ea4'

    def on_enter1(self, ev):
        self.Enter1['background'] = '#213363'

    def on_leve1(self, ev):
        self.Enter1['background'] = '#1b9ea4'

    def Log(self):
        mydp = mc.connect(host='localhost',
                          user='root',
                          password='',
                          database="un")
        mycursor = mydp.cursor()
        sql = "insert into loginadmi(Username,Password ,NameAdmin) values (%s,%s,%s) "

        if (len(self.EntryUser1.get()) == 0 or len(self.EntryUser1.get()) == 0 or len(self.NameAdmin.get()) == 0):
            mb.showerror('Error', 'يوجد حقول فارغة')
        else:
            sql1 = (
                        "select id from loginadmi where Username = '" + self.EntryUser1.get() + "' and Password = '" + self.Entrypass1.get() + "' and NameAdmin = '" + self.NameAdmin.get() + "' ")
            mycursor.execute(sql1)
            qq = mycursor.fetchone()
            if qq == None:
                if self.NameAdmin.get().isalpha():
                    val = (self.EntryUser1.get(), self.Entrypass1.get(), self.NameAdmin.get())
                    mycursor.execute(sql, val)
                    mydp.commit()
                    mb.showinfo('Message', "تمت اضافة الحساب", parent=self.master)
                    mydp.close()
                else:
                    mb.showerror('Error', 'الاسم غير صحيح', parent=self.master)
                self.Reset1()
            else:
                mb.showerror('Error', 'الحساب موجود بالفعل', parent=self.master)
                self.Reset1()

    def delete_user(self):
        mydp = mc.connect(host='localhost',
                          user='root',
                          password='',
                          database="un")
        mycursor = mydp.cursor()
        try:
            a = (
                        "select id from loginadmi where Username = '" + self.EntryUser1.get() + "' and Password = '" + self.Entrypass1.get() + "' and NameAdmin = '" + self.NameAdmin.get() + "' ")
            mycursor.execute(a)
            mb1 = mycursor.fetchone()
            if mb1 != None:
                sql = (
                            "delete from loginadmi  where Username = '" + self.EntryUser1.get() + "' and Password = '" + self.Entrypass1.get() + "' and NameAdmin = '" + self.NameAdmin.get() + "'")
                mycursor.execute(sql)
                mydp.commit()
                mb.showinfo('Message', "نم حذف الحساب", parent=self.master)
                mydp.close()
            else:
                mb.showerror('Message', "الحساب غير موجود", parent=self.master)
            self.Reset1()
        except:
            mb.showerror('Message', "الحساب غير موجود", parent=self.master)

    def Reset1(self):
        self.EntryUser1.delete(0, 'end')
        self.Entrypass1.delete(0, 'end')
        self.NameAdmin.delete(0, 'end')


if (__name__ == '__main__'):
    window = Tk()
    std = University(window)
    mainloop()
