import tkinter as tk
from turtle import width
root = tk.Tk()
root.geometry('1280x720')
root.title('MCQ PAGE')
root.resizable(False, False)
bg = tk.PhotoImage(file='mcqtestpage.png')
root.eval('tk::PlaceWindow . center')
label1 = tk.Label(root, image= bg)
label1.place(x=0, y=0)

question = 'THIS IS A SAMPLE QUESTION'
question_label = tk.Label(root,
                    text=question,
                    font='BurbankBigCondensed-Bold 30',
                    bg='#0c5dc0',
                    fg='white').place(x=43, y=330, width=1205, height=110)

option_a = 'OPTION A'
option_1 = tk.Button(root,
                text=option_a,
                font='BurbankBigCondensed-Bold 20',
                bg='#B327C4',
                fg='white').place(x=125, y=470, width=457, height=75)

option_b = 'OPTION B'
option_2 = tk.Button(root,
                text=option_b,
                font='BurbankBigCondensed-Bold 20',
                bg='#22C53A',
                fg='white').place(x=743, y=470, width=457, height=75)

option_c = 'OPTION C'
option_3 = tk.Button(root,
                text=option_c,
                font='BurbankBigCondensed-Bold 20',
                bg='#C5AE22',
                fg='white').place(x=125, y=590, width=457, height=75)

option_d = 'OPTION D'
option_4 = tk.Button(root,
                text=option_d,
                font='BurbankBigCondensed-Bold 20',
                bg='#D92B2B',
                fg='white').place(x=741, y=590, width=457, height=75)

timer = '02:24'
timer_1 = tk.Label(root,
                text=timer,
                font='BurbankBigCondensed-Bold 20',
                bg='#3D3F41',
                fg='white').place(x=550, y=257, width=220, height=74)

swap = '1/4'
swap_1 = tk.Label(root,
                text=swap,
                font='BurbankBigCondensed-Bold 20',
                bg='#3D3F41',
                fg='white').place(x=1, y=2, width=150, height=70)
next= tk.Button(root,
            text='NEXT',
            font='BurbankBigCondensed-Bold 30',
            bg='#3D3F41',
            fg='white').place(x=1127, y=2, width=150, height=70)

root.mainloop()