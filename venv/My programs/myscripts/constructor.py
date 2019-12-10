class first:
    def __init__(self):
        print("From init method of First class")

    def one(self):
        print("One...")

class second(first):    #inheriting first class to second

    def __init__(self):
        super().__init__()
        print("From init Method of second class")

    def three(self):
        print("Three...")

#s1=first()
s2=second()
#class checks for init method on its own class first ,if not present it checks from inherited class.
#if you want to call init method from both the classes , you should use @super



