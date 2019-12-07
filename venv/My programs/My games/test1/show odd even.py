#Write a function called showNumbers that takes a parameter called limit.
# It should print all the numbers between 0 and limit with a label to identify the even and odd numbers. For example,
# if the limit is 3, it should print:
#    0 EVEN
#    1 ODD
#    2 EVEN
#    3 ODD

no=input("Enter a number")
for i in range(int(no)):
    if int(i) % 2 == 0:
        print(str(i) + "EVEN")
    elif int(i) % 2 == 1:
        print(str(i) + "ODD")

