class student:
    def __init__(self,name,std,div):
        self.name=name,
        self.std=std
        self.div=div

    def change(self,newname):
        self.name=newname




std1=student("vaishakh","X","B")
std1.change("Rinsha")
print(std1.name)

