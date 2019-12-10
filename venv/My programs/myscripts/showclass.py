class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        print(self.name , self.age)


s1=Student("Ashutosh",28)
s2=Student("Doug",30)

s2.show()
