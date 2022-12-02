
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
b.resizable(False,False)

img=ImageTk.PhotoImage(Image.open("C:\\Users\\Magesh\\AppData\\Local\\Programs\\Python\\Python310\\3.jpg"))
img1=Label(b,image=img)
img1.pack()

    
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
        messagebox.showinfo("welcome","welcome")
        f1=Frame(bg="CYAN")
        f1.place(x=0,y=0,width=850,height=500)

        L1=Label(f1,text="SELECT ANYONE CENTER",fg="BLACK",bg="CYAN",font=("times new roman",30,"italic"))
        L1.place(x=200,y=50)

        b2=Button(f1,text="Avadi",font=("times new roman",15),command=Avadi)
        b2.place(x=250,y=150)
    
        b3=Button(f1,text="Padi",font=("times new roman",15),command=PADI)
        b3.place(x=500,y=150)
    
        b4=Button(f1,text="Ambattur",font=("times new roman",15),command=Ambattur)
        b4.place(x=250,y=200)
    
        b5=Button(f1,text="Porur",font=("times new roman",15),command=Porur)
        b5.place(x=500,y=200)

        e1=Button(f1,text="Exit",font=("times new roman",15),command=exit)
        e1.place(x=390,y=250)

    
        
        
        
                
        
        
f1=Button(b,text="Login",fg="red",bg="white",command=check)
f1.place(x=450,y=200)



def PADI():
    f3=Frame(bg="skyblue")
    f3.place(x=0,y=0,width=850,height=500)
    p1=Label(f3,text="OFFLINE COURSES",bg="skyblue",font=("latin",10,"bold"))
    p1.place(x=390,y=20)
    c1=Label(f3,text="C\n C++\n Java\n Java Script\n .Net\n Advanced Java\n Core Java\n HTML\n Python\n Django\n",bg="skyblue",font=("latin",10))
    c1.place(x=350,y=50)
    c11=Label(f3,text=" :\n:\n:\n:\n:\n:\n:\n:\n:\n:",bg="skyblue",font=("latin",10))
    c11.place(x=450,y=50)
    c12=Label(f3,text="Rs= 5,000/-\nRs= 9,200/-\nRs= 9,500/-\nRs=12,500/-\nRs=10,500/-\nRs=12,500/-\nRs=12,000/-\nRs= 3,000/-\nRs=15,600/-\nRs=16,600/-",bg="skyblue",font=("latin",10))
    c12.place(x=460,y=50)
    
    p2=Label(f3,text="ONLINE COURSES",bg="skyblue",font=("latin",10,"bold"))
    p2.place(x=390,y=240)
    c2=Label(f3,text="Software Testing \n Rs = 23,000/-\n\n Full Stack Development \n Rs = 24,000/- \n\n Web Designing\n Rs = 13,500/-",bg="skyblue",font=("latin",10))
    c2.place(x=370,y=270)
    b7=Button(f3,text="Billing",bg="pink",command=live_wire)
    b7.place(x=427,y=420)
    
    b6=Button(f3,text="Back",bg="pink",command=check)
    b6.place(x=430,y=450)

def live_wire():
    f8=Frame()
    f8.place(x=0,y=0,width=850,height=500)
    q0=Label(f8,text="Live Wire\nBill Details",font=("times new roman",20,"italic","bold"))
    q0.place(x=450,y=25)
    q1=Label(f8,text="Student_Id")
    q1.place(x=350,y=100)
    q2=Entry(f8)
    q2.place(x=450,y=100)
    q3=Label(f8,text="Student_Name")
    q3.place(x=350,y=150)
    q4=Entry(f8)
    q4.place(x=450,y=150)
    q5=Label(f8,text="Course")
    q5.place(x=350,y=200)
    q6=Entry(f8)
    q6.place(x=450,y=200)
    q7=Label(f8,text="Amount")
    q7.place(x=350,y=250)
    q8=Entry(f8)
    q8.place(x=450,y=250)
    q9=Label(f8,text="Bill_Date")
    q9.place(x=350,y=300)
    q10=Entry(f8)
    q10.place(x=450,y=300)

    def notes():
        z0="PADI"
        z1=q2.get()
        z2=q4.get()
        z3=q6.get()
        z4=q8.get()
        z5=q10.get()
        y="\n branch :"+ z0+"\n Student_Id :"+ z1+ "\n Student_Name:"+z2+ "\n Course:"+z3+ "\n Amount:"+z4+ "\n Bill_Date :"+z5+ "\n\n\n"
        z=open("D:\\project_python\\Padi.txt","a")
        z.write(y)
        z.close()
        #database
        db =pymysql.connect(host="localhost",user="root",password="aaaa",database="Livewire")
        c = db.cursor()
        sql =" insert into Padi (Student_Id,Student_Name,Course,Amount,Bill_Date) values(%s,%s,%s,%s,%s)"
        val=(z1,z2,z3,z4,z5)
        c.execute(sql,val)
        db.commit()
        db.close()
        print("data inserted")



    q11=Button(f8,text="Save",command=notes)
    q11.place(x=500,y=335)
    
    q12=Button(f8,text="Print")
    q12.place(x=500,y=365)
    
    b7=Button(f8,text="back",command=PADI)
    b7.place(x=500,y=400)




