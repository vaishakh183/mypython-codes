import math
class shape:
    def __init__(self,color='black',filled=True):
        self.color=color
        self.filled=filled

    def get_color(self):
        return self.color
    def get_filled(self):
        return self.filled

class rectangle(shape):
    def __init__(self,length,width):
        super().__init__()
        self.length=length
        self.width=width
    def area(self):
        return self.length * self.width

class circle(shape):
    def __init__(self,radius):
        super().__init__()
        self.radius=radius

    def perimeter(self):
        return 2*(math.pi * self.radius)

b=rectangle(4,3)
c=circle(5)
print(b.get_color(),b.area(),b.get_filled())
print(c.perimeter())
print(c.get_color())
