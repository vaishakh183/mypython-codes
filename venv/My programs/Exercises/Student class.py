

class student:
    def __init__(self,first,last,mark):
        self.first=first
        self.last=last
        self.mark=mark
        self.email=first+"."+last +"@gmail.com"

    def fullname(self):
        return self.first + " " + self.last

    def gracemark(self):
        self.mark=self.mark + 5
        return  self.mark


class addmark(student):
    addionalmark =10
#inherit attributes from main class
    def __init__(self,first,last,mark,language):
        super().__init__(first,last,mark)
        self.language=language





std1=student("vaishakh","vk",70)
std2=student("rinsha","k",90)

#print(std2.email)
#print(student.fullname(std1))

#print(std2.mark)
#print("Grace mark " + str(student.gracemark(std2)))

#get values in dictionary
#print(std2.__dict__)

#print(student.__dict__)


#Check the class inheritance. objects and methods are accessible on second class from first.

#second_std1=addmark("vaishakh","vk",70)
#second_std2=addmark("rinsha","k",90)

#print(second_std1.mark)
#print(second_std2.mark)

#print(help(addmark))


std3=addmark("pommi","k",80,"malayalam")

print(std3.language)
print(std3.first)

#abstract class cannot be instatiated. we cannot create objects or instances with this classes.
#it is used for inherting or use as base class.
