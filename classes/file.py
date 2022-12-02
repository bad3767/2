n=1
for i in range (n):
    studentname=str(input("enter your name :"))
    tamil=int(input("enter tamil marks:"))
    english=int(input("enter english mark:"))
    maths =int(input("enter maths mark:"))
    science=int(input("enter science mark:"))
    social=int (input("enter social marks:"))
    total=(tamil+english+maths+science+social)
    print (total)

    
    z="\n studentname:"+str(studentname)+"\n tamil:"+str(tamil)+"\n english:"+str(english)+"\n maths:"+str(maths)+"\n science:"+str(science)+"\n social:"+str(social)+"\ntotal:"+str(total)+"\n \n "


    a=open("C:\\Users\\Magesh\\Desktop\\python\\marksheet.txt","a")
    a.write(z)
    a.close()
    print ("file created")
