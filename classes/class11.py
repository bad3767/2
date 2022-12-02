'''
try:
    a=int(input("enter a"))
    b=int(input("enter b"))
    print(a/b)
    print ("hello")
    c=[1,2,3]
    print(c[2])
except ZeroDivisionError:
    print("dont div by 0")
except ValueError:
    print("use integer value")
except:
    print ("error")
finally:
    print("undermaintance")
'''
try:
    age=int(input("agree:"))
    if age>=18:
        print("eligible to vote")
    else:   
        raise NameError
except NameError:
        print("not eligible")
