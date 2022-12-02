'''
#while
i=0
while(i<=10):
   i+=1
   print(i)

#continue
    
   i+=1
   if i==5:
        continue
    print(i)
#break 
i=0
while(i<=10):
    if i==5:
        break
    print(i)
    i+=1

    
    #function
def add(a,b):
   # a=5
   # b=8
    print(a/b)
add(5,8)
add(5,5)
add(5,13)
add(5,48)
   

n=20
i=0
while(i<=n):
    print(i)
    i+=1

#function

#keywords
def greet (name="Arun",msg ="welcome"):
    print("Hello", name , msg)
greet ()


#default
def greet (name, msg="good morning",subject="time"):
    print("hello",name,msg,subject)
greet("Arun","welcome","time")
greet ("Arun")



#arbitary
def greet (*names):
    for i in names:
        print (i)
greet ("aaa","bbb","ccc")
greet ("aaa","bbb","ccc")



'''







    

