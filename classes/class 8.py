# polymorphism

#function overloading
class A():
    def add (self,a,b):
        self.a=a
        self.b=b
        return self.a+self.b
class B(A):
    def add(self, a,b,c):
        self.a=a
        self.b=b
        self.c =c
        return self.a+self.b+self.c
ab=A()
print(ab.add(2,5))
ba=B()
print(ba.add (2,5,10))

# function of overriding
class A():
    def eat (self):
        print("eating from A")
class B(A):
    def eat (self):
        A.eat(self)
        print ("eating from B")
ab=B()
ab.eat()
