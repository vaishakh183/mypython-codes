class school:
    def __init__(self):
        print("test")

    def student(self):
        print("student")

class excel:
    def student(self):
        print("student")
        print("student from excel tution center")

class tution:
    def classes(self,s):
        s.student()

s=excel()
tut=tution()
tut.classes(s)
