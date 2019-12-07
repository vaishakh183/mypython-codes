a=10
b=20
c=30
#def fun():
#    global a
#    print(a)

#print(a)
#fun()

#get global variable with same name without chaging value of local
def globalfun():
    a=15
    x=globals()['a']
    print(x)
    globals()['a']=50
    print(globals()['a'])

globalfun()