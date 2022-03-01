# Python program to illustrate a stop watch
# using Tkinter
#importing the required libraries
'''import tkinter as Tkinter
from datetime import datetime

counter = 66600
running = False

def counter_label(label):
    def count():
        if running:
            global counter
   
            # To manage the initial delay.
            if counter==66600:            
                display="Starting..."
            else:
                tt = datetime.fromtimestamp(counter)
                string = tt.strftime("%H:%M:%S")
                display=string
   
            label['text']=display   # Or label.config(text=display)
   
            # label.after(arg1, arg2) delays by 
            # first argument given in milliseconds
            # and then calls the function given as second argument.
            # Generally like here we need to call the 
            # function in which it is present repeatedly.
            # Delays by 1000ms=1 seconds and call count again.
            label.after(1000, count) 
            counter += 1
   
    # Triggering the start of the counter.
    count()     
   
# start function of the stopwatch
def Start(label):
    global running
    running=True
    counter_label(label)
   
# Stop function of the stopwatch
def Stop():
    global running
    running = False

root = Tkinter.Tk()
root.title("Stopwatch")
root.configure(bg="#3C4142")
   
# Fixing the window size.
root.minsize(width=250, height=70)
label = Tkinter.Label(root, text="Let's Begin!", fg="white", bg="#3C4142", font="BurbankBigCondensed-Bold 50")
label.pack()
f = Tkinter.Frame(root)

root.after(2000)
Start(label)

#Stop()
root.mainloop()'''

from tkinter import *

ws = Tk()
ws.geometry('400x450+1000+300')
ws.title('PythonGuides: Stopwatch')
ws.config(bg='#299617')
ws.iconbitmap('stopwatch.ico')
ws.resizable(0,0)


counter = -1
running = False
def counter_label(lbl):
    def count():
        if running:
            global counter
            if counter==-1:             
                display="00"
            else:
                display=str(counter)

            lbl['text']=display    
            
            lbl.after(1000, count)    
            counter += 1
    count()     

def StartTimer(lbl):
    global running
    running=True
    counter_label(lbl)
    start_btn['state']='disabled'
    stop_btn['state']='normal'
    reset_btn['state']='normal'

def StopTimer():
    global running
    start_btn['state']='normal'
    stop_btn['state']='disabled'
    reset_btn['state']='normal'
    running = False

def ResetTimer(lbl):
    global counter
    counter=-1
    if running==False:      
        reset_btn['state']='disabled'
        lbl['text']='00'
    else:                          
        lbl['text']=''

bg = PhotoImage(file='stopwatch.png')
img = Label(ws, image=bg, bg='#299617')
img.place(x=75, y=50)

lbl = Label(
    ws, 
    text="00", 
    fg="black", 
    bg='#299617', 
    font="Verdana 40 bold"
    )

label_msg = Label(
    ws, text="minutes", 
    fg="black", 
    bg='#299617', 
    font="Verdana 10 bold"
    )

lbl.place(x=160, y=170)
label_msg.place(x=170, y=250)

start_btn=Button(
    ws, 
    text='Start', 
    width=15, 
    command=lambda:StartTimer(lbl)
    )

stop_btn = Button(
    ws, 
    text='Stop', 
    width=15, 
    state='disabled', 
    command=StopTimer
    )

reset_btn = Button(
    ws, 
    text='Reset', 
    width=15, 
    state='disabled', 
    command=lambda:ResetTimer(lbl)
    )

start_btn.place(x=30, y=390)
stop_btn.place(x=150, y=390)
reset_btn.place(x=270, y=390)



ws.mainloop()