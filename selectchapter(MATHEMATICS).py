def selectchapter(maths):
    import tkinter as tk
    root = tk.Tk()
    root.geometry('1280x720')
    root.title('SELECT CHAPTER (MATHEMATICS)')
    root.resizable(False, False)
    root.config(bg='#0073FF')
    root.eval('tk::PlaceWindow . center')
    label_heading = tk.Label(root,
                        text='SELECT CHAPTER',
                        justify='center',
                        font='BurbankBigCondensed-Bold 70',
                        bg='#0073FF',
                        fg='white',
                        borderwidth=0).place(x=220, y=70, width=500, height=100)

    button_1 = tk.Button(root,
                    text='CHAPTER 1',
                    font='BurbankBigCondensed-Bold 40',
                    bg='#FE7D05',
                    fg='white').place(x=63, y=220, width=263, height=200)

    button_2 = tk.Button(root,
                    text='CHAPTER 2',
                    font='BurbankBigCondensed-Bold 40',
                    bg='#7FD10B',
                    fg='white').place(x=363, y=220, width=263, height=200)

    button_3 = tk.Button(root,
                    text='CHAPTER 3',
                    font='BurbankBigCondensed-Bold 40',
                    bg='#CD043F',
                    fg='white').place(x=663, y=220, width=263, height=200)

    button_4 = tk.Button(root,
                    text='CHAPTER 4',
                    font='BurbankBigCondensed-Bold 40',
                    bg='#F30C0D',
                    fg='white').place(x=199, y=520, width=263, height=200)

    button_5 = tk.Button(root,
                    text='CHAPTER 5',
                    font='BurbankBigCondensed-Bold 40',
                    bg='#FFCA34',
                    fg='white').place(x=499, y=520, width=263, height=200)

    button_back = tk.Button(root,
                    text='<BACK>',
                    font='BurbankBigCondensed-Bold 35',
                    bg='#0072ff',
                    fg='white',
                    borderwidth=0).place(x=5,y=15, width=150, height=70)

    root.mainloop()