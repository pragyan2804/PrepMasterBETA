from tkinter import *
import tkinter.messagebox as mb
from tkinter import ttk
import mysql.connector as mysql

def insert():
    admno =e_admno.get()
    name =e_name.get()
    classec=e_classec.get()
    date=e_date.get()
    event=e_event.get()
    prize=e_prize.get()
    organization=e_organization.get()

    if(admno=="" or name=="" or classec=="" or date=="" or prize=="" or organization==""):
        mb.showerror("Insert Status", "All fields are required")
    else:
        con = mysql.connect(port=3307,host="localhost", user="root", password='comp', database="project")
        cursor = con.cursor()
        cursor.execute("Insert into record values('"+admno+"','"+name+"','"+classec+"','"+date+"','"+prize+"','"+organization+"','"+event+"')")
        cursor.execute("commit")
        e_admno.delete(0, 'end')
        e_name.delete(0, 'end')
        e_classec.delete(0, 'end')
        e_date.delete(0, 'end')
        e_event.delete(0, 'end')
        e_prize.delete(0, 'end')
        e_organization.delete(0, 'end')
        show()
        mb.showinfo("Insert Status", "Inserted Successfully")
        con.close()
        
def delete():
    con = mysql.connect(host="localhost", user="root", password='comp', database="project",port=3307)
    cursor = con.cursor()
    cursor.execute("Select admission_number from record")
    admnos=cursor.fetchall()
    cursor.execute("Select Name_Of_Event from record")
    eventos=cursor.fetchall()
    if(e_admno.get() == "" or e_event.get() == ""):
        mb.showerror("Delete Status", "Minimum Requirements of fields to delete a record:\nAdmission number and Name of Event")
        e_admno.delete(0, 'end')
        e_name.delete(0, 'end')
        e_classec.delete(0, 'end')
        e_date.delete(0, 'end')
        e_event.delete(0, 'end')
        e_prize.delete(0, 'end')
        e_organization.delete(0, 'end')
    elif tuple([int(e_admno.get()),]) not in admnos or tuple([(e_event.get()),]) not in eventos :
        mb.showerror("Deleting Status", "No record exists for Admission Number " + e_admno.get() + "\nand with Name Of Event as "+e_event.get()+" in order to delete")
        e_admno.delete(0, 'end')
        e_name.delete(0, 'end')
        e_classec.delete(0, 'end')
        e_date.delete(0, 'end')
        e_event.delete(0, 'end')
        e_prize.delete(0, 'end')
        e_organization.delete(0, 'end')
    else:
        answer = mb.askquestion("Delete Permission","Are You sure you want to delete this record")
        if answer == ("yes"):
            cursor.execute("delete from record where admission_number="+e_admno.get()+" and Name_Of_Event='"+e_event.get()+"'")
            cursor.execute("commit")
        else:
            pass
        e_admno.delete(0, 'end')
        e_name.delete(0, 'end')
        e_classec.delete(0, 'end')
        e_date.delete(0, 'end')
        e_event.delete(0, 'end')
        e_prize.delete(0, 'end')
        e_organization.delete(0, 'end')
        show()
        mb.showinfo("Delete Status", "Record deleted Successfully")
        con.close()

def update():
    con = mysql.connect(host="localhost", user="root", password='comp', database="project",port=3307)
    cursor=con.cursor()
    admno =e_admno.get()
    name =e_name.get()
    classec=e_classec.get()
    date=e_date.get()
    event=e_event.get()
    prize=e_prize.get()
    organization=e_organization.get()
    if(admno=="" or name=="" or classec=="" or date=="" or prize=="" or organization==""):
        mb.showerror("Update Status", "All fields are required")
    else:
        try:
            cursor.execute("update record set Name_Of_Student='"+ name +"', Class_and_Section='"+ classec +"', Date_Of_Competition='"+ date +"', Name_Of_Event='"+ event +"', Prize_Won='"+ prize +"', Organization_where_Competition_was_Held='"+ organization +"' where admission_number='"+ admno +" and Name_Of_Event='"+ event +"'")
            cursor.execute("commit")
        
            e_admno.delete(0, 'end')
            e_name.delete(0, 'end')
            e_classec.delete(0, 'end')
            e_date.delete(0, 'end')
            e_event.delete(0, 'end')
            e_prize.delete(0, 'end')
            e_organization.delete(0, 'end')
            show()
            mb.showinfo("Update Status", "Record Updated Successfully")
            con.close()
        except Exception:
            mb.showerror("Update Status","No matching record found as admission number\nand name of event must match a record . In case\na record has been entered with wrong event name\nyou can delete it and insert a new one")
            e_admno.delete(0, 'end')
            e_name.delete(0, 'end')
            e_classec.delete(0, 'end')
            e_date.delete(0, 'end')
            e_event.delete(0, 'end')
            e_prize.delete(0, 'end')
            e_organization.delete(0, 'end')