def Ambattur():
    f3=Frame(bg="moccasin")
    f3.place(x=0,y=0,width=850,height=500)
    p1=Label(f3,text="OFFLINE COURSES",bg="skyblue",font=("latin",10,"bold"))
    p1.place(x=390,y=20)
    c1=Label(f3,text="C\n C++\n Java\n Java Script\n .Net\n Advanced Java\n Core Java\n HTML\n Python\n Django\n",bg="moccasin",font=("latin",10))
    c1.place(x=350,y=50)
    c11=Label(f3,text=" :\n:\n:\n:\n:\n:\n:\n:\n:\n:",bg="moccasin",font=("latin",10))
    c11.place(x=450,y=50)
    c12=Label(f3,text="Rs= 5,000/-\nRs= 9,200/-\nRs= 9,500/-\nRs=12,500/-\nRs=10,500/-\nRs=12,500/-\nRs=12,000/-\nRs= 3,000/-\nRs=15,600/-\nRs=16,600/-",bg="moccasin",font=("latin",10))
    c12.place(x=460,y=50)
    
    p2=Label(f3,text="ONLINE COURSES",bg="moccasin",font=("latin",10,"bold"))
    p2.place(x=390,y=240)
    c2=Label(f3,text="Software Testing \n Rs = 23,000/-\n\n Full Stack Development \n Rs = 24,000/- \n\n Web Designing\n Rs = 13,500/-",bg="moccasin",font=("latin",10))
    c2.place(x=370,y=270)
    b7=Button(f3,text="Billing",bg="pink",command=live_wire)
    b7.place(x=427,y=420)
    
    b6=Button(f3,text="Back",bg="pink",command=check)
    b6.place(x=430,y=450)



def live_wire():
    f8=Frame()
    f8.place(x=0,y=0,width=850,height=500)
    q0=Label(f8,text="Live Wire\nBill Details",font=("times new roman",20,"italic","bold"))
    q0.place(x=450,y=25)
    q1=Label(f8,text="Student_Id")
    q1.place(x=350,y=100)
    q2=Entry(f8)
    q2.place(x=450,y=100)
    q3=Label(f8,text="Student_Name")
    q3.place(x=350,y=150)
    q4=Entry(f8)
    q4.place(x=450,y=150)
    q5=Label(f8,text="Course")
    q5.place(x=350,y=200)
    q6=Entry(f8)
    q6.place(x=450,y=200)
    q7=Label(f8,text="Amount")
    q7.place(x=350,y=250)
    q8=Entry(f8)
    q8.place(x=450,y=250)
    q9=Label(f8,text="Bill_Date")
    q9.place(x=350,y=300)
    q10=Entry(f8)
    q10.place(x=450,y=300)

    def notes():
        z0="Ambattur"
        z1=q2.get()
        z2=q4.get()
        z3=q6.get()
        z4=q8.get()
        z5=q10.get()
        y="\n branch :"+ z0+"\n Student_Id :"+ z1+ "\n Student_Name:"+z2+ "\n Course:"+z3+ "\n Amount:"+z4+ "\n Bill_Date :"+z5+ "\n\n\n"
        z=open("D:\\project_python\\Ambathur.txt","a")
        z.write(y)
        z.close()
        
        db =pymysql.connect(host="localhost",user="root",password="aaaa",database="Livewire")
        c = db.cursor()
        sql =" insert into Ambattur (Student_Id,Student_Name,Course,Amount,Bill_Date) values(%s,%s,%s,%s,%s)"
        val=(z1,z2,z3,z4,z5)
        c.execute(sql,val)
        db.commit()
        db.close()
        print("data inserted")

    q11=Button(f8,text="Save",command=notes)
    q11.place(x=500,y=335)
    q12=Button(f8,text="Print")
    q12.place(x=500,y=365)



    
    b7=Button(f8,text="back",command=Ambattur)
    b7.place(x=500,y=400)





