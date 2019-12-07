#with open("file.txt","r") as f:
#    content = f.readline()
#    print(content,end="")
#    content = f.readlines()
#    print(content)
#end="" will remove blank lines between lines


#with open("file.txt","r") as f:
#    for i in f.readlines():
#        print(i,end="")


#with open("file.txt","r") as f:
#    print(f.read(500))


with open("file.txt","r") as f:
    lenth = f.read(100)
    print(len(lenth))
    while len(lenth) > 0:
        print(lenth)
        lenth = f.read(100)



