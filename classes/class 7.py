
class book():
    def __init__ (self,tamil,english,maths):
        self.a= tamil
        self.b=english
        self.c=maths
        print(self.a,self.b,self.c)
    def read (self):
        print("reading")
    def write (self):
        print ("writing")
k=book("the tamil book is our mother tongue","reading ","writing")
k.read()
k.write()

class teachers(book):
    def __init__ (self,tamil,english,maths):
        self.a= tamil
        self.b=english
        self.c=maths
        print(self.a,self.b,self.c)
    def read (self):
        print("reading")
    def write (self):
        print ("writing")
k=book("the teacher will teach tamil to","reading ","writing")
k.read()
k.write()
# single
class A():
    def run (self):
        print ("runing")
class B (A):
    def eat (self):
        print("eating")

obj =B()
obj.run()
obj.eat()

#multiple
class a():
    def run(self):
        print("running")
class b():
    def eat (self):
        print("eating")
class c(a,b):
    def work (self):
        print ("working")

obj =c()
obj.run()
obj.eat()
obj.work()

#multilevel

class a():
    def run(self):
        print("running")
class b(a):
    def eat (self):
        print("eating")
class c(b):
    def work (self):
        print ("working")

obj =c()
obj.run()
obj.eat()
obj.work()



#hybrid

class a():
    def run(self):
        print("running")
class b(a):
    def eat (self):
        print("eating")
class c(a):
    def work (self):
        print ("working")

obj1 =c()
obj2 =b()
obj1.run()
obj2.eat()
obj2.run()
obj1.work()


#hierarchical

class a():
    def run(self):
        print("running")
class b(a):
    def eat (self):
        print("eating")
class c(a):
    def work (self):
        print ("working")
class d(c):
    def play(self):
        print ("playing")

obj = d()
obj1 = c()
obj2 = b()
obj.run()
obj2.eat()
obj1.work()
obj.play()

# single inherarchical

class A():
    def vote (self):
        age=int(input("enter your age:"))
        if age>=18:
            print ("eligible to vote")
        else:
            print("not eligible to vote")
class B(A):
    def login (self):
        username =str(input("enter your user name:"))
        password =str(input("enter your password:"))
        if username=="Magesh" and password=="1234":
            print ("login successful")
        else:
            print ("invalid username or password")

obj = B()
obj.vote()
obj.login()



class A():
    def vote (self):
        age=int(input("enter your age:"))
        if age>=18:
            print ("eligible to vote")
        else:
            print("not eligible to vote")
class B(A):
    def login (self):
        username =str(input("enter your user name:"))
        password =str(input("enter your password:"))
        if username=="Magesh" and password=="magesh@123":
            print ("login successful")
        else:
            print ("login invalid ")
            if username=="Magesh" and password!="magesh@123":
                print ("check the password")
            if username!="Magesh" and password=="magesh@123":
                print ("check the username")

obj = B()
obj.vote()
obj.login()


















