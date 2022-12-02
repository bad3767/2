from tkinter import *
from tkinter import messagebox
import tkinter as tk

a=Tk()
a.title("login")
a.geometry("800x500")
a.config(bg="red")
s = StringVar()
o= IntVar()
l1=Label(a,text="login form",fg="white",bg="black",font=("latin",20,"italic"))
l1.pack()
l2=Label(a,text="user name")
l2.place(x=100,y=150)
l3=Entry(a)
l3.place(x=200,y=150)
l4=Label(a,text="password")
l4.place(x=100,y=200)
l5=Entry(a,bg="white")
l5.place(x=200,y=200)
l7=Label(a,text="gender")
l7.place(x=100,y=250)

def male():
    messagebox.showinfo("Alert","Male gender is selected")

def female():
    messagebox.showinfo("Alert","Female gen is sel")

rb = Radiobutton(a,text="Male",variable=s , value="Male")
rb.place(x=200,y=250)

rb1 = Radiobutton(a,text="Female",variable =s , value="Female" )
rb1.place(x=270,y=250)

ck = Checkbutton(a,text="Accept ur T & C",variable=o,onvalue=1,offvalue=0)
ck.place(x=150,y=300)

p1 = Label(a,text="ur name")
p1.place(x=400,y=150)

p2 = Label(a,text="password")
p2.place(x=400,y=200)

p3 = Label(a,text="male or female")
p3.place(x=400,y=250)

p4 = Label(a,text="T & C")
p4.place(x=400,y=300)
def sub():
    ans1 = "Username : "+ l3.get()
    ans2 = "Password : "+l5.get()
    ans3 = "Gender : " + s.get()
    ans4 = o.get()
    print(ans1)
    print(ans2)
    print(ans3)
    if ans4==1:
        h = "Status Checked"
        print(h)
    else:
        h = "Status Unhecked"
        print(h)

    p1.config(text=ans1)
    p2.config(text=ans2)
    p3.config(text=ans3)
    p4.config(text=h)
    
def sub():
    sb=tk.Tk()
    sb.geometry("500x500")
    sb.title("login")
    
    
l6=Button(a,text="Submit",command=sub)
l6.place(x=200,y=350)

a.mainloop()
