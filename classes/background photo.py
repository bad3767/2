# Import required libraries
from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("window")

img = ImageTk.PhotoImage(Image.open("D:\22.jpg"))


label = Label(image=img)
label.pack()

root.mainloop()
