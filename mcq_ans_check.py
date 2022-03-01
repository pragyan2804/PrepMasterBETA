'''import tkinter as tk
import mysql.connector as mysql
from tkinter import messagebox
from datetime import datetime
from turtle import width
import random 

def mathtest():
    root = tk.Tk()
    root.geometry('1280x720')
    root.title('MCQ PAGE')
    root.resizable(False, False)
    bg = tk.PhotoImage(file='mcqtestpage.png')
    root.eval('tk::PlaceWindow . center')
    label1 = tk.Label(root, image= bg)
    label1.place(x=0, y=0)
    mycon = mysql.connect(host='localhost', user='root', passwd='comp123', database='prepmaster')
    mycursor = mycon.cursor()
    count_button = 0
    counter=66600
    running=False 
    k=0

    def calculate():
        mycursor.execute('delete from student_record;')
        mycursor.execute('select * from student_response;')
        check = mycursor.fetchall()
        mycursor.execute('delete from student_response;')    
        global marks_obtained
        correct_count = 0
        wrong_count = 0
        for i in check:
            if i[0] == i[1]:
                correct_count = correct_count + 1
            #elif i[0] == 'Null' :
            #    skip_count = skip_count + 1
            else:
                wrong_count = wrong_count + 1
        marks_obtained = (correct_count*4)-(wrong_count*1)
        mycursor.execute('insert into student_record values({},{},{})'.format(marks_obtained, correct_count, wrong_count))
        mycon.commit()



    def stopwatch(): 
        frame= tk.Frame(root,
                    width= 180, height=70)
        frame.place(x=560, y=257)
        label = tk.Label(frame, text="Let's Begin!", fg="white", bg="#3C4142", font="BurbankBigCondensed-Bold 50")
        label.pack()
        f = tk.Frame(root)
        def counter_label(label):
                def count():
                    if running:
                        global counter
                        if counter==66600:            
                            display="Starting..."
                        else:
                            tt = datetime.fromtimestamp(counter)
                            string = tt.strftime("%H:%M:%S")
                            display=string
            
                        label['text']=display   
            
                    
                        label.after(1000, count) 
                        counter += 1
                count()     
        def Start(label):
                global running
                running=True
                counter_label(label)
        def Stop():
                global running
                running = False

        frame.after(0)
        Start(label)
    stopwatch()


    def next_q(data):
        global k
        global count_button
        count_button = 0
        k = k+1
        if k>9:
            #Stop()
            #messagebox.showwarning('SHOW WARNING','QUESTIONS HAVE ENDED')
            calculate()
            root.destroy()
        math_mens(k)

    #mycursor.execute('create table student_response(q_no varchar(30) primary key, response char(1), answer char(1) not null)')
    def ans_in_db(args):
        global count_button
        count_button = count_button + 1
        if count_button > 1:
            messagebox.showerror('SHOW ERROR', 'Answer has already been submitted.')
        if args == 'A':
            response = option_a
        elif args == 'B':
            response = option_b
        elif args == 'C':
            response = option_c
        elif args == 'D':
            response = option_d
        mycursor.execute('insert into student_response values("{}","{}")'.format(response, correct_ans,))
        mycon.commit()



    def math_mens(k):           
        mycursor.execute('select * from math_mens_mcq;')
        data = mycursor.fetchall()
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
                        command=lambda:ans_in_db('A')).place(x=125, y=470, width=457, height=75)

        option_2 = tk.Button(root,
                        text=option_b,
                        font='BurbankBigCondensed-Bold 20',
                        bg='#22C53A',
                        fg='white',
                        command=lambda:ans_in_db('B')).place(x=743, y=470, width=457, height=75)

        option_3 = tk.Button(root,
                        text=option_c,
                        font='BurbankBigCondensed-Bold 20',
                        bg='#C5AE22',
                        fg='white',
                        command=lambda:ans_in_db('C')).place(x=125, y=590, width=457, height=75)


        option_4 = tk.Button(root,
                        text=option_d,
                        font='BurbankBigCondensed-Bold 20',
                        bg='#D92B2B',
                        fg='white',
                        command=lambda:ans_in_db('D')).place(x=741, y=590, width=457, height=75)

        swap_1 = tk.Label(root,
                        #text=swap,
                        font='BurbankBigCondensed-Bold 20',
                        bg='#3D3F41',
                        fg='white').place(x=1127, y=2, width=150, height=70)

        timer_1 = tk.Button(root,
                        bg='#3D3F41',
                        fg='white',
                        borderwidth=0,
                        command=lambda:stopwatch().place(x=550, y=257, width=220, height=74))
        
        next= tk.Button(root,
                text='NEXT',
                font='BurbankBigCondensed-Bold 30',
                bg='#3D3F41',
                fg='white',
                command=lambda:next_q(data)).place(x=1127, y=2, width=150, height=70)

        root.mainloop()

    math_mens(k)
mathtest()'''


