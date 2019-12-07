a=[1,2,3,4]
b=[5,6]
a.extend(b)
print(a)
popped= a.pop()
print(a)
print("popped value is" + str(popped))
a.reverse()
print(a)

c=["Physics","MAths","Biology"]
c.sort(reverse=True)

print(c)

d=["Hi","vaishakh","test","Rinsha"]
sorted_value=sorted(d)
print(sorted_value)

print(d.index("test"))

#check a vaule in a list

print("Art" in d)

print("test" in d)
#get index and value, enumerate return two values
for i,j in enumerate(d):
    print(i,j)

#starting value will be 1
for i,j in enumerate(d,start=1):
    print(i,j)


