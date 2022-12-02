'''
import pywhatkit
pywhatkit.sendwhatmsg("+91 9500196179"," hi ",16,10)
'''

from tkinter import *
import tkinter as tk
def  home():
    hm=tk.Tk()
    hm.geometry("400x500")
    l=Label(hm,text="Home")
    
    l.pack()
    b2=Button(hm,text="file",command=file)
    b2.pack()
    b3=Button(hm,text="edit",command=edit)
    b3.pack()
    b4=Button(hm,text="exit",command=exit)
    b4.pack()
    mainloop()


def file ():
    fl=tk.Tk()
    fl.geometry("200x200")
    l2=Label(fl,text="file")
    l2.pack()
    un= Label(fl,text="un")
    un.pack()
    e= Entry(fl)
    e.pack()

    
def edit ():
    ed=tk.Tk()
    ed.geometry("200x300")
    l3=Label(ed,text="edit")
    l3.pack()

def exit ():
    ex=tk.Tk()
    ex.geometry("200x400")
    l4=Label(ex,text="exit")
    l4.pack()

home()
