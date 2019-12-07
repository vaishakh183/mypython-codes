
def fibonacci(a):
    for i in range(1,int(a)):
        l1.append(l1[i]+l1[i-1])

l1=[0,1]
a=input("Enter a number")
fibonacci(a)
print(l1)