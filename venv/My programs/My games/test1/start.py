#Write a function called show_stars(rows). If rows is 5, it should print the following:
#       *
#      * *
#     * * *
#    * * * *
#   * * * * *

no=input("Enter a number: ")
i=0
j=0
while j<= int(no):
    while i<=int(no):
        print("*",end=" ")
        i +=1
    j +=1
    print("\n")



