'''
def add():
    a = int(input("Enter a: "))
    b= int(input("Enter b: "))
    return a+b
print(add())
print(add())
print(add())
print(add())
# recursive

x=int(input("Enter x:"))
def fact(x):
    if x==1:
        return 1
    else:
        return x*fact(x-1)
print (fact(x))
    # lambda
a = lambda x,y,z : x*y*z
print(a(3,6,5))


a = [11,12,13,14,15,16,17,18,19,20]

s = list(filter(lambda x:x%2==1,a))
print(s)
d = list(map(lambda k : k%2==0,a))
print(d)


a=lambda x,y,z,w : (x*y-z)/w
print(a(5,6,10,5))

a=[1,2,3,4,5,6,7,8,9,10]
b=list(filter(lambda c: c%2==1,a))
print("odd numbers",b)

d= list (map(lambda x:x*2,a))
print (d)

x=int(input ("enter x:"))
def fact(x):
    if x==1:
        return 1
    else :
        return x*fact (x-1)
print (fact(x))

a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
b=list(filter(lambda c: c%3==0,a))
print(b)




arr = [-3,55,2,45,0,66,-1]
for i in range (len(arr)):
    for j in range (i+1,len(arr)):
        if arr [i]> arr[j]:
            arr[i],arr[j]=arr[j],arr[i]
print(arr)







'''







