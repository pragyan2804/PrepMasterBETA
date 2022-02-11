from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import tkinter
import importlib
import mysql.connector as mysql



def signupwindowaction():
    signupwindow = Tk()
    signupwindow.title("PrepMasterBETA")
    signupwindow.geometry("1280x720")   
    bg = PhotoImage(file = "signup.png")
    label2 = Label( signupwindow, image = bg)
    label2.place(x = 0, y = 0)
    signupwindow.resizable(False, False)

    def accountdone1():
        mycon = mysql.connect(host='localhost', user='root', passwd='dhruv_789_$1', database='prepmaster')
        mycursor = mycon.cursor()
        try:
            mycursor.execute('insert into sign_in_student values("%s","%s","%s","%s","%s","%s");'%(f_name.get(),user_name.get(),passwd_key.get(),"VIII",school_db.get(),email_db.get(),))
            mycon.commit()
            mycursor.execute('insert into account_student values("%s","%s");'%(user_name.get(),passwd_key.get()))
            mycon.commit()
            messagebox.showinfo("SHOWINFO", "ACCOUNT CREATED!")
            signupwindow.destroy()
            from MasterPrepBETA import loginaction
            loginaction()        
        except:
            messagebox.showerror('SHOWERROR','RECORD INSERTION UNSUCCESSFUL!')

    def accountdone2(e):
        mycon = mysql.connect(host='localhost', user='root', passwd='dhruv_789_$1', database='prepmaster')
        mycursor = mycon.cursor()
        try:
            mycursor.execute('insert into sign_in_student values("%s","%s","%s","%s","%s","%s");'%(f_name.get(),user_name.get(),passwd_key.get(),"VIII",school_db.get(),email_db.get(),))
            mycon.commit()
            mycursor.execute('insert into account_student values("%s","%s");'%(user_name.get(),passwd_key.get()))
            mycon.commit()
            messagebox.showinfo("SHOWINFO", "ACCOUNT CREATED!")
            signupwindow.destroy()
            from MasterPrepBETA import loginaction
            loginaction()        
        except:
            messagebox.showerror('SHOWERROR','RECORD INSERTION UNSUCCESSFUL!')

    f_name = StringVar()
    fullname = Entry(signupwindow,
                textvariable=f_name,
                justify="center",
                bg="#0c5dc0",
                borderwidth=0,
                font="calibri 20",).place(x=799, y=50, width=435, height=55)

    user_name = StringVar()
    username = Entry(signupwindow,
                textvariable=user_name,
                justify="center",
                bg="#0c5dc0",
                borderwidth=0,
                font="calibri 20",).place(x=799, y=153, width=435, height=55)

    passwd_key = StringVar()
    passkey   = Entry(signupwindow,
                textvariable=passwd_key,
                justify="center",
                bg="#0c5dc0",
                borderwidth=0,
                show="*",
                font="calibri 20",).place(x=799, y=254, width=435, height=55)

    classdisplay = Entry(signupwindow, 
                        font="BurbankBigCondensed-Bold 17", 
                        width=13, 
                        bg="#0c5dc0", 
                        disabledbackground="#0c5dc0",
                        state="disabled",
                        fg="white")
    classdisplay.place(x=799, y=353, width=435, height=55)



    def setclass8():
        classdisplay.configure(disabledbackground="#0c5dc0",
                     state="normal",)
        classdisplay.delete(0,"end")
        classdisplay.insert(0, "Class 8th")
        classdisplay.configure(disabledbackground="#0c5dc0",
                               disabledforeground="white",
                               state="disabled",)

    class8button = tkinter.Button(signupwindow, 
                                  text="8th", 
                                  font="BurbankBigCondensed-Bold 17",
			    	              fg="white",
				                  bg="#0072ff",
				                  borderwidth=1,
				                  command=setclass8).place(x=1100, y=353, width=130, height=55)

    def setclass9():
        messagebox.showerror("ERROR", "This BETA version is currently only available for class 8th only")
        classdisplay.configure(disabledbackground="#0c5dc0",
                     state="normal",)
        classdisplay.delete(0,"end")
        classdisplay.insert(0, "Class 8th")
        classdisplay.configure(disabledbackground="#0c5dc0",
                     state="disabled", 
                     disabledforeground="white")


    class9button = tkinter.Button(signupwindow, text="9th",
	    			font="BurbankBigCondensed-Bold 17",
		    		fg="white",
			    	bg="#0072ff",
				    borderwidth=1,
				    command=setclass9).place(x=970, y=353, width=130, height=55)

    school_db = StringVar()
    school    = Entry(signupwindow,
                textvariable=school_db,
                justify="center",
                borderwidth=0,
                bg="#0c5dc0",
                font="calibri 20",).place(x=799, y=455, width=435, height=55)

    email_db = StringVar()
    emailad   = Entry(signupwindow,
                textvariable=email_db,
                justify="center",
                borderwidth=0,
                bg="#0c5dc0",
                font="calibri 20",).place(x=799, y=551, width=435, height=55)

    Display = Button(signupwindow, 
	    			text ="SIGN UP",
		    		font ="BurbankBigCondensed-Bold 25",
			    	bg="#57595c",
                    borderwidth=0,
                    fg='white',
				    command = lambda:accountdone1()).place(x=920, y=631, width=200, height=53)
    signupwindow.bind('<Return>',accountdone2)



    mainloop()