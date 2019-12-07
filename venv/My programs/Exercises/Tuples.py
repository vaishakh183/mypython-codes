
#conver a list to string with "," comma seperated value

list1=["vaihsakh","rinsha","test","madapeedika"]

#first give how you want to seperate string then use .join method and pass list.
str=', '.join(list1)
print(str)
#str='- '.join(list1)
#print(str)

#conver back string to list
a=str.split(", ")
print(a)


#############################################

#Tuple is immutable


l1=[1,2,3,4]
l2=l1

print(l1)
print(l2)

l1[0]=6
print(l1)
print(l2)
#both lists will be same ,because of its mutability, if you dont want to change you can use Tuple insted.
#It behave almost same as list except its immutaability.
tuple1=(1,2,3,4)
tuple2=tuple1
print(tuple1)
print(tuple2)



