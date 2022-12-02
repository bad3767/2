'''
# palenrome
x=str(input("enter the string"))
if (x==x [::-1]):
    print("string is palenroome")
else:
    print("string is not a palenroome")
#example

my_str= "aIbohPhoBiA"
my_str = my_str.casefold()
rev_str=reversed(my_str)
if list(my_str)==list(rev_str):
    print("it is palenrome")
else :
    print ("its not a palindrome")

#matrics addtion
X = [[12, 7, 3], [4, 5, 6], [7, 8, 9]]
Y = [[5, 8, 1], [6, 7, 3], [4, 5, 9]]
result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# iterate through rows
for i in range(len(X)):
    # iterate through columns
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]

for r in result:
    print(r)

#matrix multiplication

x=[[12,7,3],[4,5,6],[7,8,9]]
y=[[5,8,1,2],[6,7,3,0],[4,5,9,1]]
result=[[0,0,0,0],[0,0,0,0],[0,0,0,0]]
for i in range (len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):\
            result[i][j]+=x[i][k]*y[k][j]
for r in result:
    print(r)


#punctuation

pun="!@#$%^&*(()_+<>?/.,';/*-+"
my_str="h%^&*ello !,.;'wo$%^&rld"
no_punct=""
for char in my_str:
    if char not in pun:
        no_punct = no_punct + char
print(no_punct)





#sort words

my_str ="Hello this is an Example with cased letters"
words=my_str.split()
words.sort()
print("the sorted words are:")
for word in words:
    print(word)
    
#example

# change this value for a different result
my_str = "Hello this Is an Example With cased letters"

# uncomment to take input from the user
#my_str = input("Enter a string: ")

# breakdown the string into a list of words
words = my_str.split()

# sort the list
words.sort()

# display the sorted words

print("The sorted words are:")
for word in words:
   print(word)
   '''
vo_e="aeiou"
string=input("enter the letter")
vo_s=""
for i in string:
    if i in vo_e:
        vo_s+=i
print("vowels in input :",vo_s)
vo_s=list(vo_s[::-1])
vowels_replaced=""
for i in string:
    if i not in vo_e:
        vowels_replaced+=i
    else:
        vowels_replaced+=vo_s[0]
        vo_s.pop(0)
        print(vowels_replaced)

