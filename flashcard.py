from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import importlib
import tkinter
from tkinter import font
from tkinter.tix import IMAGETEXT
from unittest import TextTestResult
import PIL
from PIL import Image
import tkinter as tk
import tkinter.font as font
import mysql.connector as mysql

global x 
x = 1
global flip 
flip = 0


#considering only science flashcard questions
def flashcardscreen():
    root= Tk()
    root.title("PrepMasterBETA")
    root.geometry("1280x720")
    root.resizable(False, False)
    bg = PhotoImage(file= "card.png")
    label1 = Label(root, image = bg)
    label1.place(x=0, y=0)
    mycon = mysql.connect(host='localhost', user='root', passwd='dhruv_789_$1', database='prepmaster')
    mycursor = mycon.cursor()
    global counter
    counter = 0
    mycursor.execute('select * from sci_cell;')
    flash_data = mycursor.fetchall()
    corr_ans = ''

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
        #from homepagestarter import homepageaction
        #homepageaction()

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


    root.mainloop()

flashcardscreen()