from sqlite3 import Cursor
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import tkinter
import importlib
from tkinter import font
import mysql.connector as mysql   
    
    

def doubtstudent():
    root = Tk()
    root.title("PrepMasterBETA")
    root.geometry("1280x720")   
    bg = PhotoImage(file = "chapbg.png")
    label2 = Label( root, image = bg)
    label2.place(x = 0, y = 0)
    root.resizable(False, False)   

    global counter
    counter = 0


    mycon = mysql.connect(host='localhost', user='root', passwd='pragyan123', database='prepmaster')

    mycursor = mycon.cursor()
    mycursor.execute('select username from account_student where status = 1;')
    records = mycursor.fetchall()
    mycon.commit()
    leaderuser = (records)
    leaderuserin = (str(leaderuser)[3:-4])
    #######################################

    global entrycount

    mycursor = mycon.cursor()
    sql = 'select * from doubt_record where username = %s;'
    val = (leaderuserin,)
    mycursor.execute(sql,val)
    records = mycursor.fetchall()
    mycon.commit()
    entrycount = len(records)
    print(entrycount)


    def submitdoubt():
        mycon = mysql.connect(host='localhost', user='root', passwd='pragyan123', database='prepmaster')
        mycursor = mycon.cursor()
        mycursor.execute('insert into doubt_record values("%s","%s","%s","%s");'%(leaderuserin,doubtgiven.get(),"(NO ANSWER AVAILABLE)",1))
        mycon.commit()
        messagebox.showinfo("SUBMITTED", "DOUBT SUBMITTED")
        root.destroy()

    def submitdoubt1(e):
        submitdoubt()




    doubtgiven = StringVar()
    doubtenter = Entry(root,
                textvariable=doubtgiven,
                justify="center",
                bg="#0c5dc0",
                font="BurbankBigCondensed-Bold 25",).place(x=250, y=200, width=790, height=90)




    def doubtnext():
        global counter    
        counter += 1
        global checker
        checker = counter+1
        if (checker>entrycount):
            counter=0
        prevqtext.set(records[counter][1])
        answergiven.set(records[counter][2])


    def doubtback():
        global counter    
        counter -= 1
        global checker
        checker = counter+1
        if (checker==0):
            counter=entrycount-1
        prevqtext.set(records[counter][1])
        answergiven.set(records[counter][2])

    def doubtnext1(e):
        doubtnext()
    def doubtback1(e):
        doubtback()

    root.bind('<Left>',doubtback1)
    root.bind('<Right>',doubtnext1)


    global prevqtext 
    prevqtext= StringVar()
    if entrycount == 0:
        prevqtext.set("(NO PREVIOUSLY ASKED DOUBTS)")
    else:
        mycursor = mycon.cursor()
        sql = 'select * from doubt_record where username = %s;'
        val = (leaderuserin,)
        mycursor.execute(sql,val)
        records = mycursor.fetchall()
        mycon.commit()
        prevqtext= StringVar()
        prevqtext.set(records[counter][1])




    prevqdisplay = Label(root, 
                    font="BurbankBigCondensed-Bold 17", 
                    width=13,
                    textvariable=prevqtext,
                    bg="#0c5dc0",
                    justify="center",
                    borderwidth="1",
                    relief="solid",
                    fg="white")
    prevqdisplay.place(x=250, y=370, width=790, height=90)




    global answergiven
    answergiven= StringVar()
    if entrycount == 0:
        answergiven.set("(NO ANSWER AVAILABLE)")
    else:
        mycursor = mycon.cursor()
        sql = 'select * from doubt_record where username = %s;'
        val = (leaderuserin,)
        mycursor.execute(sql,val)
        records = mycursor.fetchall()
        mycon.commit()
        answergiven= StringVar()
        answergiven.set(records[counter][2])


    answerdisplay = Label(root, 
                    font="BurbankBigCondensed-Bold 17", 
                    width=13,
                    textvariable=answergiven,
                    bg="#0c5dc0",
                    justify="center",
                    borderwidth="1",
                    relief="solid",
                    fg="white")
    answerdisplay.place(x=250, y=450, width=790, height=90)





    button_back = tk.Button(root,
        text='<BACK>',
        font='BurbankBigCondensed-Bold 35',
        bg='#0072ff',
        fg='white',
        borderwidth=0,).place(x=5,y=15, width=150, height=70)

    Display = Button(root, 
                text ="SUBMIT",
                font ="BurbankBigCondensed-Bold 25",
                bg="#57595c",
                command=lambda:submitdoubt()).place(x=535, y=600, width=250, height=50)
    root.bind('<Return>',submitdoubt1)

    great_font = font.Font(size = 100)
    great_display = tk.Button(root,
                    text='>',
                    font="BurbankBigCondensed-Bold 17",
                    fg="white",
                    bg="#0072ff",
                    width=80,
                    height=89,
                    borderwidth=0,
                    command=lambda:doubtnext())
    great_display['font'] = great_font
    great_display.place(x=1190, y=300, width=80, height=100)

    less_font = font.Font(size = 100)
    less_display = tk.Button(root,
                        text='<',
                        font="BurbankBigCondensed-Bold 17",
                        fg="white",
                        bg="#0072ff",
                        width=80,
                        height=89,
                        borderwidth=0,
                        command=lambda:doubtback())
    less_display['font'] = less_font
    less_display.place(x=5, y=300, width=80, height=100)

    root.mainloop()