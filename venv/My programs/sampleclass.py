class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age



    def aboveage(self):
        if self.age >=30:
            return True
        else:
            return False