import math
import tkinter as tk
import mysql.connector as mysql
from tkinter import messagebox
from datetime import datetime
from turtle import width
import random 


root = tk.Tk()
root.geometry('1280x720')
root.title('MCQ PAGE')
root.resizable(False, False)
bg = tk.PhotoImage(file='mcqtestpage.png')
root.eval('tk::PlaceWindow . center')
label1 = tk.Label(root, image= bg)
label1.place(x=0, y=0)
mycon = mysql.connect(host='localhost', user='root', passwd='comp123', database='prepmaster')
mycursor = mycon.cursor()
count_button = 0
counter=66600
running=False 
k=0

def calculate():
    mycursor.execute('delete from student_record;')
    mycursor.execute('select * from student_response;')
    check = mycursor.fetchall()
    mycursor.execute('delete from student_response;')    
    global marks_obtained
    correct_count = 0
    wrong_count = 0
    for i in check:
        if i[0] == i[1]:
            correct_count = correct_count + 1
        #elif i[0] == 'Null' :
        #    skip_count = skip_count + 1
        else:
            wrong_count = wrong_count + 1
    marks_obtained = (correct_count*4)-(wrong_count*1)
    mycursor.execute('insert into student_record values({},{},{})'.format(marks_obtained, correct_count, wrong_count))
    mycon.commit()



def stopwatch(): 
    frame= tk.Frame(root,
                width= 180, height=70)
    frame.place(x=560, y=257)
    label = tk.Label(frame, text="Let's Begin!", fg="white", bg="#3C4142", font="BurbankBigCondensed-Bold 50")
    label.pack()
    f = tk.Frame(root)
    def counter_label(label):
            def count():
                if running:
                    global counter
                    if counter==66600:            
                        display="Starting..."
                    else:
                        tt = datetime.fromtimestamp(counter)
                        string = tt.strftime("%H:%M:%S")
                        display=string
        
                    label['text']=display   
        
                
                    label.after(1000, count) 
                    counter += 1
            count()     
    def Start(label):
            global running
            running=True
            counter_label(label)
    def Stop():
            global running
            running = False

    frame.after(0)
    Start(label)
stopwatch()


def next_q(data):
    global k
    global count_button
    count_button = 0
    k = k+1
    if k>9:
        #Stop()
        #messagebox.showwarning('SHOW WARNING','QUESTIONS HAVE ENDED')
        calculate()
        root.destroy()
        from homepagestarter_new import homepageaction
        homepageaction()
    math_mens(k)

#mycursor.execute('create table student_response(q_no varchar(30) primary key, response char(1), answer char(1) not null)')
def ans_in_db(args):
    global count_button
    count_button = count_button + 1
    if count_button > 1:
        messagebox.showerror('SHOW ERROR', 'Answer has already been submitted.')
    if args == 'A':
        response = option_a
    elif args == 'B':
        response = option_b
    elif args == 'C':
        response = option_c
    elif args == 'D':
        response = option_d
    mycursor.execute('insert into student_response values("{}","{}")'.format(response, correct_ans,))
    mycon.commit()



def math_mens(k):           
    mycursor.execute('select * from math_mens_mcq;')
    data = mycursor.fetchall()
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
                    command=lambda:ans_in_db('A')).place(x=125, y=470, width=457, height=75)

    option_2 = tk.Button(root,
                    text=option_b,
                    font='BurbankBigCondensed-Bold 20',
                    bg='#22C53A',
                    fg='white',
                    command=lambda:ans_in_db('B')).place(x=743, y=470, width=457, height=75)

    option_3 = tk.Button(root,
                    text=option_c,
                    font='BurbankBigCondensed-Bold 20',
                    bg='#C5AE22',
                    fg='white',
                    command=lambda:ans_in_db('C')).place(x=125, y=590, width=457, height=75)


    option_4 = tk.Button(root,
                    text=option_d,
                    font='BurbankBigCondensed-Bold 20',
                    bg='#D92B2B',
                    fg='white',
                    command=lambda:ans_in_db('D')).place(x=741, y=590, width=457, height=75)

    swap_1 = tk.Label(root,
                    #text=swap,
                    font='BurbankBigCondensed-Bold 20',
                    bg='#3D3F41',
                    fg='white').place(x=1127, y=2, width=150, height=70)

    timer_1 = tk.Button(root,
                    bg='#3D3F41',
                    fg='white',
                    borderwidth=0,
                    command=lambda:stopwatch().place(x=550, y=257, width=220, height=74))
    
    next= tk.Button(root,
            text='NEXT',
            font='BurbankBigCondensed-Bold 30',
            bg='#3D3F41',
            fg='white',
            command=lambda:next_q(data)).place(x=1127, y=2, width=150, height=70)

    root.mainloop()

math_mens(k)

