from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector as mc
import tkinter.messagebox as mb
from datetime import datetime

class Staff:
    def __init__(self ,centerFrame):
        self.centerFrame=centerFrame
        self.staffFrame = Frame(self.centerFrame, pady=10, padx=10)
        self.staffFrame.grid(row=0, column=2,sticky='senw',pady=5)
        self.img2 = Image.open('image/8439492.png')
        self.img2.thumbnail((200, 200))
        self.new_img2 = ImageTk.PhotoImage(self.img2)

        self.imgStaff = Label(self.staffFrame, image=self.new_img2,pady=10,padx=10)
        self.imgStaff.pack()
        self.ButtonStaff= Button(self.staffFrame,command=self.opensstaffwindo, text="Staff Management", bg='#1b9ea4', fg='white', padx=10,
                                       pady=10,font=("tahoma",10 , 'bold'))
        self.ButtonStaff.pack()

    def opensstaffwindo(self):
        stf = StaffWindow()


class StaffWindow:
    def __init__(self):
        self.master = Toplevel()
        self.master.title('(✿◡‿◡)Staff Management System(✿◡‿◡)')
        self.master.geometry("800x600+150+150")
        #  side  تسمح خاصية باخذ العنصر لاقصى اليسار للوسط
        self.frameleft = Frame(self.master, width=400,bg='#1b9ea4')
        self.frameleft.pack(side=LEFT, fill=Y)
        # -------------------------------------------------------#
        self.FirstName = Label(self.frameleft, text='FirstName', font=('tahoma', 10, 'bold'),width=12)
        self.FirstName.place(x=10, y=22)
        self.LastName = Label(self.frameleft, text='LastName', font=('tahoma', 10, 'bold'),width=12)
        self.LastName.place(x=10, y=62)
        self.CIN = Label(self.frameleft, text='CIN', font=('tahoma', 10, 'bold'),width=12)
        self.CIN.place(x=10, y=102)
        self.Email = Label(self.frameleft, text='Email', font=('tahoma', 10, 'bold'),width=12)
        self.Email.place(x=10, y=142)
        self.Phone = Label(self.frameleft, text='Phone', font=('tahoma', 10, 'bold'),width=12)
        self.Phone.place(x=10, y=182)
        self.Date = Label(self.frameleft, text='Date', font=('tahoma', 10, 'bold'),width=12)
        self.Date.place(x=10, y=222)
        self.Jop = Label(self.frameleft, text='Jop', font=('tahoma', 10, 'bold'),width=12)
        self.Jop.place(x=10, y=282)


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
        self.FirstNameEntry.place(x=130, y=20, width=250, height=30)
        self.LastNameEntry = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'), textvariable=self.last)
        self.LastNameEntry.place(x=130, y=60, width=250, height=30)
        self.CINEntry = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'), textvariable=self.cin)
        self.CINEntry.place(x=130, y=100, width=250, height=30)
        self.EmailEntry = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'), textvariable=self.email)
        self.EmailEntry.place(x=130, y=140, width=250, height=30)
        self.PhoneEntry = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'), textvariable=self.phone)
        self.PhoneEntry.place(x=130, y=180, width=250, height=30)
        self.DateEntry = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'), textvariable=self.date)
        self.DateEntry.place(x=130, y=220, width=250, height=30)
        self.JopEntry = ttk.Combobox(self.frameleft, values=['', 'Professor', 'Employee', 'Technicain'],font=('tahoma', 10, 'bold'), width=25 , state='readonly',textvariable=self.jopEntry)
        self.JopEntry.place(x=130, y=280)

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

        self.add = Button(self.frameleft, command=self.add, image=self.new_im0, bg='#D0D3D4',activeforeground='white',activebackground='#750E21' , font=('tahoma',10,'bold'),cursor='plus')
        self.add.place(x=30, y=350, width=60, height=60)
        self.Update = Button(self.frameleft, command=self.update,image=self.new_im1, bg='#D0D3D4',activeforeground='white',activebackground='#750E21' , font=('tahoma',10,'bold'),cursor='plus')
        self.Update.place(x=105, y=350, width=60, height=60)
        self.Delete = Button(self.frameleft, command=self.delete, image=self.new_im2, bg='#D0D3D4',activeforeground='white',activebackground='#750E21' , font=('tahoma',10,'bold'),cursor='mouse')
        self.Delete.place(x=180, y=350, width=60, height=60)
        self.Show = Button(self.frameleft, command=self.read, image=self.new_im3, bg='#D0D3D4',activeforeground='white',activebackground='#750E21' , font=('tahoma',10,'bold'),cursor='plus')
        self.Show.place(x=255, y=350, width=60, height=60)
        self.Rest = Button(self.frameleft, command=self.Reset, image=self.new_im4, bg='#D0D3D4',activeforeground='white',activebackground='#750E21' , font=('tahoma',10,'bold'),cursor='plus')
        self.Rest.place(x=330, y=350, width=60, height=60)

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
        self.frameview = Frame(self.frameright, bg='red')
        self.frameview.pack(fill=BOTH)
        self.scrollbar = Scrollbar(self.frameview, orient=VERTICAL)
        self.table = ttk.Treeview(self.frameview,
                                  columns=("ID", "FirstName", "LastName", "CIN", "Email", "Phone", "Date","Jop"),
                                  show='headings', yscrollcommand=self.scrollbar.set,height=500)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.table.pack(fill=BOTH)

        self.table.heading("ID", text="ID")
        self.table.heading("FirstName", text="FirstName")
        self.table.heading("LastName", text="LastName")
        self.table.heading("CIN", text="CIN")
        self.table.heading("Email", text="Email")
        self.table.heading("Phone", text="Phone")
        self.table.heading("Date", text="Date")
        self.table.heading("Jop",text="Jop")

        self.table.column("ID", anchor=W, width=10)  # بلظهار القيم في الجدول في الجانب الايسر وضعنا w
        self.table.column("FirstName", anchor=W , width=140)
        self.table.column("LastName", anchor=W , width=140)
        self.table.column("CIN", anchor=W , width=100)
        self.table.column("Email", anchor=W)
        self.table.column("Phone", anchor=W, width=120)
        self.table.column("Date", anchor=W)
        self.table.column("Jop" , anchor=W)
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
        sql = 'insert into staff(FirstName,LastName,CIN,Email,Phone,Date,Job) values (%s,%s,%s,%s,%s,%s,%s)'
        if (self.FirstNameEntry.get() == '' or self.LastNameEntry.get() == '' or self.CINEntry.get() == '' or self.EmailEntry.get() == '' or self.PhoneEntry.get() == '' or self.DateEntry.get() == '' or self.JopEntry.get()==''):
            mb.showerror('Error', 'all Data is Empty' ,parent = self.master)
        else:
            st = self.EmailEntry.get().find("@gmail.com")
            if self.FirstNameEntry.get().isalpha():
                if self.LastNameEntry.get().isalpha():
                    if self.CINEntry.get().isdigit():
                        if (self.EmailEntry.get()[st]=='@' and st !=-1):
                            if self.PhoneEntry.get().isdigit():
                                if self.is_valid_date(self.DateEntry.get()):
                                    try:
                                        val = (self.FirstNameEntry.get(), self.LastNameEntry.get(), self.CINEntry.get(),self.EmailEntry.get(), self.PhoneEntry.get(), self.DateEntry.get(),self.JopEntry.get())
                                        mycursor.execute(sql, val)
                                        mydp.commit()
                                        id1 = mycursor.lastrowid  # للحصول على اخر id اضيف للجدول
                                        query = "SELECT * FROM staff ORDER BY id DESC LIMIT 1"
                                        mycursor.execute(query)
                                        row = mycursor.fetchone()
                                        if row[6] == None:
                                            self.delete1(row[6], id1)
                                            mb.showerror("Error", "التاريخ الذي ادخلته خاطئ يا حبيبي رجاع دخل",parent=self.master)
                                        else:
                                            self.table.insert('', 'end', values=(id1, self.FirstNameEntry.get(), self.LastNameEntry.get(),
                                            self.CINEntry.get(),
                                            self.EmailEntry.get(), self.PhoneEntry.get(), self.DateEntry.get(),
                                            self.JopEntry.get()))
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
                                        mb.showerror('error', 'التاريخ الذي ادخلته غير موجود ياحبيبي', parent=self.master)
                                else:
                                    mb.showerror("Error","التاريخ عير صحيح", parent=self.master)
                            else:
                                mb.showerror('Error',"رقم الجوال غير صحيح", parent=self.master)
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
            self.table.insert('', 'end', iid=mr[0],values=mr)  # الحصول على قيمة iidالمفتاح من القاعدة # على علاقة focus مع
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
            mb.showerror('Error','لايمكن حذف السجل لارتباطه بجداول اخرى')

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
            sql = ('update staff set FirstName=%s,LastName=%s,CIN=%s,Email=%s,Phone=%s,Date=%s,Job = %s where id = ' + self.iid)
        except:
            mb.showerror('Error', 'لم يتم تحديد سطر')
            return 0
        if (self.FirstNameEntry.get() == '' or self.LastNameEntry.get() == '' or self.CINEntry.get() == '' or self.EmailEntry.get() == '' or self.PhoneEntry.get() == '' or self.DateEntry.get() == '' or self.JopEntry.get()==''):
            mb.showerror('Error', 'all Data is Empty' ,parent = self.master)
        else:
            st = self.EmailEntry.get().find("@gmail.com")
            if self.FirstNameEntry.get().isalpha():
                if self.LastNameEntry.get().isalpha():
                    if self.CINEntry.get().isdigit():
                        if (self.EmailEntry.get()[st] == '@' and st != -1):
                            if self.PhoneEntry.get().isdigit():
                                if self.is_valid_date(self.DateEntry.get()):
                                    val = (self.first.get(), self.last.get(), self.cin.get(), self.email.get(), self.phone.get(),self.date.get(), self.JopEntry.get())
                                    mycursor.execute(sql, val)
                                    mydp.commit()
                                    self.read()
                                    self.Reset()
                                    mb.showinfo("Update ", 'the Staff is Update', parent=self.master)
                                else:
                                    mb.showerror('Error',"التاريخ عير صحيح", parent=self.master)
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
                    mb.showerror("Error","الرقم الذي ادخلته غير موجود")
            else:
                mb.showerror("Error","البيانات التي ادخلتها غير صحيحة")
        else:
            mb.showerror('Error',"لم يتم تحديد قيمة")
    def is_valid_date(self,date_str):
        try:
            # تحويل النص إلى تاريخ
            datetime_obj = datetime.strptime(date_str, '%Y-%m-%d')  # تنسيق التاريخ (YYYY-MM-DD)
            return True  # إذا كان التحويل ناجحًا، يعني أن البيانات صحيحة
        except ValueError:
            return False  # في حالة حدوث خطأ أثناء التحويل، يعني ذلك أن البيانات غير صحيحة

