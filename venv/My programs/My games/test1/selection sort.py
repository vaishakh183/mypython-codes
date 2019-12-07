#go from start to end to find min value, you will assume the min value is first value. then you compare it with next value,
# if the next value is smaller then , you will assign min to this value. now min vlaue will become second one. You will contine this iteration and you will find the min
#value.

def selectionsort(l1):
    print("length of list is " + str(len(l1)))
    for i in range(len(l1)):
        minposition=i
        for j in range(i,len(l1)):
            if l1[j] < l1[minposition]:
                minposition=j
        temp=l1[i]
        l1[i]=l1[minposition]
        l1[minposition]=temp

l1=[45,23,576,78,4,5,2,1]
selectionsort(l1)
print(l1)
