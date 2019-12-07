index=0
def linearsearch(l1,no):
    for i in l1:
        if int(no) == l1[i]:
            globals()['index']=i
            return True
    return False


l1=[1,2,3,4,5,6,7,8]
no=input("Enter a number")
if linearsearch(l1,no):
    print("Found at "+ str(index))
else:
    print("Not Found")




