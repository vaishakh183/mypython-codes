#As we know, a child class inherits all the methods from the parent class. However, you will encounter situations where the method inherited from the
# parent class doesn’t quite fit into the child class. In such cases, you will have to re-implement method in the child class.
# This process is known as Method Overriding.
#If you have overridden a method in the child class, then the version of the method will be called based upon the type of the object used to call it.
# If a child class object is used to call an overridden method then the child class version of the method is called. On the other hand, if parent class object
# is used to call an overridden method, then the parent class version of the method is called.

class A:
    def explore(self):
        print("from class A")

class B:
    def explore(self):
        print("from class B")

ob1=A()
ob2=B()
ob1.explore()
ob2.explore()


#If for some reason you still want to access the overridden method of the parent class in the child class, you can call it using the super() function.

class C:
    def explore(self):
        print("from class C")

class D(C):
    def explore(self):
        super().explore()
        print("from class D")

ob3=C()
ob4=D()

ob4.explore()
