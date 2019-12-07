#values should be sorted.
#there will lower and upper bound.
#find middle by adding lower and upper divided by 2.
#if middle value is lower than searching value ,move the lower limit to middle value.
#if middle value is higher than searching vlaue ,move the upper limit to middle value.

def binary(l1,n):
    lower=0
    upper=len(l1)
    while lower <= upper:
        middle=(lower+upper)//2
        if int(n) == l1[middle]:
            globals() ["pos"]=middle
            return True
        else:
            if int(n)< l1[middle]:
                upper=middle
            else:
                lower=middle
    return False


l1=[1,2,3,4,5,6,7,8]
n=2
if binary(l1,n) is True:
    print("Found at " + str(pos))
else:
    print("Not Found")