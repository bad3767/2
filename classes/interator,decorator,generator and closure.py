#iterator sequence order,*iter(),*next()
a=[1,5,6,8,7,2,6]
z=iter(a)
print(next(z))
print(next(z))
print(next(z))
print(next(z))
print(next(z))
print(next(z))
print(next(z))


#generator , yeild()
def my_gen():
    n=1
    print('hello everyone')
    yield n

    n+=1
    print('hello')
    yield n

    n+=1
    print('happy')
    yield n

    n+=1
    print('end')
    yield n

for item in my_gen():
    print(item)

# closure and decorator
def a(id):
    
    def admin_view():
        print (id)
        def b(fees):
            return fees
        return b(77)
    def stu_view():
        print (id)
    print( admin_view())
a(113218114318)





#generator
def genrator():
    def gen():
        a='shd'
        yield a
    def end():
        a="BYE"
        b=iter(a)
        print(next(b))
        print(next(b))
        print(next(b))
    return end
a=genrator()
a()
