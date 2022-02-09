from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import tkinter
import importlib



def signupwindowaction():
    signupwindow = Tk()
    signupwindow.title("PrepMasterBETA")
    signupwindow.geometry("1280x720")   
    bg = PhotoImage(file = "signup.png")
    label2 = Label( signupwindow, image = bg)
    signupwindow.eval('tk::PlaceWindow . center')
    label2.place(x = 0, y = 0)
    signupwindow.resizable(False, False)

    def accountdone1():
        messagebox.showinfo("showinfo", "[ACCOUNT CREATED] button")
        signupwindow.destroy()
        from MasterPrepBETA import loginaction
        loginaction()
	

    def accountdone2(e):
        messagebox.showinfo("showinfo", "[ACCOUNT CREATED] enter")
        signupwindow.destroy()
        import MasterPrepBETA
        from MasterPrepBETA import loginaction
        loginaction()
	


    fullname = Entry(signupwindow,
                justify="center",
                bg="#0c5dc0",
                borderwidth=0,
                font="calibri 20",).place(x=799, y=50, width=435, height=55)

    username = Entry(signupwindow,
                justify="center",
                bg="#0c5dc0",
                borderwidth=0,
                font="calibri 20",).place(x=799, y=153, width=435, height=55)

    passkey   = Entry(signupwindow,
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



    def setclass11():
        classdisplay.configure(disabledbackground="#0c5dc0",
                     state="normal",)
        classdisplay.delete(0,"end")
        classdisplay.insert(0, "Class 11th")
        classdisplay.configure(disabledbackground="#0c5dc0",
                               disabledforeground="white",
                               state="disabled",)

    class11button = tkinter.Button(signupwindow, 
                                  text="11th", 
                                  font="BurbankBigCondensed-Bold 17",
			    	              fg="white",
				                  bg="#0072ff",
				                  borderwidth=1,
				                  command=setclass11).place(x=1100, y=353, width=130, height=55)

    def setclass12():
        classdisplay.configure(disabledbackground="#0c5dc0",
                     state="normal",)
        classdisplay.delete(0,"end")
        classdisplay.insert(0, "Class 12th")
        classdisplay.configure(disabledbackground="#0c5dc0",
                     state="disabled", 
                     disabledforeground="white")


    class12button = tkinter.Button(signupwindow, text="12th",
	    			font="BurbankBigCondensed-Bold 17",
		    		fg="white",
			    	bg="#0072ff",
				    borderwidth=1,
				    command=setclass12).place(x=970, y=353, width=130, height=55)


    school    = Entry(signupwindow,
                justify="center",
                borderwidth=0,
                bg="#0c5dc0",
                font="calibri 20",).place(x=799, y=455, width=435, height=55)

    emailad   = Entry(signupwindow,
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