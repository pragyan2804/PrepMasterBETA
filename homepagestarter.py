import datetime
from re import A
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import importlib
import tkinter
from tkinter import font
from tkinter.tix import IMAGETEXT
import PIL
from PIL import Image
import tkinter as tk
import tkinter.font as font
import mysql.connector as mysql
import random



def homepageaction():
    root = Tk()
    root.geometry("1280x720")
    root.title("PrepMasterBETA")
    root.resizable(False, False)
    usernametoshow = ""

    mycon = mysql.connect(host='localhost', user='root', passwd='pragyan123', database='prepmaster')
    mycursor = mycon.cursor()
    mycursor.execute('select username from account_student where status = 1;')
    records = mycursor.fetchall()
    mycon.commit()
    usernametoshow = (records)
    

    def signout():
        root.destroy()
        from MasterPrepBETA import studentlogin
        studentlogin()

    def homeflash1(e):
        homeflash()
    def homemcq1(e):
        homemcq()
    def homedoubt1(e):
        homedoubt()
    def homeleader1(e):
        homeleader()
    def selectsubject1(e):
        selectsubject()
    def selecttest1(e):
        selecttest()
    global leaderselect
    leaderselect = int
    global mcqsesh
    mcqsesh = int
    global count_button
    count_button = 0



    def leadssc():
        global leaderselect
        leaderselect==1
        mycursor = mycon.cursor()
        mycursor.execute('select fullname,school,sst_score from account_student order by sst_score desc;')
        global table_data
        table_data = mycursor.fetchall()
        leaderstart()

    def leadmath():
        global leaderselect
        leaderselect==2
        mycursor = mycon.cursor()
        mycursor.execute('select fullname,school,math_score from account_student order by math_score desc;')
        global table_data
        table_data = mycursor.fetchall() 
        leaderstart()
    def leadsci():
        global leaderselect
        leaderselect==3
        mycursor = mycon.cursor()
        mycursor.execute('select fullname,school,sci_score from account_student order by sci_score desc;')
        global table_data
        table_data = mycursor.fetchall()  
        leaderstart()
        
    def mathmensmcq():
        global mcqsesh
        global data
        mcqsesh==1
        mycursor.execute('select * from math_mens_mcq;')
        data = mycursor.fetchall()
        mcqstart()

    def scicellmcq():
        global mcqsesh
        global data
        mcqsesh==2   
        mycursor.execute('select * from sci_cell_mcq;')
        data = mycursor.fetchall()
        mcqstart()

    def stopwatch(): 
        frame= tk.Frame(root,
                    width= 210, height=150)
        frame.place(x=609, y=267)
        global label1
        label1 = tk.Label(frame, text="Let's Begin!", fg="white", bg="#3C4142", font="BurbankBigCondensed-Bold 40")
        label1.pack()
        global f
        f = tk.Frame(root)

        def counter_label(label1):
                def count():
                    if running:
                        global counter
                        if counter==66600:            
                            display="Starting..."
                        else:
                            tt = datetime.datetime.fromtimestamp(counter)
                            global timeval
                            timeval = tt.strftime("%M:%S")
                            display=timeval
                            label1.pack()
            
                        label1['text']=display   
                        label1.after(1000, count) 
                        counter += 1
                        global timerq
                        timerq=counter-66600
                count()     
        def Start(label1):
                global running
                running=True
                counter_label(label1)

        def Stop():
                global running
                running = False
        
        frame.after(0)
        Start(label1)

    global iscomp
    iscomp=0





    

