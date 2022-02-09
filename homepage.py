from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import importlib

def homepageaction():
    homepage = Tk()
    homepage.title("PrepMasterBETA")
    homepage.geometry("1280x720")   
    bg = PhotoImage(file = "home1.png")
    homepage.eval('tk::PlaceWindow . center')
    label2 = Label( homepage, image = bg)
    label2.place(x = 0, y = 0)
    homepage.resizable(False, False)