available=5
def candy(no):
    i=0
    while i <=int(no):
        if i > available:
            break
        print("candy")
        i +=1
    print("Bye")


no=input("How many")
candy(no)

########----------

#print numbers till 100 and skip all numbers divisible by 3

for i in range(1,100):
    if i%3==0:
        continue
    print(i)

print("Bye")