#######################################################################################################
    def homeflash():
        frame = Frame(root, width=1280, height=720)
        frame.pack()
        frame.place(anchor='center', relx=0.5, rely=0.5)
        global img
        img = PhotoImage(file="homeflash.png")
        label = Label(frame, image = img)
        label.pack()
        global x
        x = 1

        root.bind('<Left>',homeleader1)
        root.bind('<Right>',homemcq1)
        root.bind('<Return>',selectsubject1)

        great_font = font.Font(size = 100)
        great_display = tk.Button(root,
                            text='>',
                            font="BurbankBigCondensed-Bold 17",
                            fg="white",
                            bg="#22C53A",
                            width=80,
                            height=89,
                            borderwidth=0,
                            command = lambda:homemcq())
        great_display['font'] = great_font
        great_display.place(x=1190, y=332, width=80, height=100)

        less_font = font.Font(size = 100)
        less_display = tk.Button(root,
                            text='<',
                            font="BurbankBigCondensed-Bold 17",
                            fg="white",
                            bg="#22C53A",
                            width=80,
                            height=89,
                            borderwidth=0,
                            command = lambda:homeleader())
        less_display['font'] = less_font
        less_display.place(x=5, y=332, width=80, height=100)
        display = tkinter.Button(root, 
                            text = 'GO!',
                            font='BurbankBigCondensed-Bold 25',
                            bg='#57595c',
                            fg='white',
                            command = lambda:selectsubject()).place(x=480, y=486, width=320, height=75)


        display = tk.Button(root,
                            text="signed in as "+str(usernametoshow)[3:-4],
                            font="BurbankBigCondensed-Bold 17",
                            fg="black",
                            bg="#22C53A",
                            borderwidth=0).place(x=0, y=1.15, width=300, height=50)

        display = tk.Button(root,
                            text="<SIGN OUT>",
                            font="BurbankBigCondensed-Bold 17",
                            fg="black",
                            bg="#22C53A",
                            borderwidth=0,
                            command = lambda:signout()).place(x=970, y=1.15, width=300, height=50)


    def homemcq():
        frame = Frame(root, width=1280, height=720)
        frame.pack()
        frame.place(anchor='center', relx=0.5, rely=0.5)
        global img
        img = PhotoImage(file="homemcq.png")
        label = Label(frame, image = img)
        label.pack()
        global x
        x = 2

        root.bind('<Left>',homeflash1)
        root.bind('<Right>',homedoubt1)
        root.bind('<Return>',selecttest1)

        great_font = font.Font(size = 100)
        great_display = tk.Button(root,
                            text='>',
                            font="BurbankBigCondensed-Bold 17",
                            fg="white",
                            bg="#D92B2B",
                            width=80,
                            height=89,
                            borderwidth=0,
                            command = lambda:homedoubt())
        great_display['font'] = great_font
        great_display.place(x=1190, y=332, width=80, height=100)

        less_font = font.Font(size = 100)
        less_display = tk.Button(root,
                            text='<',
                            font="BurbankBigCondensed-Bold 17",
                            fg="white",
                            bg="#D92B2B",
                            width=80,
                            height=89,
                            borderwidth=0,
                            command = lambda:homeflash())
        less_display['font'] = less_font
        less_display.place(x=5, y=333, width=80, height=100)

        display = tk.Button(root, 
                            text = 'GO!',
                            font='BurbankBigCondensed-Bold 25',
                            bg='#57595c',
                            fg='white',
                            command = lambda:selecttest()).place(x=480, y=486, width=320, height=75)

        display = tk.Button(root,
                            text="signed in as "+str(usernametoshow)[3:-4],
                            font="BurbankBigCondensed-Bold 17",
                            fg="black",
                            bg="#D92B2B",
                            borderwidth=0).place(x=0, y=1.15, width=300, height=50)

        display = tk.Button(root,
                            text="<SIGN OUT>",
                            font="BurbankBigCondensed-Bold 17",
                            fg="black",
                            bg="#D92B2B",
                            borderwidth=0,
                            command = lambda:signout()).place(x=970, y=1.15, width=300, height=50)



    def homeleader():
        frame = Frame(root, width=1280, height=720)
        frame.pack()
        frame.place(anchor='center', relx=0.5, rely=0.5)
        global img
        img = PhotoImage(file="homeleader.png")
        label = Label(frame, image = img)
        label.pack()
        global x
        x = 3
        root.bind('<Left>',homedoubt1)
        root.bind('<Right>',homeflash1)
        root.bind('<Return>',selectsubject1)

        great_font = font.Font(size = 100)
        great_display = tk.Button(root,
                            text='>',
                            font="BurbankBigCondensed-Bold 17",
                            fg="white",
                            bg="#C5AE22",
                            width=80,
                            height=89,
                            borderwidth=0,
                            command = lambda:homeflash())
        great_display['font'] = great_font
        great_display.place(x=1190, y=332, width=80, height=100)

        less_font = font.Font(size = 100)
        less_display = tk.Button(root,
                            text='<',
                            font="BurbankBigCondensed-Bold 17",
                            fg="white",
                            bg="#C5AE22",
                            width=80,
                            height=89,
                            borderwidth=0,
                            command = lambda:homedoubt())
        less_display['font'] = less_font
        less_display.place(x=5, y=332, width=80, height=100)

        display = tk.Button(root, 
                            text = 'GO!',
                            font='BurbankBigCondensed-Bold 25',
                            bg='#57595c',
                            fg='white',
                            command = lambda:selectsubject()).place(x=480, y=486, width=320, height=75)

        display = tk.Button(root,
                            text="signed in as "+str(usernametoshow)[3:-4],
                            font="BurbankBigCondensed-Bold 17",
                            fg="black",
                            bg="#C5AE22",
                            borderwidth=0).place(x=0, y=1.15, width=300, height=50)

        display = tk.Button(root,
                            text="<SIGN OUT>",
                            font="BurbankBigCondensed-Bold 17",
                            fg="black",
                            bg="#C5AE22",
                            borderwidth=0,
                            command = lambda:signout()).place(x=970, y=1.15, width=300, height=50)

                        
    def homedoubt():
        frame = Frame(root, width=1280, height=720)
        frame.pack()
        frame.place(anchor='center', relx=0.5, rely=0.5)
        global img
        img = PhotoImage(file="homedoubt.png")
        label = Label(frame, image = img)
        label.pack()
        root.bind('<Left>',homemcq1)
        root.bind('<Right>',homeleader1)

        great_font = font.Font(size = 100)
        great_display = tk.Button(root,
                            text='>',
                            font="BurbankBigCondensed-Bold 17",
                            fg="white",
                            bg="#B327C4",
                            width=80,
                            height=89,
                            borderwidth=0,
                            command = lambda:homeleader())
        great_display['font'] = great_font
        great_display.place(x=1190, y=332, width=80, height=100)

        less_font = font.Font(size = 100)
        less_display = tk.Button(root,
                            text='<',
                            font="BurbankBigCondensed-Bold 17",
                            fg="white",
                            bg="#B327C4",
                            width=80,
                            height=89,
                            borderwidth=0,
                            command = lambda:homemcq())
        less_display['font'] = less_font
        less_display.place(x=5, y=332, width=80, height=100)

        display = tk.Button(root, 
                            text = 'GO!',
                            font='BurbankBigCondensed-Bold 25',
                            bg='#57595c',
                            fg='white').place(x=480, y=486, width=320, height=75)

        display = tk.Button(root,
                            text="signed in as "+str(usernametoshow)[3:-4],
                            font="BurbankBigCondensed-Bold 17",
                            fg="black",
                            bg="#B327C4",
                            borderwidth=0).place(x=0, y=1.15, width=300, height=50)

        display = tk.Button(root,
                            text="<SIGN OUT>",
                            font="BurbankBigCondensed-Bold 17",
                            fg="black",
                            bg="#B327C4",
                            borderwidth=0,
                            command = lambda:signout()).place(x=970, y=1.15, width=300, height=50)





    def selecttest():
        frame = Frame(root, width=1280, height=720)
        frame.pack()
        frame.place(anchor='center', relx=0.5, rely=0.5)
        global img
        img = PhotoImage(file="selecttest.png")
        label = Label(frame, image = img)
        label.pack()

        root.bind('<Escape>',homemcq1)

        def selectedstandard():
            global iscomp
            iscomp=0
            selectsubject()

        button_mcq = tk.Button(root,
                text='STANDARD MCQ TEST',
                font='BurbankBigCondensed-Bold 40',
                bg='#c32b2b',
                fg='white',
                command = lambda:selectedstandard()).place(x=63, y=240, width=500, height=300)

        def selectedcomp():
            global iscomp
            iscomp=1
            selectsubject()

        button_mcq_comp = tk.Button(root,
                text='COMPETITIVE MASTERTEST',
                font='BurbankBigCondensed-Bold 35',
                bg='#c32b2b',
                fg='white',
                command = lambda:selectedcomp()).place(x=723, y=240, width=500, height=300)

        button_back = tk.Button(root,
                text='<BACK>',
                font='BurbankBigCondensed-Bold 35',
                bg='#0072ff',
                fg='white',
                borderwidth=0,
                command = lambda:homemcq()).place(x=5,y=15, width=150, height=70)

    def selectsubject():
        frame = Frame(root, width=1280, height=720)
        frame.pack()
        frame.place(anchor='center', relx=0.5, rely=0.5)
        global img
        img = PhotoImage(file="selectsubject.png")
        label = Label(frame, image = img)
        label.pack()
        global flashsesh
        
        if x==1:
            button_back = tk.Button(root,
                text='<BACK>',
                font='BurbankBigCondensed-Bold 35',
                bg='#0072ff',
                fg='white',
                borderwidth=0,
                command = lambda:homeflash()).place(x=5,y=15, width=150, height=70)
        elif x==2:
            button_back = tk.Button(root,
                text='<BACK>',
                font='BurbankBigCondensed-Bold 35',
                bg='#0072ff',
                fg='white',
                borderwidth=0,
                command = lambda:selecttest()).place(x=5,y=15, width=150, height=70)
        elif x==3:
            button_back = tk.Button(root,
                text='<BACK>',
                font='BurbankBigCondensed-Bold 35',
                bg='#0072ff',
                fg='white',
                borderwidth=0,
                command = lambda:homeleader()).place(x=5,y=15, width=150, height=70)

        if x==1:
            root.bind('<Escape>',homeflash1)
        elif x==2:
            root.bind('<Escape>',selecttest1)
        elif x==3:
            root.bind('<Escape>',homeleader1)


        if x == 3:
            button_sst = tk.Button(root,
                        text='SST',
                        font='BurbankBigCondensed-Bold 40',
                        bg='#9518a4',
                        fg='white',
                        command=leadssc).place(x=86, y=350, width=325, height=195)
            button_maths = tk.Button(root,
                        text='MATHS',
                        font='BurbankBigCondensed-Bold 40',
                        bg='#ab9623',
                        fg='white',
                        command=leadmath).place(x=496, y=350, width=325, height=195)
            button_science = tk.Button(root,
                        text='SCIENCE',
                        font='BurbankBigCondensed-Bold 40',
                        bg='#1eaf32',
                        fg='white',
                        command=leadsci).place(x=894, y=350, width=325, height=195)
            
        else:
            button_sst = tk.Button(root,
                            text='SST',
                            font='BurbankBigCondensed-Bold 40',
                            bg='#9518a4',
                            fg='white',
                            command=chapssc).place(x=86, y=350, width=325, height=195)

            button_maths = tk.Button(root,
                            text='MATHS',
                            font='BurbankBigCondensed-Bold 40',
                            bg='#ab9623',
                            fg='white',
                            command=chapmath).place(x=496, y=350, width=325, height=195)

            button_science = tk.Button(root,
                            text='SCIENCE',
                            font='BurbankBigCondensed-Bold 40',
                            bg='#1eaf32',
                            fg='white',
                            command=chapcsi).place(x=894, y=350, width=325, height=195)

    def leadershow():
        frame = Frame(root, width=1280, height=720)
        frame.pack()
        frame.place(anchor='center', relx=0.5, rely=0.5)
        global img
        img = PhotoImage(file="leaderboard.png")
        label = Label(frame, image = img)
        label.pack()
        button_back = tk.Button(root,
                        text='<BACK>',
                        font='BurbankBigCondensed-Bold 35',
                        bg='#0072ff',
                        fg='white',
                        borderwidth=0,
                        command=selectsubject).place(x=5,y=15, width=150, height=70)



    def chapssc():
        frame = Frame(root, width=1280, height=720)
        frame.pack()
        frame.place(anchor='center', relx=0.5, rely=0.5)
        global img
        img = PhotoImage(file="chapbg.png")
        label = Label(frame, image = img)
        label.pack()
        label_heading = tk.Label(root,
                            text='SELECT CHAPTER',
                            justify='center',
                            font='BurbankBigCondensed-Bold 70',
                            bg='#0073FF',
                            fg='white',
                            borderwidth=0).place(x=350, y=70, width=500, height=100)

        button_1 = tk.Button(root,
                        text='The Making Of National Movement',
                        font='BurbankBigCondensed-Bold 30',
                        wraplength=200,
                        bg='#FE7D05',
                        fg='white').place(x=100, y=220, width=263, height=200)

        button_2 = tk.Button(root,
                        text='Resources',
                        font='BurbankBigCondensed-Bold 30',
                        wraplength=200,
                        bg='#7FD10B',
                        fg='white').place(x=470, y=220, width=263, height=200)

        button_3 = tk.Button(root,
                        text='Industries!',
                        font='BurbankBigCondensed-Bold 30',
                        wraplength=200,
                        bg='#FFCA34',
                        fg='white',
                        command=lambda:industries()).place(x=850, y=220, width=263, height=200)
        def industries():
            if x==1:
                global flashsesh
                flashsesh=6
                flashcardstart()


        button_4 = tk.Button(root,
                        text='The Indian Constituion',
                        font='BurbankBigCondensed-Bold 30',
                        wraplength=200,
                        bg='#F00272',
                        fg='white').place(x=250, y=500, width=263, height=200)

        button_5 = tk.Button(root,
                        text='Women, Caste And Reform',
                        font='BurbankBigCondensed-Bold 30',
                        wraplength=200,
                        bg='#CD043F',
                        fg='white').place(x=650, y=500, width=263, height=200)

        button_back = tk.Button(root,
                        text='<BACK>',
                        font='BurbankBigCondensed-Bold 35',
                        bg='#0072ff',
                        fg='white',
                        borderwidth=0,
                        command=selectsubject).place(x=5,y=15, width=150, height=70)
        root.bind('<Escape>',selectsubject1)



    def chapmath():
        frame = Frame(root, width=1280, height=720)
        frame.pack()
        frame.place(anchor='center', relx=0.5, rely=0.5)
        global img
        img = PhotoImage(file="chapbg.png")
        label = Label(frame, image = img)
        label.pack()
        label_heading = tk.Label(root,
                    text='SELECT CHAPTER',
                    justify='center',
                    font='BurbankBigCondensed-Bold 70',
                    bg='#0073FF',
                    fg='white',
                    borderwidth=0).place(x=350, y=70, width=500, height=100)

        button_1 = tk.Button(root,
                        text='Linear Equations!',
                        font='BurbankBigCondensed-Bold 30',
                        wraplength=150,
                        bg='#FE7D05',
                        fg='white',
                        command=lambda:linear()).place(x=100, y=220, width=263, height=200)
        def linear():
            if x==1:
                global flashsesh
                flashsesh=5
                flashcardstart()

        button_2 = tk.Button(root,
                        text='Mensuration!',
                        font='BurbankBigCondensed-Bold 30',
                        bg='#7FD10B',
                        fg='white',
                        command=lambda:mensuration()).place(x=470, y=220, width=263, height=200)
        def mensuration():
            if x==1:
                global flashsesh
                flashsesh=4
                flashcardstart()
            elif x==2:
                global mcqsesh
                mcqsesh=1
                mathmensmcq()


        button_3 = tk.Button(root,
                        text='Exponents And Powers',
                        font='BurbankBigCondensed-Bold 30',
                        wraplength=150,
                        bg='#CD043F',
                        fg='white').place(x=830, y=220, width=263, height=200)

        button_4 = tk.Button(root,
                        text='Sqaure And Square Roots',
                        font='BurbankBigCondensed-Bold 30',
                        wraplength=150,
                        bg='#F30C0D',
                        fg='white').place(x=300, y=500, width=263, height=200)

        button_5 = tk.Button(root,
                        text='Cube And Cube Roots',
                        font='BurbankBigCondensed-Bold 30',
                        wraplength=150,
                        bg='#FFCA34',
                        fg='white').place(x=700, y=500, width=263, height=200)

        button_back = tk.Button(root,
                        text='<BACK>',
                        font='BurbankBigCondensed-Bold 35',
                        bg='#0072ff',
                        fg='white',
                        borderwidth=0,
                        command=selectsubject).place(x=5,y=15, width=150, height=70)
        root.bind('<Escape>',selectsubject1)

    def chapcsi():
        frame = Frame(root, width=1280, height=720)
        frame.pack()
        frame.place(anchor='center', relx=0.5, rely=0.5)
        global img
        img = PhotoImage(file="chapbg.png")
        label = Label(frame, image = img)
        label.pack()        
        label_heading = tk.Label(root,
                    text='SELECT CHAPTER',
                    justify='center',
                    font='BurbankBigCondensed-Bold 70',
                    bg='#0073FF',
                    fg='white',
                    borderwidth=0).place(x=350, y=70, width=500, height=100)

        button_1 = tk.Button(root,
                        text='Crop Production And Management!',
                        font='BurbankBigCondensed-Bold 30',
                        wraplength=200,
                        bg='#FE7D05',
                        fg='white',
                        command=lambda:crop()).place(x=100, y=220, width=263, height=200)
        def crop():
            if x==1:
                global flashsesh
                flashsesh=2
                flashcardstart()

        button_2 = tk.Button(root,
                        text='Coal And Petroleum',
                        font='BurbankBigCondensed-Bold 30',
                        wraplength=150,
                        bg='#F30C0D',
                        fg='white').place(x=470, y=220, width=263, height=200)


        button_3 = tk.Button(root,
                            text='Cell - Structure And Functions!',
                            font='BurbankBigCondensed-Bold 30',
                            wraplength=150,
                            bg='#7FD10B',
                            fg='white',
                            command=lambda:cell()).place(x=850, y=220, width=263, height=200)
        def cell():
            if x==1:
                global flashsesh
                flashsesh=1
                flashcardstart()
            elif x==2:
                global mcqsesh
                mcqsesh=2
                scicellmcq()
        
        

        button_4 = tk.Button(root,
                        text='Force And Pressure!',
                        font='BurbankBigCondensed-Bold 30',
                        bg='#FFCA34',
                        fg='white',
                        command=lambda:force()).place(x=250, y=500, width=263, height=200)
        def force():
            if x==1:
                global flashsesh
                flashsesh=3
                flashcardstart()

        button_5 = tk.Button(root,
                        text='Light',
                        font='BurbankBigCondensed-Bold 30',
                        wraplength=150,
                        bg='#F00272',
                        fg='white').place(x=650, y=500, width=263, height=200)

        button_back = tk.Button(root,
                        text='<BACK>',
                        font='BurbankBigCondensed-Bold 35',
                        bg='#0072ff',
                        fg='white',
                        borderwidth=0,
                        command = selectsubject).place(x=5,y=15, width=150, height=70)
        root.bind('<Escape>',selectsubject1)


    


    ################------BIGGER FUNCTIONS-------##########################


