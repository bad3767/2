from tkinter import *
from PIL import ImageTk,Image
import os

root = Tk()

root.geometry("850x500")

a=ImageTk.PhotoImage(Image.open("C:\\Users\\Magesh\\AppData\\Local\\Programs\\Python\\Python310\\3.jpg"))
b=Label(root,image=a)
b.pack()

root.mainloop()
