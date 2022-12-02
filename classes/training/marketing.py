
from tkinter import *
from tkinter import messagebox
import tkinter as ak
from PIL import ImageTk,Image
import os
import pymysql




b=ak.Tk()
b.title("REPORT")
b.geometry("850x500")
b.config(bg="CYAN")

img=ImageTk.PhotoImage(Image.open("D:\\magesh pics\\pic\\IMG_20220126_205646.jpg"))
img1=Label(b,image=img)
img1.pack()

def Login():
    f1=Frame(bg="CYAN")
    f1.place(x=0,y=0,width=850,height=500)

    L1=Label(f1,text="SELECT ANYONE CENTER",fg="BLACK",bg="CYAN",font=("times new roman",30))
    L1.pack()

    b2=Button(f1,text="Avadi",font=("times new roman",15),command=Avadi)
    b2.pack()
    
    b3=Button(f1,text="Padi",font=("times new roman",15),command=PADI)
    b3.pack()
    
    b4=Button(f1,text="Ambattur",font=("times new roman",15),command=Ambattur)
    b4.pack()
    
    b5=Button(f1,text="Porur",font=("times new roman",15),command=Porur)
    b5.pack()
    

    
i1=Label (b,text="login_Form",fg="red",bg="yellow",font=("latin",20,"italic"))
i1.place(x=400,y=40)

    
        
un=Label(b,text="User_Name",fg="yellow",bg="blue")
un.place(x=300,y=100)
ue=Entry(b)
ue.place(x=450,y=100)

pw=Label(b,text="Password",fg="yellow",bg="blue")
pw.place(x=300,y=150)
pe=Entry(b)
pe.place(x=450,y=150)



def check():
    if ue.get()=="" or pe.get()=="":
        messagebox.showerror("Error","All fields are required")
    elif ue.get()!="magesh@gmail.com" or pe.get()!="Magesh":
        messagebox.showerror("Error","Invalid UserName / Password")
    else :
        messagebox.showinfo("Welcome",f"Welcome")
        
        
f1=Button(b,text="Login",fg="red",bg="white",command=check)
f1.place(x=450,y=200)


def PADI():
    f3=Frame(bg="skyblue")
    f3.place(x=0,y=0,width=850,height=500)
    p1=Label(f3,text="OFFLINE COURSES",bg="skyblue",font=("latin",10,"bold"))
    p1.pack()
    c1=Label(f3,text="C                      :   Rs=5,000/-  \n C++                  :   Rs=9,200/-   \n Java                :   Rs=9,500/- \n Java Script      :   Rs=12,500/-\n .Net               :   Rs=10,500/- \n Advanced Java   :   Rs=12,500/-   \n Core Java           :   Rs=12,000/-   \n HTML               :   Rs=3,000/-   \n Python              :   Rs=15,600/-   \n Django              :   Rs=16,600/-   \n",bg="skyblue",font=("latin",10))
    c1.pack()

    
    p2=Label(f3,text="ONLINE COURSES",bg="skyblue",font=("latin",10,"bold"))
    p2.pack()
    c2=Label(f3,text="Software Testing :  Rs=23,000/- \n Full Stack Development : Rs=24,000/- \n Webdesigning : Rs=13,500",bg="skyblue",font=("latin",10))
    c2.pack()
    b7=Button(f3,text="Billing",bg="pink",command=Bill_details)
    b7.pack()
    
    b6=Button(f3,text="Back",bg="pink",command=Login)
    b6.pack()



def Ambattur():
    f3=Frame(bg="moccasin")
    f3.place(x=0,y=0,width=850,height=500)
    p1=Label(f3,text="OFFLINE COURSES",bg="moccasin",font=("latin",10,"bold"))
    p1.pack()
    c1=Label(f3,text="C                      :   Rs=5,000/-  \n C++                  :   Rs=9,200/-   \n Java                :   Rs=9,500/- \n Java Script      :   Rs=12,500/-\n .Net               :   Rs=10,500/- \n Advanced Java   :   Rs=12,500/-   \n Core Java           :   Rs=12,000/-   \n HTML               :   Rs=3,000/-   \n Python              :   Rs=15,600/-   \n Django              :   Rs=16,600/-   \n",bg="moccasin",font=("latin",10))
    c1.pack()

    
    p2=Label(f3,text="ONLINE COURSES",bg="moccasin",font=("latin",10,"bold"))
    p2.pack()
    c2=Label(f3,text="Software Testing :  Rs=23,000/- \n Full Stack Development : Rs=24,000/- \n Webdesigning : Rs=13,500",bg="moccasin",font=("latin",10))
    c2.pack()
    b7=Button(f3,text="Billing",bg="pink",command=Bill_details)
    b7.pack()
    b6=Button(f3,text="Back",bg="pink",command=Login)
    b6.pack()


def Avadi():
    f3=Frame(bg="bisque")
    f3.place(x=0,y=0,width=850,height=500)
    p1=Label(f3,text="OFFLINE COURSES",bg="bisque",font=("latin",10,"bold"))
    p1.pack()
    c1=Label(f3,text="C                      :   Rs=5,000/-  \n C++                  :   Rs=9,200/-   \n Java                :   Rs=9,500/- \n Java Script      :   Rs=12,500/-\n .Net               :   Rs=10,500/- \n Advanced Java   :   Rs=12,500/-   \n Core Java           :   Rs=12,000/-   \n HTML               :   Rs=3,000/-   \n Python              :   Rs=15,600/-   \n Django              :   Rs=16,600/-   \n",bg="bisque",font=("latin",10))
    c1.pack()

    
    p2=Label(f3,text="ONLINE COURSES",bg="bisque",font=("latin",10,"bold"))
    p2.pack()
    c2=Label(f3,text="Software Testing :  Rs=23,000/- \n Full Stack Development : Rs=24,000/- \n Webdesigning : Rs=13,500",bg="bisque",font=("latin",10))
    c2.pack()
    b7=Button(f3,text="Billing",bg="pink",command=Bill_details)
    b7.pack()
    b6=Button(f3,text="Back",bg="pink",command=Login)
    b6.pack()

def Porur():
    f3=Frame(bg="lavender")
    f3.place(x=0,y=0,width=850,height=500)
    p1=Label(f3,text="OFFLINE COURSES",bg="lavender",font=("latin",10,"bold"))
    p1.pack()
    c1=Label(f3,text="C                      :   Rs=5,000/-  \n C++                  :   Rs=9,200/-   \n Java                :   Rs=9,500/- \n Java Script      :   Rs=12,500/-\n .Net               :   Rs=10,500/- \n Advanced Java   :   Rs=12,500/-   \n Core Java           :   Rs=12,000/-   \n HTML               :   Rs=3,000/-   \n Python              :   Rs=15,600/-   \n Django              :   Rs=16,600/-   \n",bg="lavender",font=("latin",10))
    c1.pack()

    
    p2=Label(f3,text="ONLINE COURSES",bg="lavender",font=("latin",10,"bold"))
    p2.pack()
    c2=Label(f3,text="Software Testing :  Rs=23,000/- \n Full Stack Development : Rs=24,000/- \n Webdesigning : Rs=13,500",bg="lavender",font=("latin",10))
    c2.pack()
    b7=Button(f3,text="Billing",bg="pink",command=Bill_details)
    b7.pack()
    b6=Button(f3,text="Back",bg="pink",command=Login)
    b6.pack("500x350")





    
def Bill_details():
    f4=Frame(bg="grey")
    f4.place(x=0,y=0,width=850,height=500)
    s1=Label(f4,text="Student_Id")
    s1.place(x=50,y=25)
    s2=Label(f4,text="")
    
