'''no=int(input("enter no:"))
if no%2==0:
    print("magesh age is",no)
    print('even')
else:
    print ("odd")
'''
#login page
'''un=str(input("user name:"))
pw=str(input("password:"))
if un=="aaa" and pw=="a@1":
    print ("login successful")
else:
    print("invalid user")
'''

'''
mark=int(input("user input:"))
if mark==45:
    print("just pass")
elif (mark>=46) and (mark<=65):
    print("C grade")
elif (mark>=66)and(mark<=85):
    print("B grade")
elif (mark>=86)and(mark<=100):
    print("A grade")
elif (mark >100):
    print ("invalid")
else:
    print("fail")
'''


'''
#nested if
age = int(input("user age:"))
if age >=18:
    print("eligible")
    if (age>=18) and (age<=45):
        print ("junior citizen")
    else:
        print ("senior citizen")
else:
    print("not eligible")
    if (age>=1)and(age<=10):
        print("kids")
    elif (age<=0):
        print ("enter the valid age")
    else:
        print("adult")
'''
'''
no=int(input("user no:"))
if (no%2==0)and(no>=1)and (no<=6):
    print("aa")
elif (no%2==0) and (no>=7) and (no<=20):
    print ("bb")
elif (no%2==0)and(no>20):
    print("cc")
else:
        print ("dd")
'''
'''
for i in range (10):
    print(-i)

print (range(15))


stud=int(input("enter no of studs:"))
for i in range(stud):
    print("student",i+1)
    t=int(input("tamil marks:"))
    e=int(input("english marks:"))
    m=int(input("maths marks:"))
    tot=t+e+m
    print(tot)
    avg=tot/3
    print(avg)
'''


i=0
n=int(input("enter the valu"))
while (i<=n):
    print(i)
    i+=1