#############################################LEADERBOARDSTART
    def leaderstart():
        frame = Frame(root, width=1280, height=720)
        frame.pack()
        frame.place(anchor='center', relx=0.5, rely=0.5)
        global img
        img = PhotoImage(file="chapbg.png")
        label = Label(frame, image = img)
        label.pack()  

        leaderhead = Entry(root,
                        font="BurbankBigCondensed-Bold 70", 
                            width=13, 
                            borderwidth=0,
                            justify="center",)
        leaderhead.insert(0, "LEADERBOARDS")
        leaderhead.place(x=410, y=10, width=450, height=100)
        leaderhead.configure(disabledbackground="#0072ff", disabledforeground="white",
                            state="disabled",)

        button_back = tk.Button(root,
                        text='<BACK>',
                        font='BurbankBigCondensed-Bold 35',
                        bg='#0072ff',
                        fg='white',
                        borderwidth=0,
                        command=lambda:homeleader()).place(x=5,y=15, width=150, height=70)

        rankhead = Entry(root,
                        font="BurbankBigCondensed-Bold 45", 
                            width=13, 
                            borderwidth=0,
                            justify="center",)
        rankhead.insert(0, "RANK")
        rankhead.place(x=30, y=135, width=150, height=80)
        rankhead.configure(disabledbackground="#0072ff", disabledforeground="black",
                            state="disabled",)

        namehead = Entry(root,
                        font="BurbankBigCondensed-Bold 45", 
                            width=13, 
                            borderwidth=0,
                            justify="center",)
        namehead.insert(0, "NAME")
        namehead.place(x=280, y=135, width=150, height=80)
        namehead.configure(disabledbackground="#0072ff", disabledforeground="black",
                            state="disabled",)


        schoolhead = Entry(root,
                        font="BurbankBigCondensed-Bold 45", 
                            width=13, 
                            borderwidth=0,
                            justify="center",)
        schoolhead.insert(0, "SCHOOL")
        schoolhead.place(x=580, y=135, width=370, height=80)
        schoolhead.configure(disabledbackground="#0072ff", disabledforeground="black",
                            state="disabled",)

        scorehead = Entry(root,
                        font="BurbankBigCondensed-Bold 45", 
                            width=13, 
                            borderwidth=0,
                            justify="center",)
        scorehead.insert(0, "MASTERSCORE")
        scorehead.place(x=925, y=135, width=315, height=80)
        scorehead.configure(disabledbackground="#0072ff", disabledforeground="black",
                            state="disabled",)
        ###############################################################################################################################
        rank1head = Entry(root,
                        font="BurbankBigCondensed-Bold 40", 
                            width=13, 
                            borderwidth=0,
                            justify="center",)
        rank1head.insert(0, "1")
        rank1head.place(x=65, y=220, width=70, height=80)
        rank1head.configure(disabledbackground="#0072ff", disabledforeground="white",
                            state="disabled",)

        rank2head = Entry(root,
                        font="BurbankBigCondensed-Bold 40", 
                            width=13, 
                            borderwidth=0,
                            justify="center",)
        rank2head.insert(0, "2")
        rank2head.place(x=65, y=300, width=70, height=80)
        rank2head.configure(disabledbackground="#0072ff", disabledforeground="white",
                            state="disabled",)

        rank3head = Entry(root,
                        font="BurbankBigCondensed-Bold 40", 
                            width=13, 
                            borderwidth=0,
                            justify="center",)
        rank3head.insert(0, "3")
        rank3head.place(x=65, y=380, width=70, height=80)
        rank3head.configure(disabledbackground="#0072ff", disabledforeground="white",
                            state="disabled",)

        rank4head = Entry(root,
                        font="BurbankBigCondensed-Bold 40", 
                            width=13, 
                            borderwidth=0,
                            justify="center",)
        rank4head.insert(0, "4")
        rank4head.place(x=65, y=460, width=70, height=80)
        rank4head.configure(disabledbackground="#0072ff", disabledforeground="white",
                            state="disabled",)

        rank5head = Entry(root,
                        font="BurbankBigCondensed-Bold 40", 
                            width=13, 
                            borderwidth=0,
                            justify="center",)
        rank5head.insert(0, "5")
        rank5head.place(x=65, y=540, width=70, height=80)
        rank5head.configure(disabledbackground="#0072ff", disabledforeground="white",
                            state="disabled",)

        rank6head = Entry(root,
                        font="BurbankBigCondensed-Bold 40", 
                            width=13, 
                            borderwidth=0,
                            justify="center",)
        rank6head.insert(0, "6")
        rank6head.place(x=65, y=620, width=70, height=80)
        rank6head.configure(disabledbackground="#0072ff", disabledforeground="white",
                            state="disabled",)
        ###############################################################################################################################
        name1= StringVar()
        name1head = Entry(root,
                        font="BurbankBigCondensed-Bold 37", 
                            width=13, 
                            borderwidth=0,
                            textvariable=name1,
                            justify="center",)
        name1head.insert(0, table_data[0])
        name1head.place(x=212, y=220, width=310, height=70)
        name1head.configure(disabledbackground="#0072ff", disabledforeground="white",
                            state="disabled",)
        name1.set(table_data[0][0])
                        
        name2= StringVar()
        name2head = Entry(root,
                        font="BurbankBigCondensed-Bold 37", 
                            width=13, 
                            borderwidth=0,
                            textvariable=name2,
                            justify="center",)
        name2head.place(x=212, y=300, width=310, height=70)
        name2head.configure(disabledbackground="#0072ff", disabledforeground="white",
                            state="disabled",)
        name2.set(table_data[1][0])

        name3= StringVar()
        name3head = Entry(root,
                        font="BurbankBigCondensed-Bold 37", 
                            width=13, 
                            borderwidth=0,
                            textvariable=name3,
                            justify="center",)
        name3head.place(x=212, y=380, width=310, height=70)
        name3head.configure(disabledbackground="#0072ff", disabledforeground="white",
                            state="disabled",)
        name3.set(table_data[2][0])

        name4= StringVar()
        name4head = Entry(root,
                        font="BurbankBigCondensed-Bold 37", 
                            width=13, 
                            borderwidth=0,
                            textvariable=name4,
                            justify="center",)
        name4head.place(x=212, y=460, width=310, height=70)
        name4head.configure(disabledbackground="#0072ff", disabledforeground="white",
                            state="disabled",)
        name4.set(table_data[3][0])

        name5= StringVar()
        name5head = Entry(root,
                        font="BurbankBigCondensed-Bold 37", 
                            width=13, 
                            borderwidth=0,
                            textvariable=name5,
                            justify="center",)
        name5head.place(x=212, y=540, width=310, height=70)
        name5head.configure(disabledbackground="#0072ff", disabledforeground="white",
                            state="disabled",)
        name5.set(table_data[4][0])

        name6= StringVar()
        name6head = Entry(root,
                        font="BurbankBigCondensed-Bold 37", 
                            width=13, 
                            borderwidth=0,
                            textvariable=name6,
                            justify="center",)
        name6head.place(x=212, y=620, width=310, height=70)
        name6head.configure(disabledbackground="#0072ff", disabledforeground="white",
                            state="disabled",)
        name6.set(table_data[5][0])
        ###############################################################################################################
        school1= StringVar()
        school1head = Entry(root,
                        font="BurbankBigCondensed-Bold 25", 
                            width=7,
                            textvariable=school1, 
                            borderwidth=0,
                            justify="center",)
        school1head.insert(0, "Mayo International School")
        school1head.place(x=580, y=210, width=370, height=80)
        school1head.configure(disabledbackground="#0072ff", disabledforeground="white",
                            state="disabled",)
        school1.set(table_data[0][1])

        school2= StringVar()
        school2head = Entry(root,
                        font="BurbankBigCondensed-Bold 25", 
                            width=7,
                            textvariable=school2,
                            borderwidth=0,
                            justify="center",)
        school2head.insert(0, "Mayo International School")
        school2head.place(x=580, y=290, width=370, height=80)
        school2head.configure(disabledbackground="#0072ff", disabledforeground="white",
                            state="disabled",)
        school2.set(table_data[1][1])

        school3= StringVar()
        school3head = Entry(root,
                        font="BurbankBigCondensed-Bold 25", 
                            width=7,
                            textvariable=school3,
                            borderwidth=0,
                            justify="center",)
        school3head.insert(0, "Mayo International School")
        school3head.place(x=580, y=370, width=370, height=80)
        school3head.configure(disabledbackground="#0072ff", disabledforeground="white",
                            state="disabled",)
        school3.set(table_data[2][1])

        school4= StringVar()
        school4head = Entry(root,
                        font="BurbankBigCondensed-Bold 25", 
                            width=7,
                            textvariable=school4,
                            borderwidth=0,
                            justify="center",)
        school4head.insert(0, "Mayo International School")
        school4head.place(x=580, y=450, width=370, height=80)
        school4head.configure(disabledbackground="#0072ff", disabledforeground="white",
                            state="disabled",)
        school4.set(table_data[3][1])

        school5= StringVar()
        school5head = Entry(root,
                        font="BurbankBigCondensed-Bold 25", 
                            width=7,
                            textvariable=school5,
                            borderwidth=0,
                            justify="center",)
        school5head.insert(0, "Mayo International School")
        school5head.place(x=580, y=530, width=370, height=80)
        school5head.configure(disabledbackground="#0072ff", disabledforeground="white",
                            state="disabled",)
        school5.set(table_data[4][1])

        school6= StringVar()
        school6head = Entry(root,
                        font="BurbankBigCondensed-Bold 25", 
                            width=7,
                            textvariable=school6,
                            borderwidth=0,
                            justify="center",)
        school6head.insert(0, "Mayo International School")
        school6head.place(x=580, y=610, width=370, height=80)
        school6head.configure(disabledbackground="#0072ff", disabledforeground="white",
                            state="disabled",)
        school6.set(table_data[5][1])

        ################################################################################################################
        score1= StringVar()
        score1head = Entry(root,
                        font="BurbankBigCondensed-Bold 37", 
                            width=13,
                            textvariable=score1,
                            borderwidth=0,
                            justify="center",)
        score1head.insert(0, "40")
        score1head.place(x=1030, y=210, width=100, height=80)
        score1head.configure(disabledbackground="#0072ff", disabledforeground="white",
                            state="disabled",)
        score1.set(table_data[0][2])

        score2= StringVar()
        score2head = Entry(root,
                        font="BurbankBigCondensed-Bold 37", 
                            width=13,
                            textvariable=score2,
                            borderwidth=0,
                            justify="center",)
        score2head.insert(0, "30")
        score2head.place(x=1030, y=290, width=100, height=80)
        score2head.configure(disabledbackground="#0072ff", disabledforeground="white",
                            state="disabled",)
        score2.set(table_data[1][2])

        score3= StringVar()
        score3head = Entry(root,
                        font="BurbankBigCondensed-Bold 37", 
                            width=13,
                            textvariable=score3,
                            borderwidth=0,
                            justify="center",)
        score3head.insert(0, "10")
        score3head.place(x=1030, y=370, width=100, height=80)
        score3head.configure(disabledbackground="#0072ff", disabledforeground="white",
                            state="disabled",)
        score3.set(table_data[2][2])

        score4= StringVar()
        score4head = Entry(root,
                        font="BurbankBigCondensed-Bold 37", 
                            width=13,
                            textvariable=score4,
                            borderwidth=0,
                            justify="center",)
        score4head.insert(0, "5")
        score4head.place(x=1030, y=450, width=100, height=80)
        score4head.configure(disabledbackground="#0072ff", disabledforeground="white",
                            state="disabled",)
        score4.set(table_data[3][2])

        score5= StringVar()
        score5head = Entry(root,
                        font="BurbankBigCondensed-Bold 37", 
                            width=13,
                            textvariable=score5,
                            borderwidth=0,
                            justify="center",)
        score5head.insert(0, "0")
        score5head.place(x=1030, y=530, width=100, height=80)
        score5head.configure(disabledbackground="#0072ff", disabledforeground="white",
                            state="disabled",)
        score5.set(table_data[4][2])


        score6= StringVar()
        score6head = Entry(root,
                        font="BurbankBigCondensed-Bold 37", 
                            width=13,
                            textvariable=score6, 
                            borderwidth=0,
                            justify="center",)
        score6head.insert(0, "-20")
        score6head.place(x=1030, y=610, width=100, height=80)
        score6head.configure(disabledbackground="#0072ff", disabledforeground="white",
                            state="disabled",)
        score6.set(table_data[5][2])



    
