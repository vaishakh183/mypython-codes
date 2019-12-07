#comapre 1st and 2nd values ,if first value is grater than second ,swap it.
#now compare 2nd and 3rd values,do same..and continue..you will get largest value at the end. continue the loop.


def bubble(l1):
    for j in range(len(l1)):
        for i in range(1,len(l1)):
            if l1[i-1] > l1[i]:
                temp=l1[i]
                l1[i] = l1[i-1]
                l1[i-1]=temp
    return l1

l1=[6,4,7,2,9,5,1,67]
print(bubble(l1))

