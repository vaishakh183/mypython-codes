class first:
    def one(self):
        print("One...")
    def two(self):
        print("Two...")

class second(first):    #inheriting first class to second
    def three(self):
        print("Three...")

class third(second):
    def four(self):
        print("Four.....")

class forth():
    def five(self):
        print("Five....")

class fifth(first,forth):  #multiple inheritance
    def six(self):
        print("six....")


s1=first()
s2=second()
s3=third()
s4=forth()
s5=fifth()


s1.one()
s1.two()

#now i want to inherit all properties of class first to class second.

s2.two()
s3.one()   #multi level inheritance
s5.five()
s5.six()
s5.one()