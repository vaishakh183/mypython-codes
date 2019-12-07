#Write a Python program to map two lists into a dictionary.

l1=[1,2,3]
l2=[4,5,6]
d1=dict()
key=0
for i in (l1,l2):
    d1[key]=i
    key=key+1
print(d1)