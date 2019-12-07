#Decorators change the behavior of a function in run time.
#make first parameter is always grater than second with out chaging the first function.

def div(a,b):
    print(a/b)

def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner()


div=smart_div(div)
div(2,4)