def Avadi():
    f3=Frame(bg="bisque")
    f3.place(x=0,y=0,width=850,height=500)
    p1=Label(f3,text="OFFLINE COURSES",bg="bisque",font=("latin",10,"bold"))
    p1.place(x=390,y=20)
    c1=Label(f3,text="C\n C++\n Java\n Java Script\n .Net\n Advanced Java\n Core Java\n HTML\n Python\n Django\n",bg="bisque",font=("latin",10))
    c1.place(x=350,y=50)
    c11=Label(f3,text=" :\n:\n:\n:\n:\n:\n:\n:\n:\n:",bg="bisque",font=("latin",10))
    c11.place(x=450,y=50)
    c12=Label(f3,text="Rs= 5,000/-\nRs= 9,200/-\nRs= 9,500/-\nRs=12,500/-\nRs=10,500/-\nRs=12,500/-\nRs=12,000/-\nRs= 3,000/-\nRs=15,600/-\nRs=16,600/-",bg="bisque",font=("latin",10))
    c12.place(x=460,y=50)
    
    p2=Label(f3,text="ONLINE COURSES",bg="bisque",font=("latin",10,"bold"))
    p2.place(x=390,y=240)
    c2=Label(f3,text="Software Testing \n Rs = 23,000/-\n\n Full Stack Development \n Rs = 24,000/- \n\n Web Designing\n Rs = 13,500/-",bg="bisque",font=("latin",10))
    c2.place(x=370,y=270)
    b7=Button(f3,text="Billing",bg="pink",command=live_wire)
    b7.place(x=427,y=420)
    
    b6=Button(f3,text="Back",bg="pink",command=check)
    b6.place(x=430,y=450)

    
    
def live_wire():
    f8=Frame()
    f8.place(x=0,y=0,width=850,height=500)
    q0=Label(f8,text="Live Wire\nBill Details",font=("times new roman",20,"italic","bold"))
    q0.place(x=450,y=25)
    q1=Label(f8,text="Student_Id")
    q1.place(x=350,y=100)
    q2=Entry(f8)
    q2.place(x=450,y=100)
    q3=Label(f8,text="Student_Name")
    q3.place(x=350,y=150)
    q4=Entry(f8)
    q4.place(x=450,y=150)
    q5=Label(f8,text="Course")
    q5.place(x=350,y=200)
    q6=Entry(f8)
    q6.place(x=450,y=200)
    q7=Label(f8,text="Amount")
    q7.place(x=350,y=250)
    q8=Entry(f8)
    q8.place(x=450,y=250)
    q9=Label(f8,text="Bill_Date")
    q9.place(x=350,y=300)
    q10=Entry(f8)
    q10.place(x=450,y=300)

    def notes():
        zo="Avadi"
        z1=q2.get()
        z2=q4.get()
        z3=q6.get()
        z4=q8.get()
        z5=q10.get()
        y="\n branch :"+ z0+"\n Student_Id :"+ z1+ "\n Student_Name:"+z2+ "\n Course:"+z3+ "\n Amount:"+z4+ "\n Bill_Date :"+z5+ "\n\n\n"
        z=open("D:\\project_python\\Avadi.txt","a")
        z.write(y)
        z.close()
        
        db =pymysql.connect(host="localhost",user="root",password="aaaa",database="Livewire")
        c = db.cursor()
        sql =" insert into Avadi (Student_Id,Student_Name,Course,Amount,Bill_Date) values(%s,%s,%s,%s,%s)"
        val=(z1,z2,z3,z4,z5)
        c.execute(sql,val)
        db.commit()
        db.close()
        print("data inserted")

    q11=Button(f8,text="Save",command=notes)
    q11.place(x=500,y=335)
    q12=Button(f8,text="Print")
    q12.place(x=500,y=365)



    
    b7=Button(f8,text="back",command=Avadi)
    b7.place(x=500,y=400)





