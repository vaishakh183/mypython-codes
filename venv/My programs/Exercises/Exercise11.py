# Write a Python script to sort (ascending and descending) a dictionary by value.
string="Understanding Write Behaviors of Storage Backends in Ceph Object Store"
a=string.split()
print(a)
count=0
dictionary = dict()
for i in a:
    dictionary[count] =i
    count +=1

print(dictionary)
print(dictionary[8])

#Write a Python script to concatenate following dictionaries to create a new one
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

newdict =dict()

for d in (dic1,dic2,dic3):
    newdict.update(d)

print(newdict)

#Write a Python script to check if a given key already exists in a dictionary

key =2

for j in dictionary:
    print(j)
    if j == key:
        print("key is available")
    else:
        print("key not available")