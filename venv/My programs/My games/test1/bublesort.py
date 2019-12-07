#compare first and second number and swap highre number to right.

def bublesort(l1):
    for i in range(len((l1))-1,0,-1):
        for j in range(i):
            if l1[j] > l1[j+1]:
                b=l1[j]
                l1[j]=l1[j+1]
                l1[j+1]=b

l1=[3,1,5,7,6,4,2,1]
bublesort(l1)
print(l1)