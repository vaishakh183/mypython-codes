index=0
def linear_search(no):
    l1=[1,2,3,4,5,7,9,12,15,18]
    start=0
    while start < len(l1):
        if int(no) == l1[start]:
            globals()['index']=start
            return True
        start +=1
    return False


no=input("Enter a num")
if linear_search(no):
    print("Found at" + str(index))
else:
    print("Not found")
