#Find all occurrences of “USA” in given string ignoring the case.
word=input("enter word")
a=word.split()
count=0
for i in a:
    if i.lower() == "usa":
        count +=1
print("occurance of USA is" + str(count))

