# Write a Python program to find the highest 3 values in a dictionary.

d1={1:8,2:12,3:3,4:4,5:5,6:6,7:7}
print(type(d1))
a=[]
for i,j in d1.items():
    a.append(j)

a.sort()
print(a)
print(a[-1:-3])