def Porur():
    f3=Frame(bg="lavender")
    f3.place(x=0,y=0,width=850,height=500)
    p1=Label(f3,text="OFFLINE COURSES",bg="lavender",font=("latin",10,"bold"))
    p1.place(x=390,y=20)
    c1=Label(f3,text="C\n C++\n Java\n Java Script\n .Net\n Advanced Java\n Core Java\n HTML\n Python\n Django\n",bg="lavender",font=("latin",10))
    c1.place(x=350,y=50)
    c11=Label(f3,text=" :\n:\n:\n:\n:\n:\n:\n:\n:\n:",bg="lavender",font=("latin",10))
    c11.place(x=450,y=50)
    c12=Label(f3,text="Rs= 5,000/-\nRs= 9,200/-\nRs= 9,500/-\nRs=12,500/-\nRs=10,500/-\nRs=12,500/-\nRs=12,000/-\nRs= 3,000/-\nRs=15,600/-\nRs=16,600/-",bg="lavender",font=("latin",10))
    c12.place(x=460,y=50)
    
    p2=Label(f3,text="ONLINE COURSES",bg="lavender",font=("latin",10,"bold"))
    p2.place(x=390,y=240)
    c2=Label(f3,text="Software Testing \n Rs = 23,000/-\n\n Full Stack Development \n Rs = 24,000/- \n\n Web Designing\n Rs = 13,500/-",bg="lavender",font=("latin",10))
    c2.place(x=370,y=270)
    b7=Button(f3,text="Billing",bg="pink",command=live_wire)
    b7.place(x=427,y=420)
    
    b6=Button(f3,text="Back",bg="pink",command=check)
    b6.place(x=430,y=450)


def live_wire():
    f8=Frame()
    f8.place(x=0,y=0,width=850,height=500)
    q0=Label(f8,text="Live Wire\nBill Details",font=("times new roman",20,"italic","bold"))
    q0.place(x=450,y=25)
    q1=Label(f8,text="Student_Id")
    q1.place(x=350,y=100)
    q2=Entry(f8)
    q2.place(x=450,y=100)
    q3=Label(f8,text="Student_Name")
    q3.place(x=350,y=150)
    q4=Entry(f8)
    q4.place(x=450,y=150)
    q5=Label(f8,text="Course")
    q5.place(x=350,y=200)
    q6=Entry(f8)
    q6.place(x=450,y=200)
    q7=Label(f8,text="Amount")
    q7.place(x=350,y=250)
    q8=Entry(f8)
    q8.place(x=450,y=250)
    q9=Label(f8,text="Bill_Date")
    q9.place(x=350,y=300)
    q10=Entry(f8)
    q10.place(x=450,y=300)

    def notes():
        z0="Porur"
        z1=q2.get()
        z2=q4.get()
        z3=q6.get()
        z4=q8.get()
        z5=q10.get()
        y="\n branch :"+ z0+ "\n Student_Id :"+ z1+ "\n Student_Name:"+z2+ "\n Course:"+z3+ "\n Amount:"+z4+ "\n Bill_Date :"+z5+ "\n\n\n"
        z=open("D:\\project_python\\Porur.txt","a")
        z.write(y)
        z.close()

        db =pymysql.connect(host="localhost",user="root",password="aaaa",database="Livewire")
        c = db.cursor()
        sql =" insert into Porur (Student_Id,Student_Name,Course,Amount,Bill_Date) values(%s,%s,%s,%s,%s)"
        val=(z1,z2,z3,z4,z5)
        c.execute(sql,val)
        db.commit()
        db.close()
        print("data inserted")
        

    
    q11=Button(f8,text="Save",command=notes)
    q11.place(x=500,y=335)


    
    q12=Button(f8,text="Print")
    q12.place(x=500,y=365)



    
    b7=Button(f8,text="back",command=Porur)
    b7.place(x=500,y=400)


