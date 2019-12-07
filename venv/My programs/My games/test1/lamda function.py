#lamda functions are called anonymous functions. it does not require def keywork.
#you can pass any number of arguments ,but it should be one expression
#since b is a function ,we have to use ()

b=lambda a : a * a
print(b(4))

c=lambda c,d: c+d
print(c(5,6))

#filter list based in lambda function.
l1=[1,2,3,4,5,6,7,8]
a=list(filter(lambda n:n%2==0,l1))

print(a)

################################
#map function.. give any common operation..
#add 2 to all values in list
print(list(map(lambda a:a*2,l1)))

#################################

from functools import *
#reduce function to add all values of a list.
z=reduce(lambda x,y:x+y,l1)
print(z)