###############FLASHSTART
    def flashcardstart():
        frame = Frame(root, width=1280, height=720)
        frame.pack()
        frame.place(anchor='center', relx=0.5, rely=0.5)
        global img
        img = PhotoImage(file="card.png")
        label = Label(frame, image = img)
        label.pack()

        mycon = mysql.connect(host='localhost', user='root', passwd='pragyan123', database='prepmaster')
        global counter


        if flashsesh == 1:
                mycursor = mycon.cursor()
                counter = 0
                mycursor.execute('select * from sci_cell;')
                flash_data = mycursor.fetchall()
                corr_ans = ''
        
        elif flashsesh == 2:
                mycursor = mycon.cursor()
                counter = 0
                mycursor.execute('select * from sci_crops;')
                flash_data = mycursor.fetchall()
                corr_ans = ''
        
        elif flashsesh == 3:
                mycursor = mycon.cursor()
                counter = 0
                mycursor.execute('select * from sci_force;')
                flash_data = mycursor.fetchall()
                corr_ans = ''

        elif flashsesh == 4:
                mycursor = mycon.cursor()
                counter = 0
                mycursor.execute('select * from math_mensuration;')
                flash_data = mycursor.fetchall()
                corr_ans = ''

        elif flashsesh == 5:
                mycursor = mycon.cursor()
                counter = 0
                mycursor.execute('select * from math_linear_eqs;')
                flash_data = mycursor.fetchall()
                corr_ans = ''

        elif flashsesh == 6:
                mycursor = mycon.cursor()
                counter = 0
                mycursor.execute('select * from social_industries;')
                flash_data = mycursor.fetchall()
                corr_ans = ''






        def flashskip1(e):
            flashskip()
        def flashback1(e):
            flashback()
        def flashflip1(e):
            flashflip()

        root.bind('<Left>',flashback1)
        root.bind('<Right>',flashskip1)
        root.bind('<space>',flashflip1)

        global buttonstatus
        buttonstatus = tk.StringVar()
        buttonstatus = "SKIP"

        def flashflip():
            global flip 
            flip = 1
            buttonstatus.set("NEXT")
            #statementtext.set("mujhe kya pata  ¯\_(ツ)_/¯ ")
            statementtext.set(flash_data[counter][1])
        
        buttonstatus = tk.StringVar()
            
        def flashquit():
            root.destroy()
            from homepagestarter import homepageaction
            homepageaction()

        display = tk.Button(root, 
                            text = '<QUIT>',
                            font='BurbankBigCondensed-Bold 35',
                            bg='#278835',
                            borderwidth=0,
                            fg='white',
                            command=flashquit).place(x=5,y=15, width=150, height=70)

        FLIPbutton = tk.Button(root, 
                            text = 'FLIP',
                            font='BurbankBigCondensed-Bold 40',
                            bg='#0073fe',
                            borderwidth=1,
                            fg='white',
                            command = flashflip).place(x=655, y=587, width=250, height=70)

        flashcardcounter = Entry(root, 
                            font="BurbankBigCondensed-Bold 35", 
                            width=13, 
                            bg="#278835",
                            borderwidth="0",
                            justify="center",
                            text = "1",
                            disabledbackground="#278835",
                            fg="white")
                            
        flashcardcounter.insert(0, "1/10")
        flashcardcounter.state="disabled"
        flashcardcounter.place(x=1100, y=2, width=200, height=70)

        def flashskip():
            global x
            global y
            global counter
            x += 1
            y = (x,"/10")
            if x == 11:
                messagebox.showinfo("SHOWINFO", "Session Complete!")
                homeflash()

            else:    
                flashcardcounter.configure(disabledbackground="#278835",state="normal",)
                flashcardcounter.delete(0,"end")
                flashcardcounter.insert(0, y)
                flashcardcounter.configure(disabledbackground="#278835",
                                        disabledforeground="white",
                                        state="disabled",)
                global buttonstatus
                buttonstatus.set("SKIP")
                counter += 1
                statementtext.set(flash_data[counter][0])

        def flashback():
            global x
            global y
            global counter

            if x <=1:
                x==1

            else:    
                x -= 1
                y = (x,"/10")
                flashcardcounter.configure(disabledbackground="#278835",state="normal",)
                flashcardcounter.delete(0,"end")
                flashcardcounter.insert(0, y)
                flashcardcounter.configure(disabledbackground="#278835",
                                        disabledforeground="white",
                                        state="disabled",)
                global buttonstatus
                buttonstatus.set("SKIP")
                counter -= 1
                statementtext.set(flash_data[counter][0])

            

        
        SKIPdisplay = tk.Button(root, 
                            textvariable=buttonstatus,
                            font='BurbankBigCondensed-Bold 40',
                            bg='#0073fe',
                            borderwidth=1,
                            fg='white',
                            command=flashskip).place(x=405, y=587, width=250, height=70)
        buttonstatus.set("SKIP")

        global texttest 
        statementtext= StringVar()
        #statementtext.set("_________ is called the powerhouse of the cell")
        statementtext.set(flash_data[counter][0])

        TEXTdisplay = Label(root, 
                            font="BurbankBigCondensed-Bold 35", 
                            width=13,
                            textvariable=statementtext,
                            wraplength=450,
                            bg="#0073fe",
                            justify="center",
                            borderwidth="5",
                            relief="solid",
                            fg="white")
        TEXTdisplay.place(x=408, y=75, width=493, height=450)
        great_font = font.Font(size = 100)
        great_display = tk.Button(root,
                        text='>',
                        font="BurbankBigCondensed-Bold 17",
                        fg="white",
                        bg="#278835",
                        width=80,
                        height=89,
                        borderwidth=0,
                        command=lambda:flashskip())
        great_display['font'] = great_font
        great_display.place(x=1190, y=332, width=80, height=100)

        less_font = font.Font(size = 100)
        less_display = tk.Button(root,
                            text='<',
                            font="BurbankBigCondensed-Bold 17",
                            fg="white",
                            bg="#278835",
                            width=80,
                            height=89,
                            borderwidth=0,
                            command=lambda:flashback())
        less_display['font'] = less_font
        less_display.place(x=5, y=332, width=80, height=100)
        root.mainloop()



