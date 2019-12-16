class parrot:
    def fly(self):
        print("Parrot can fly")
    def swim(self):
        print("Parrot cannot swim")
class Penguin:
    def fly(self):
        print("Penguin cannot fly")

bird=parrot()
bird1=Penguin()

def canfly():
    bird.fly()
    bird1.fly()

canfly()