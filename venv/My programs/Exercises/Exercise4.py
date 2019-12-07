#Write a Python program to print a long text, convert the string to a list and print all the words and their frequencies.
#text = input("Enter long text")
#a=text.split()
#print(a)
#wordcount=[]
#count=0
#for i in range(len(a)):
#    for j in a:
#        if a[i] == j:
#            count +=1
#    print(a[i] + " times " + str(count))
#    wordcount.append(count)
#    count =0
#print(a + wordcount)


text = input("Enter long text")
a=text.split()
for a in text:
    a.count(a)



