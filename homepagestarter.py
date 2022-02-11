from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import importlib
import tkinter
from tkinter import font
import matplotlib
from tkinter.tix import IMAGETEXT
import PIL
from PIL import Image
import tkinter as tk
import tkinter.font as font
from login import loginaction

root = Tk()
root.geometry("1280x720")
root.title("PrepMasterBETA")

def signout():
    root.destroy()
    loginaction()


def homeflash():
    frame = Frame(root, width=1280, height=720)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)
    global img
    img = PhotoImage(file="homeflash.png")
    label = Label(frame, image = img)
    label.pack()

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
                        text = 'GO',
                        font='BurbankBigCondensed-Bold 25',
                        bg='#57595c',
                        fg='white').place(x=480, y=490, width=320, height=75)

    display = tk.Button(root,
                        text="<SIGN OUT>",
                        font="BurbankBigCondensed-Bold 17",
                        fg="black",
                        bg="#22C53A",
                        borderwidth=0,
                        command = lambda:signout()
                        ).place(x=900, y=1.15, width=500, height=50)


def homemcq():
    frame = Frame(root, width=1280, height=720)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)
    global img
    img = PhotoImage(file="homemcq.png")
    label = Label(frame, image = img)
    label.pack()

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
                        text = 'GO',
                        font='BurbankBigCondensed-Bold 25',
                        bg='#57595c',
                        fg='white').place(x=487, y=492, width=320, height=75)

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
                        text = 'GO',
                        font='BurbankBigCondensed-Bold 25',
                        bg='#57595c',
                        fg='white').place(x=500, y=490, width=320, height=75)

    display = tk.Button(root,
                        text="<SIGN OUT>",
                        font="BurbankBigCondensed-Bold 17",
                        fg="black",
                        bg="#C5AE22",
                        borderwidth=0,).place(x=980, y=1.15, width=300, height=50)
                    
def homedoubt():
    frame = Frame(root, width=1280, height=720)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)
    global img
    img = PhotoImage(file="homedoubt.png")
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
                        text = 'GO',
                        font='BurbankBigCondensed-Bold 25',
                        bg='#57595c',
                        fg='white').place(x=503, y=490, width=320, height=75)

    display = tk.Button(root,
                        text="<SIGN OUT>",
                        font="BurbankBigCondensed-Bold 17",
                        fg="black",
                        bg="#B327C4",
                        borderwidth=0,
                        command = lambda:signout()).place(x=980, y=1.15, width=300, height=50)
                        

homeflash()

root.mainloop()