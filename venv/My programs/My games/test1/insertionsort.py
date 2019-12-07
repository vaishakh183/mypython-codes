#take first element as sorted port and others are unsorted. compare sorted with unsorted. if unsorted element is lesser than sorted inserted to its position else leave as it is.
#.After inserted compare that with its previous element and so on.  #elemets will inserted on proper index.

def insertionsort(l1):
    for index in range(1,len(l1)):
        current_element=l1[index]
        pos=index
        while current_element < l1[pos -1] and pos > 0:
            l1[pos] = l1[pos-1]
            pos = pos-1
        l1[pos] = current_element

l1=[8,9,4,1,3,34,56,12,55]
insertionsort(l1)
print(l1)