from re import A, X
import tkinter as tk
from tkinter import Entry, font
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
label1 = tk.Label(root, image= bg)
label1.place(x=0, y=0)
mycon = mysql.connect(host='localhost', user='root', passwd='pragyan123', database='prepmaster')
mycursor = mycon.cursor()
count_button = 0
counter=66600
running=False 
k=0
global mcqsesh
mcqsesh=2

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
    root.destroy()



def stopwatch(): 
    frame= tk.Frame(root,
                width= 210, height=150)
    frame.place(x=609, y=275)
    label = tk.Label(frame, text="Let's Begin!", fg="white", bg="#3C4142", font="BurbankBigCondensed-Bold 40")
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
                        string = tt.strftime("%M:%S")
                        display=string
        
                    label['text']=display   
        
                
                    label.after(1000, count) 
                    counter += 1
                    global timerq
                    timerq=counter-66600
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
    if k<=1:
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
    if mcqsesh==1:     
        mycursor.execute('select * from math_mens_mcq;')
        data = mycursor.fetchall()

    elif mcqsesh==2:
        mycursor.execute('select * from sci_cell_mcq;')
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

    def next1(e):
        next_q(data)
    def back1(e):
        back_q(data)

    root.bind('<Left>',back1)
    root.bind('<Right>',next1)



    ################################################################

    root.mainloop()


quizshow(k)