##################################################################################################


    def mcqstart():
        frame = Frame(root, width=1280, height=720)
        frame.pack()
        frame.place(anchor='center', relx=0.5, rely=0.5)
        global img
        img = PhotoImage(file="mcqtestpage.png")
        label = Label(frame, image = img)
        label.pack()

        mycon = mysql.connect(host='localhost', user='root', passwd='pragyan123', database='prepmaster')

        count_button = 0
        global counter
        counter=66600
        running=False 
        global k
        k=0
        global mcqsesh

        def calculate():
            mycursor.execute('drop table student_record')
            mycursor.execute('create table student_record (marks_obtained float, correct_ans_count float,incorrect_ans_count float)')
            mycursor.execute('select * from student_response;')
            check = mycursor.fetchall()
            global marks_obtained
            correct_count = 0
            wrong_count = 0
            for i in check:
                if i[0] == i[1]:
                    correct_count = correct_count + 1
                elif i[0] == 'Null' :
                    skip_count = skip_count + 1
                else:
                    wrong_count = wrong_count + 1
            marks_obtained = (correct_count*4)-(wrong_count*1)
            mycursor.execute('insert into student_record values({},{},{})'.format(marks_obtained, correct_count, wrong_count))
            mycon.commit()
            endresult=("TEST COMPLETE! || SCORE:"+ str(marks_obtained)+ " || CORRECT:"+str(correct_count)+ " || INCORRECT:"+str(wrong_count)+ " || TIME:"+str(timerq)+ " SECONDS ||")
            messagebox.showinfo('RESULT', endresult)

            global compresult
            compresult = (marks_obtained/timerq)

            def math_mens_mcq_done():
                sql = "UPDATE account_student SET math_score = %s WHERE status = %s"
                val = (marks_obtained,1)
                mycursor.execute(sql, val)
                mycon.commit()
                messagebox.showinfo('RESULT', "DEBUG")
                root.destroy()


            if iscomp==1 and mcqsesh==1:
                math_mens_mcq_done()
            

            elif iscomp==1 and mcqsesh==2:
                sql = "UPDATE account_student SET sci_score = %s WHERE status = %s"
                val = (compresult, "1")
                mycursor.execute(sql, val)
                mycon.commit()

            else:
                messagebox.showinfo('RESULT', "DEBUG")
                





        stopwatch()

        flashcardcounter = Entry(root, 
                            font="BurbankBigCondensed-Bold 35", 
                            width=13, 
                            bg="#0072ff",
                            borderwidth="0",
                            justify="center",
                            text = "1",
                            disabledbackground="#0072ff",
                            fg="white")
                            
        flashcardcounter.insert(0, "1/10")
        flashcardcounter.state="disabled"
        flashcardcounter.place(x=1100, y=2, width=200, height=70)


        def next_q(data):
            global y
            global counter
            global k
            global x
            global count_button
            count_button = 0
            global k
            k = k+1
            y = (k+1,"/10")
            if k==10:
                global running
                running = False
                messagebox.showwarning('QUIZ COMPLETE','QUESTIONS HAVE ENDED, SESSION ENDING..')
                calculate()
            else:    
                flashcardcounter.configure(disabledbackground="#0072ff",state="normal",)
                flashcardcounter.delete(0,"end")
                flashcardcounter.insert(0, y)
                flashcardcounter.configure(disabledbackground="#0072ff",
                                        disabledforeground="white",
                                        state="disabled",)
                quizshow(k)



        def back_q(data):
            global y
            global counter
            global k
            global count_button
            count_button = 0
            if k<1:
                k==1
            else:
                k -= 1
                y = (k+1,"/10")  
                flashcardcounter.configure(disabledbackground="#0072ff",state="normal",)
                flashcardcounter.delete(0,"end")
                flashcardcounter.insert(0, y)
                flashcardcounter.configure(disabledbackground="#0072ff",
                                        disabledforeground="white",
                                        state="disabled",)
            quizshow(k)



        def ansa():
            global submitted
            submitted=("a") 
            ans_in_db()
        def ansb():
            global submitted
            submitted=("b")
            ans_in_db()
        def ansc():
            global submitted
            submitted=("c")
            ans_in_db()
        def ansd():
            global submitted
            submitted=("d")
            ans_in_db()




        mycursor.execute('drop table student_response')
        mycursor.execute('create table student_response(response char(20), answer char(20) not null)')

        def ans_in_db():
            global count_button
            count_button = count_button + 1
            if count_button > 1:
                messagebox.showerror('SHOW ERROR', 'Answer has already been submitted.')
            else:
                if submitted==("a") :
                    ansresponse = option_a
                elif submitted==("b") :
                    ansresponse = option_b
                elif submitted==("c") :
                    ansresponse = option_c
                elif submitted==("d") :
                    ansresponse = option_d
                mycursor = mycon.cursor()
                mycursor.execute('insert into student_response values("%s","%s");'%(ansresponse, correct_ans))
                mycon.commit()



        def quizshow(k):      

            global option_a
            global option_b
            global option_c
            global option_d

            global correct_ans
            correct_ans = data[k][1]
            list_ans = [data[k][1],data[k][2],data[k][3],data[k][4]]
            random.shuffle(list_ans)
            option_a = list_ans[0]
            option_b = list_ans[1]
            option_c = list_ans[2]
            option_d = list_ans[3]

            question = data[k][0]
            question_label = tk.Label(root,
                                text=question,
                                font='BurbankBigCondensed-Bold 30',
                                bg='#0c5dc0',
                                fg='white').place(x=43, y=330, width=1205, height=110)

            option_1 = tk.Button(root,
                            text=option_a,
                            font='BurbankBigCondensed-Bold 20',
                            bg='#B327C4',
                            fg='white',
                            command=lambda:ansa()).place(x=125, y=470, width=457, height=75)

            option_2 = tk.Button(root,
                            text=option_b,
                            font='BurbankBigCondensed-Bold 20',
                            bg='#22C53A',
                            fg='white',
                            command=lambda:ansb()).place(x=743, y=470, width=457, height=75)

            option_3 = tk.Button(root,
                            text=option_c,
                            font='BurbankBigCondensed-Bold 20',
                            bg='#C5AE22',
                            fg='white',
                            command=lambda:ansc()).place(x=125, y=590, width=457, height=75)


            option_4 = tk.Button(root,
                            text=option_d,
                            font='BurbankBigCondensed-Bold 20',
                            bg='#D92B2B',
                            fg='white',
                            command=lambda:ansd()).place(x=741, y=590, width=457, height=75)



            timer_1 = tk.Button(root,
                            bg='#3D3F41',
                            fg='white',
                            borderwidth=0,
                            command=lambda:stopwatch().place(x=550, y=257, width=220, height=74))
            

                
            ###################################################################
            great_font = font.Font(size = 100)
            great_display = tk.Button(root,
                            text='>',
                            font="BurbankBigCondensed-Bold 17",
                            fg="white",
                            bg="#0072ff",
                            width=80,
                            height=89,
                            borderwidth=0,
                            command=lambda:next_q(data))
            great_display['font'] = great_font
            great_display.place(x=1190, y=210, width=80, height=100)

            less_font = font.Font(size = 100)
            less_display = tk.Button(root,
                                text='<',
                                font="BurbankBigCondensed-Bold 17",
                                fg="white",
                                bg="#0072ff",
                                width=80,
                                height=89,
                                borderwidth=0,
                                command=lambda:back_q(data))
            less_display['font'] = less_font
            less_display.place(x=5, y=210, width=80, height=100)

            def mcqquit():
                root.destroy()
                from homepagestarter import homepageaction
                homepageaction()


            button_back = tk.Button(root,
            text='<QUIT>',
            font='BurbankBigCondensed-Bold 35',
            bg='#0072ff',
            fg='white',
            borderwidth=0,
            command = lambda:mcqquit()).place(x=5,y=15, width=150, height=70)

            def next1(e):
                next_q(data)
            def back1(e):
                back_q(data)

            root.bind('<Left>',back1)
            root.bind('<Right>',next1)
            root.mainloop()
        quizshow(k)
        root.mainloop()


            ################################################################

                           

    homeflash()
    

    root.mainloop()
homepageaction()