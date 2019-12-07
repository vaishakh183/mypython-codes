#. Write a Python program to sort a dictionary by key.

d1={6: 10, 2: 20, 5: 30, 4: 40, 1: 50, 3: 60}
#l1=[]
#d2=dict()
#for i in d1:
#    l1.append(i)
#    l1.sort()

#for j in l1:
#    d2[j]=d1[j]

#print(d2)

for i in sorted(d1):
    print(i,d1[i])
