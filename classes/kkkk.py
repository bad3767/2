'''
ue=str(input("u"))
pe=str(input("p"))

if ((ue=="magesh@gmail.com") & (pe=="Magesh")):
    print("Login Successfully")
else:
    print("Login Invalid")
    if ue=="magesh@gmail.com" & pe!="Magesh":
        print("Check your Password")
    if ue!="magesh@gmail.com" & pe=="Magesh":
        print("Check Your UserName")

'''




from tkinter import *
root = Tk()
root.geometry("500x500")
root.title("Test")


def button_press():
    if one:
        x = 1
        display.configure(text=x)
    if two:
        x = 2
        display.configure(text=x)

display = LabelFrame(root, bg="white", width="462", height="60")
display.pack()

one = Button(root, text="1", width="10", height="10",command=button_press)
one.pack()


two = Button(root, text="2", width="15", height="5", command=button_press)
two.pack()

root.mainloop()
