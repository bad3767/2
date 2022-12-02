a=[5,6,7,8,3]
print(type(a))
a.sort(reverse=True)
print(a)
a.append(8)
print(a)
a.append([5,3,2,1])
print(a)

b=a.copy()
print(b)
print(a.count(8))
print(a.index(8))
a.extend([1,2,3])
print(a)
a.insert(4,33)
print(a)
a.pop(4)
print(a)
a.remove(8)
print(a)
a.reverse()
print(a)

a.clear()
print(a)

'''
#tuple



a=(1,2,3,4,5,6,7,8,9,8,7,8)
print(type(a))

print(a.count(8))
print(a.index(5))



#set

a={1,2,3,4,5,6,7}
b={5,6,7,11,15,44}
print(type(a))
a.add(11)
print (a)
print (a.union(b))
a.pop()
print(a)
print(a.intersection(b))
print(a.issubset(b))




#dictionary

a={'a':"name",2:"magesh",3:"jnjz"}
print(type(a))
print(a.keys())
print (a.values())
print(a.items())
print(a['a'])
a[3]="abc"
print(a.items())

'''
