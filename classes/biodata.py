from tkinter import *
from tkinter import messagebox
import pymysql
a=Tk()
a.title("bio data")
a.geometry("500x500")
a.config(bg="red")

s=StringVar()
i=IntVar()

l1=Label(a,text="biodata",fg="white",bg="black",font=("latin",20,"italic"))
l1.pack()
l2=Label(a,text="name")
l2.place(x=100,y=150)
l3=Entry(a)
l3.place(x=200,y=150)
l4=Label(a,text="father name")
l4.place(x=100,y=200)
l5=Entry(a)
l5.place(x=200,y=200)
l7=Label(a,text="gender")
l7.place(x=100,y=250)

def male():
    messagebox.showinfo("Alert","male is selected")
def female ():
    messagebox.showinfo("Alert","female is selected")
    
rb = Radiobutton(a,text="Male",variable=s,value="Male")
rb.place(x=200,y=250)

rb1 = Radiobutton(a,text="Female",variable=s,value="female" )
rb1.place(x=270,y=250)
    
ck = Checkbutton(a,text="Accept ur T & C",variable=i,onvalue=1,offvalue=0)
ck.place(x=150,y=300)

# To collecting the answer of entry
def clt():
    a1=l3.get()
    a2=l5.get()
    a3=s.get()
    a4=i.get()
    print("Name :",a1)
    print("father Name:",a2)
    print("gender:",a3)
    if a4==1:
        h ="Accepted  T & C"
        print(h)
    else:
        h ="Not Accept T & C " 
        print(h)
    y="\n name :"+ a1+ "\n father_name:"+a2+ "\n gender:"+a3+ "\n status:"+h+ "\n\n\n"
    z=open("D:\\biodata.txt","a")
    z.write(y)
    z.close()
    
    
    db =pymysql.connect(host="localhost",user="root",password="aaaa",database="collage")
    c = db.cursor()
    sql =" insert into biodata (name,father_name,gender,status) values(%s,%s,%s,%s)"
    val=(a1,a2,a3,h)
    c.execute(sql,val)
    db.commit()
    db.close()
    print("data inserted")



    
l6=Button(a,text="Submit",command=clt)
l6.place(x=200,y=350)
def clt():
    a5=l6.get()
    print(a5)
a.mainloop()
