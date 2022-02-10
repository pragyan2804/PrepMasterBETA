import tkinter as tk
import tkinter.font as font
root = tk.Tk()
root.title('HOME PAGE')
root.geometry("1280x720")
root.resizable(False, False)
bg = tk.PhotoImage(file='homedoubt.png')
root.eval('tk::PlaceWindow . center')
label1 = tk.Label( root, image = bg)
label1.place(x = 0, y = 0)

great_font = font.Font(size = 100)
great_display = tk.Button(root,
                    text='>',
                    font="BurbankBigCondensed-Bold 17",
					fg="white",
					bg="#B327C4",
                    width=80,
                    height=89,
                    borderwidth=0)
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
                    borderwidth=0)
less_display['font'] = less_font
less_display.place(x=5, y=332, width=80, height=100)

display = tk.Button(root, 
                    text = 'GO',
                    font='BurbankBigCondensed-Bold 25',
                    bg='#57595c',
                    fg='white').place(x=508, y=495, width=300, height=70)

display = tk.Button(root,
					text="<SIGN OUT>",
					font="BurbankBigCondensed-Bold 17",
					fg="black",
					bg="#B327C4",
					borderwidth=0,).place(x=980, y=1.15, width=300, height=50)
root.mainloop()