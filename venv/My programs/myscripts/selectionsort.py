#find min value from the list on every iteration and move to left.
#intially first value will be the min value. compare it with other values in list. if you found any min value lesser than minvalue , make this as new min value
#and comapre, after first iteration you will find min value , move it to index 0. make it as permanent. start next iteration from index pos 1 and do same.

def selection(l1):
    for i in range(len(l1)):
        minvalue=i
        for j in range(minvalue,len(l1)):
            if l1[j] < l1[minvalue]:
                minvalue=j
        temp=l1[minvalue]
        l1[minvalue]=l1[i]
        l1[i]=temp
    return l1



l1=[6,5,7,4,2]
print(selection(l1))