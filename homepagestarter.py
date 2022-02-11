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
from login import loginaction


def homepageaction():
    root = Tk()
    root.geometry("1280x720")
    root.title("PrepMasterBETA")
    root.resizable(False, False)

    def signout():
        root.destroy()
        loginaction()


    def homeflash():
        frame = Frame(root, width=1280, height=720)
        frame.pack()
        frame.place(anchor='center', relx=0.5, rely=0.5)
        global img
        img = PhotoImage(file="CORE\homeflash.png")
        label = Label(frame, image = img)
        label.pack()
        global x
        x = 1

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
        img = PhotoImage(file="CORE\homemcq.png")
        label = Label(frame, image = img)
        label.pack()
        global x
        x = 2

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
        img = PhotoImage(file="CORE\homeleader.png")
        label = Label(frame, image = img)
        label.pack()
        global x
        x = 3

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
                            text="<SIGN OUT>",
                            font="BurbankBigCondensed-Bold 17",
                            fg="black",
                            bg="#C5AE22",
                            borderwidth=0,).place(x=970, y=1.15, width=300, height=50)
                        
    def homedoubt():
        frame = Frame(root, width=1280, height=720)
        frame.pack()
        frame.place(anchor='center', relx=0.5, rely=0.5)
        global img
        img = PhotoImage(file="CORE\homedoubt.png")
        label = Label(frame, image = img)
        label.pack()

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
        img = PhotoImage(file="CORE\selecttest.png")
        label = Label(frame, image = img)
        label.pack()

        button_mcq = tk.Button(root,
                text='STANDARD MCQ TEST',
                font='BurbankBigCondensed-Bold 40',
                bg='#c32b2b',
                fg='white',
                command = lambda:selectsubject()).place(x=63, y=240, width=500, height=300)

        button_mcq_comp = tk.Button(root,
                text='COMPETITIVE MASTERTEST',
                font='BurbankBigCondensed-Bold 35',
                bg='#c32b2b',
                fg='white',
                command = lambda:selectsubject()).place(x=723, y=240, width=500, height=300)

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
        img = PhotoImage(file="CORE\selectsubject.png")
        label = Label(frame, image = img)
        label.pack()

        
        if x ==1:
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



        button_sst = tk.Button(root,
                        text='SST',
                        font='BurbankBigCondensed-Bold 40',
                        bg='#9518a4',
                        fg='white',).place(x=86, y=350, width=325, height=195)

        button_maths = tk.Button(root,
                        text='MATHS',
                        font='BurbankBigCondensed-Bold 40',
                        bg='#ab9623',
                        fg='white',).place(x=496, y=350, width=325, height=195)

        button_maths = tk.Button(root,
                        text='SCIENCE',
                        font='BurbankBigCondensed-Bold 40',
                        bg='#1eaf32',
                        fg='white',).place(x=894, y=350, width=325, height=195)
                            

    homeflash()

    root.mainloop()