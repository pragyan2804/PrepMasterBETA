import tkinter as tk
root = tk.Tk()
root.title('HOME PAGE')
root.geometry("1000x720")
root.resizable(False, False)
bg = tk.PhotoImage(file='homedoubt (1000x720).png')
root.eval('tk::PlaceWindow . center')
label1 = tk.Label( root, image = bg)
label1.place(x = 0, y = 0)

display = tk.Button(root, 
                    text = 'GO',
                    font='BurbankBigCondensed-Bold 25',
                    bg='#57595c',
                    fg='white').place(x=390, y=387, width=250, height=50)

display = tk.Button(root,
					text="<SIGN OUT>",
					font="BurbankBigCondensed-Bold 17",
					fg="black",
					bg="#B327C4",
					borderwidth=0,).place(x=780, y=1.15, width=300, height=50)
root.mainloop()