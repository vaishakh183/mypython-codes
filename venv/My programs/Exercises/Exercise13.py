#Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
#Sample Dictionary ( n = 5) :
#Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


length=input("Enter lenth of dictionary")
i=1
dict1= dict()
while i<=int(length):
    value=i*i
    dict1[i]=value
    i +=1

print(dict1)

