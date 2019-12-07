#Write a Python program to remove and print every third number from a list of numbers until the list becomes empty.
list1=[1,2,3,4,5,6,7,8,9,0,11,12]
def listfun(list1):
    i = 1
    for count in range(len(list1)):
        if i == 3:
            print(list1[count])
            i = 1
        print(list1)
        i += 1
        a=len(list1)
    return a
b = listfun(list1)
while b != 0:
    listfun(list1)