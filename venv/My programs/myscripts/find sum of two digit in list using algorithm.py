#find two digits to add and sum should come 10 in best ways.
#sum =10
#1. Using Linear search.

#def search(l1):
#    sum=10
#    globals()["d1"]=dict()
#    index=0
#    for i in range(len(l1)):
#        for j in range(i,len(l1)):
#            if l1[i]+l1[j]==10:
#                if i != j:
#                    print(l1[i],l1[j])

#l1=[1,2,3,4,5,6,7,8,9,10,11]
#print(search(l1))
#search(l1)

#2. Using Binary search.
def binary(l2):
    sum=5
    lower=0
    upper=len(l2)
    l3=[]
    mydict=dict()
    length=len(l2)//2
    for i in range(length):
        print(i)
        no = sum - l2[i]
        while lower <=upper:
            middle=(lower+upper)//2
            if l2[middle] == no:
#                print(l2[middle],l2[i])
                mydict[l2[i]]=l2[middle]
                return mydict
            else:
                if no < middle:
                    upper=middle
                else:
                    lower=middle

l2=[1,2,3,4,5,6,7,8,9,10,11]
print(binary(l2))