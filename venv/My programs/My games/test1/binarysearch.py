#List shound be sorted for doing binary search. add lower and upper index and divide by 2, thant will be middle index. if no is higher than value in lower index
# ,change lowerindex to midleindex
position=-1
def binarysearch(l1,no):
    lowerindex=0
    upperindex=len(l1)-1 #index start with 0

    while lowerindex <= upperindex:
        middleindex = (lowerindex + upperindex) // 2
        if l1[middleindex] == int(no):
            globals()['position']=middleindex
            return True
        else:
            if l1[middleindex] < int(no):
                lowerindex=middleindex+1
            else:
                upperindex=middleindex-1
    return False

l1=[10,20,30,40,50,60,70,80,90,100]
no=input("Enter a no to search")
if binarysearch(l1,no):
    print("Found at" + str(position))
else:
    print("Not Found")