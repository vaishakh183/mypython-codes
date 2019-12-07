##a.read will read file as intividual string and so allows relatively easy file-wide manipulations, such as a file-wide regex search or substitution.
#f.readline() reads a single line of the file, allowing the user to parse a single line without necessarily reading the entire file.
a=open("file.txt","r")
#print(a.readlines())
#print(a.read())

print(a.name)
print(a.mode)
for lines in a:
    print(lines)

a.close()

a=open("file.txt","a")
a.write("\n vaishakh")
a.close()

a=open("file.txt","r")
b=a.readlines()
for i in b:
    if i == "vaishakh":
        b.remove(i)

print(b)


#no need of closing files here. it does automatically for you. Its always recommened to do by this way.
with open("file.txt","r") as f:
    pass
print(f)


