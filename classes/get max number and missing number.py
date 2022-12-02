a=[-3,2,0,1,8,9]

def max (nl):
    m=0
    for i in nl:
        if i > m:
            m=i
    print(m)
    return m

for i in range (max(a)):
    if i not in a:
        print (i)
        break
