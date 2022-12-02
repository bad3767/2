
from tkinter import *
from tkinter import messagebox
import tkinter as ak
from PIL import ImageTk,Image
import os
import pymysql

b=ak.Tk()
b.title("Login_Form")
b.geometry("850x500")
b.config(bg="yellow")

img=ImageTk.PhotoImage(Image.open("C:\\Users\\Magesh\\AppData\\Local\\Programs\\Python\\Python310\\3.jpg"))
img1=Label(b,image=img)
img1.pack()

i1=Label (b,text="login_Form",fg="red",bg="yellow",font=("latin",20,"italic"))
i1.place(x=400,y=100)

def sign_in():
    
    a=ak.Toplevel()
    a.title("love_my_web")
    a.geometry("850x500")
    

    img2=ImageTk.PhotoImage(Image.open("C:\\Users\\Magesh\\AppData\\Local\\Programs\\Python\\Python310\\3.jpg"))
    img3=Label(a,image=img2)
    img3.pack()

    s=StringVar()
    n=IntVar()
        
    un=Label(a,text="User_Name",fg="yellow",bg="blue")
    un.place(x=300,y=100)
    ue=Entry(a)
    ue.place(x=450,y=100)

    pw=Label(a,text="Password",fg="yellow",bg="blue")
    pw.place(x=300,y=150)
    pe=Entry(a)
    pe.place(x=450,y=150)

    f1=Button(a,text="Forgot_Password",fg="red",bg="white")
    f1.place(x=450,y=200)



    p1 = Label(a,text=" ")
    p1.place(x=600,y=100)

    p2 = Label(a,text=" ")
    p2.place(x=600,y=150)

 


    def s1():
        ue1 =ue.get()
        pe1 =pe.get()
        
        print("User_Name : " ,ue1)
        print("Password  : " ,pe1)
        p1.config(text=ue1)
        p2.config(text=pe1)

        y="\n User_Name :"+ ue1+ "\n Password:"+pe1+ "\n\n\n"
        z=open("D:\\python notes database\\Login Page.txt","a")
        z.write(y)
        z.close()
        db =pymysql.connect(host="localhost",user="root",password="aaaa",database="LoginPage")
        c = db.cursor()
        sql =" insert into LoginPage (User_Name,Password) values(%s,%s)"
        val=(ue1,pe1)
        c.execute(sql,val)
        db.commit()
        db.close()
        print("data inserted")

    b1=Button(a,text="Login",command=s1)
    b1.place(x=450,y=250)

    a.mainloop()
    
    
    

a1=Button(b,text="sign_in",command=sign_in)
a1.place(x=425,y=200)

