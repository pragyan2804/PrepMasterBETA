from cProfile import label
from importlib.metadata import entry_points
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

mycon = mysql.connect(host='localhost', user='root', passwd='pragyan123', database='prepmaster')
root = tk.Tk()
root.geometry('1280x720')
root.title('MCQ PAGE')
root.resizable(False, False)
bg = tk.PhotoImage(file='chapbg.png')
label1 = tk.Label(root, image= bg)
label1.place(x=0, y=0)

global leaderselect
leaderselect = int
leaderselect==1

if leaderselect==1:
    mycursor = mycon.cursor()
    mycursor.execute('select fullname,school,sst_score from account_student order by sst_score desc;')
    table_data = mycursor.fetchall()

elif leaderselect==2:
    mycursor = mycon.cursor()
    mycursor.execute('select fullname,school,math_score from account_student order by math_score desc;')
    table_data = mycursor.fetchall()    

elif leaderselect==3:
    mycursor = mycon.cursor()
    mycursor.execute('select fullname,school,sci_score from account_student order by sci_score desc;')
    table_data = mycursor.fetchall()   






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
                borderwidth=0).place(x=5,y=15, width=150, height=70)

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





























root.mainloop()