def get():
    con = mysql.connect(host="localhost", user="root", password='comp', database="project",port=3307)
    cursor = con.cursor()
    cursor.execute("Select admission_number from record")
    admnos=cursor.fetchall()
    if(e_admno.get() == ""):
        mb.showerror("Fetching Status", "Admmission number is compulsory for fetching record")    
    elif tuple([int(e_admno.get()),]) not in admnos:
       mb.showerror("Fetching Status", "No record exists for Admission Number " + e_admno.get())
       e_admno.delete(0, 'end')
    else:
        cursor.execute("Select * from record where admission_number='"+ e_admno.get() +"'")
        rows = cursor.fetchall()
        def get1():
                for row in rows:
                    Student_table.insert('',END,values=row)
                con.commit()
                con.close()
        def all():
            con = mysql.connect(host="localhost", user="root", password='comp', database="project",port=3307)
            cursor = con.cursor()
            cursor.execute("Select * from record order by admission_number")
            dataall=cursor.fetchall()
            for dele in Student_table.get_children():
                    Student_table.delete(dele)
            for row in dataall:
                Student_table.insert('',END,values=row)
            con.commit()
            con.close()
                

        e_admno.delete(0, 'end')
        e_name.delete(0, 'end')
        e_classec.delete(0, 'end')
        e_date.delete(0, 'end')
        e_event.delete(0, 'end')
        e_prize.delete(0, 'end')
        e_organization.delete(0, 'end')

        
        root1=Tk()
        root1.geometry("800x580")
        root1.maxsize(800,580)
        root1.minsize(800,580)
        root1.title("Fetch status")

        Detail_frame=Frame(root1,bg="#272727")
        Detail_frame.pack(fill=BOTH,expand=1)

        showallbtn=Button(Detail_frame,text="Show all Records", font=("times new roman", 10),width=20,pady=5,bg="#FF652F", command=all)
        showallbtn.place(x=30,y=530)
        closebtn=Button(Detail_frame,text="Close", font=("times new roman", 10),width=12,pady=5,bg="#FF652F", command=root1.destroy)
        closebtn.place(x=680,y=530)

        Table_frame=Frame(Detail_frame,bd=4,relief=RIDGE,bg="#272727")
        Table_frame.place(x=10,y=10,width=780,height=500)

        scroll_x=Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_frame,orient=VERTICAL)
        Student_table=ttk.Treeview(Table_frame,columns=("admno","name","class","date","prize","organization","event"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=Student_table.xview)
        scroll_y.config(command=Student_table.yview)
        Student_table.heading('admno',text="Adm. No.")
        Student_table.heading('name',text="Name")
        Student_table.heading('class',text="Class and Section")
        Student_table.heading('date',text="Date of Event")
        Student_table.heading('event',text="Name of Event")
        Student_table.heading('prize',text="Prize Won")
        Student_table.heading('organization',text="Organization where event was held")
        Student_table['show']='headings'
        Student_table.column("admno",width=100)
        Student_table.column("name",width=200)
        Student_table.column("class",width=120)
        Student_table.column("date",width=120)
        Student_table.column("event",width=200)
        Student_table.column("prize",width=100)
        Student_table.column("organization",width=400)
        Student_table.pack(fill=BOTH,expand=1)
        get1()
        root1.mainloop()        

def show():
     con = mysql.connect(host="localhost", user="root", password='comp', database="project",port=3307)
     cursor = con.cursor()
     cursor.execute("Select * from record order by admission_number")
     rows = cursor.fetchall()
     for dele in Student_table.get_children():
                    Student_table.delete(dele)
     for row in rows:
        Student_table.insert('',END,values=row)
     con.commit()
     con.close()

def about():
    root=Tk()
    root.geometry("310x170")
    root.maxsize(310,100)
    root.minsize(310,100)
    root.title("About")
    info=Label(root, text="This is a software to store and manage competition prizes")
    info2=Label(root, text="Created By:Prabhav Chandra", fg="#FF652F")
    info4=Label(root, text="Created as annual project of class 12")
    
    info.place(x=0, y=25)
    info2.place(x=70, y=50)
    info4.place(x=55, y=80)
    closebtn=Button(root,text="Close", font=("times new roman", 10),width=12,pady=1,bg="SystemButtonFace", command=root.destroy)
    closebtn.place(x=95,y=120)
    root.mainloop()

def prihelp():
    root=Tk()
    root.geometry("320x160")
    root.maxsize(320,160)
    root.minsize(320,160)
    root.title("Help")
    info=Label(root, text="This is a software to store and manage competition prizes")
    info1=Label(root, text="The Admission Number field accepts only integer values\nDate Format must be YYYY/MM/DD")
    info.place(x=0, y=40)
    info1.place(x=0, y=60)
    closebtn=Button(root,text="Close", font=("times new roman", 10),width=12,pady=1,bg="#FF652F", command=root.destroy)
    closebtn.place(x=110,y=125)
    root.mainloop()


root=Tk()
root.geometry("1300x800+30+15")
root.minsize(1200,700)
root.maxsize(1300,800)
root.title("Records for Competetion")
root.configure(background="#E0EEEE")


f=Frame(root, bg="#66CCCC" , borderwidth=6 , relief=SUNKEN) 
f.pack(side=TOP, fill=X)
heading=Label(f, text="The Prize Records", font=("bold", 30),bg="#66CCCC", fg="#FFFFFF")
heading.pack()

f1=Frame(root, bg="#D1EEEE" , borderwidth=6 , relief=SUNKEN)
f1.pack(side=LEFT, anchor="nw",padx=10, pady=30)


admno=Label(f1, text="Admission number",bg="#66CCCC", fg="#FFFFFF", pady=5, borderwidth=6 , relief=SUNKEN, font=('bold'))
name=Label(f1, text="Name Of Participant",bg="#66CCCC", fg="#FFFFFF",pady=5,borderwidth=6 , relief=SUNKEN, font=('bold'))
classec=Label(f1, text="Class and Section",bg="#66CCCC", fg="#FFFFFF",pady=5,borderwidth=6 , relief=SUNKEN, font=('bold'))
date=Label(f1, text="Date of event",bg="#66CCCC", fg="#FFFFFF",pady=5,borderwidth=6 , relief=SUNKEN, font=('bold'))
event=Label(f1, text="Name Of event",bg="#66CCCC", fg="#FFFFFF",pady=5,borderwidth=6 , relief=SUNKEN, font=('bold'))
prize=Label(f1, text="Prize Won by student",bg="#66CCCC", fg="#FFFFFF",pady=5,borderwidth=6 , relief=SUNKEN, font=('bold'))
organization=Label(f1, text="Organization where competition was held", bg="#66CCCC", fg="#FFFFFF",pady=5,borderwidth=6 , relief=SUNKEN, font=('bold'))


admno.pack(padx=0, pady=15,)
name.pack(padx=0, pady=15, )
classec.pack(padx=0, pady=15,) 
date.pack(padx=0, pady=15, )
event.pack(padx=0, pady=15, )
prize.pack(padx=0, pady=15,)
organization.pack(padx=2, pady=15,)


f2=Frame(root, bg="#D1EEEE" , borderwidth=6 , relief=SUNKEN)
f2.pack(side=LEFT,anchor="nw", padx=30,pady=30)


e_admno=Entry(f2,font=('bold'))
e_admno.pack(padx=30, pady=25,)
e_name=Entry(f2,font=('bold'))
e_name.pack(padx=30, pady=22,)
e_classec=Entry(f2,font=('bold'))
e_classec.pack(padx=30, pady=24,)
e_date=Entry(f2,font=('bold'))
e_date.pack(padx=30, pady=25,)
e_event=Entry(f2,font=('bold'))
e_event.pack(padx=30, pady=25,)
e_prize=Entry(f2,font=('bold'))
e_prize.pack(padx=30, pady=24,)
e_organization=Entry(f2,font=('bold'))
e_organization.pack(padx=30, pady=25,)



insert = Button(text="INSERT", font=("italic", 10, "bold"), bg="#00CDCD", command=insert,padx=15)
insert.place(x=640, y=150)

delete = Button(text="DELETE", font=("italic", 10, "bold"), bg="#00CDCD", command=delete,padx=15)
delete.place(x=640, y=250)

update = Button(text="UPDATE", font=("italic", 10, "bold"), bg="#00CDCD", command=update,padx=15)
update.place(x=640, y=350)

get = Button(text="SEARCH", font=("italic", 10, "bold"), bg="#00CDCD", command=get,padx=15)
get.place(x=640, y=450)

fr4=Frame(root , bg="#66CCCC", borderwidth="7", relief=SUNKEN)
fr4.place(x=10,y=600,height=180,width=1290,)
scroll_x=Scrollbar(fr4,orient=HORIZONTAL)
scroll_y=Scrollbar(fr4,orient=VERTICAL)
Student_table=ttk.Treeview(fr4,columns=("admno","name","class","date","prize","organization","event"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=Student_table.xview)
scroll_y.config(command=Student_table.yview)
Student_table.heading('admno',text="Adm. No.")
Student_table.heading('name',text="Name")
Student_table.heading('class',text="Class and Section")
Student_table.heading('date',text="Date of Event")
Student_table.heading('event',text="Name of Event")
Student_table.heading('prize',text="Prize Won")
Student_table.heading('organization',text="Organization where event was held")
Student_table['show']='headings'
Student_table.column("admno",width=100)
Student_table.column("name",width=200)
Student_table.column("class",width=120)
Student_table.column("date",width=120)
Student_table.column("event",width=200)
Student_table.column("prize",width=100)
Student_table.column("organization",width=400)
Student_table.pack(fill=BOTH,expand=1)
show()


menubar=Menu(root)
m1 = Menu(menubar, tearoff=0)
m1.add_separator()
m1.add_command(label="Exit", command=root.destroy)
root.config(menu=menubar)
menubar.add_cascade(label="File", menu=m1)

m2 = Menu(menubar, tearoff=0)
m2.add_command(label="About", command=about)
m2.add_separator()
m2.add_command(label="Help", command=prihelp)
root.config(menu=menubar)
menubar.add_cascade(label="Help", menu=m2)

root.mainloop()
