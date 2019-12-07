#recursion -- calling same function again and again on that function itself.


def fact(a):
    if int(a) == 1:
        return a
    return int(a) * fact(int(a)-1)


a=input("Enter a no")
print(fact(a))
