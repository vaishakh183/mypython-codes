name = ["vaishakh", "rinsha", "kuttan", "pommi"]
index =1
for i in name:
    print(index, i)
    index=index + 1

#-----------------

name = ["vaishakh", "rinsha", "kuttan", "pommi"]
others = ["batman", "superman","deadpool", "spiderman"]

for we,other in zip(name,others):
    print(f'{we}  "is"  {other}')





