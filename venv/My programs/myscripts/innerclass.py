class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.lap=self.Laptop()

    def show(self):
        print(self.name , self.age)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand="HP"
            self.model="I5"
            self.ram="8GB"
        def show(self):
            print(self.model, self.brand,self.ram)

s1=Student("Ashutosh",28)
s2=Student("Doug",30)

s2.show()

#print(Student.Laptop.model)