num=input("enter numbers")
while len(num) >=1:
    b=num%10
    b=b+num

    num=int(num)//10
print(num)

