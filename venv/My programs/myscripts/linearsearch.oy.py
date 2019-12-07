
def search(l1,n):
    global j
    j=-1
    for i in l1:
        j +=1
        if int(i) == int(n):
            return True
    return False

l1=[1,2,3,4,7,6,8,9,12]
n=12
#print(search(l1,n))
if search(l1,n) == True:
    print("Found at position " + str(j))
else:
    print("Not Found")