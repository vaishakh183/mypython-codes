from array import *
arr1=array('i',[1,2,3,6,4,9])

#print(arr1)
#print(arr1.buffer_info())
#print(arr1.typecode)
#arr1.reverse()
#print(arr1)
#print(arr1[2])

#for i in range(len(arr1)):
#    print(arr1[i])

#for j in arr1:
#    print(j)

#copy array
#newarr= array(arr1.typecode, (a for a in arr1))
#print(newarr)

add = input("How many values you want to array")

for k in range(int(add)):
    val=input("Enter value to array")
    arr1.append(int(val))

print(arr1)

search=input("Enter a value to search in array")
c=0
for l in arr1:
    if l == int(search):
        print("index is" + str(c))
    c+=1

search1=input("Enter a value to search in array")
print(arr1.index(search1))