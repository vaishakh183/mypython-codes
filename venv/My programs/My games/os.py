import os

print(dir(os))
print(os.getcwd())

#os.chdir()

#print(os.listdir())

#os.mkdir("test")
#os.remove("test")
#os.rename("test","test1")
print(os.stat("test1").st_uid)
print(os.stat("test1").st_atime)
print(os.stat("test1"))
#print(os.listdir())


#for i in os.walk(os.curdir):
#    print(i)

print(os.environ.get("HOME"))

print(os.path.basename("test1"))

print(os.path.dirname(os.getcwd()))

print(os.path.split(os.getcwd()))

print(os.path.exists("test1"))

print(os.path.isdir("test1"))
print(os.path.isfile("test1"))
print(os.path.splitext("os.py"))



print(dir(os))