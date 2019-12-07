#1. Write a Python function that takes a sequence of numbers and determines if all the numbers are different from each other

i=0
a=[]
while i<=3:
    a.append(input("Enter a number"))
    i +=1
a.sort()

for no in range(len(a)-1):
#    print(str(no)+ "\n")
    if a[no] == a[no+1]:
        print(a[no])

