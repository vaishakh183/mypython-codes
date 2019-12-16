#Using OOP in Python, we can restrict access to methods and variables. This prevent data from direct modification which is called encapsulation.
# In Python, we denote private attribute using underscore as prefix i.e single “ _ “ or double “ __“.

class A:
    def __init__(self):
        self.__name="vaishakh"

    def callname(self):
        print(self.__name)

    def changename(self,name):
        self.__name=name

obj1=A()
obj1.callname()
obj1.__name="rinsh"
obj1.callname()
obj1.changename("rinsha")
obj1.callname()