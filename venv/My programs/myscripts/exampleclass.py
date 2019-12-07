class Employee:
    place="thalassery"    #---------> class variable , variable that common for all objects.
    def __init__(self,name,age):
        self.name=name    #---------> object variable
        self.age=age

    def details(self):
        print(self.age -2)

    def compare(self,emp2):     #these are instance method,so we pass self keyword
        if self.age == emp2.age:
            return True
        else:
            return False
    @classmethod
    def info(cls):         #----------->class method should pass cls variable as arg
        return cls.place

    @staticmethod          #----------->static method which has nothing to do with class or instance variables,so we dont pass anything.
    def add():
        return (5+5)



emp1=Employee("vaishakh",28)
emp2=Employee("Rinsha",28)

print(Employee.info())
print(Employee.add())
#Employee.details(emp2)
#emp1.details()
#print(emp1.name)

#print(emp1.place)
#print(emp2.place)
if emp1.compare(emp2) :
    print("Age is same")
else:
    print("Ages are different")