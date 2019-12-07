string = input("Enter a word")
#print(len(string))

a=0
for b in string:
    a +=1
print(a)

#-----------------

#program to check alphabet

word = "qaz123wsx"

for i in word:
    if i.isalpha():
        print(i)
