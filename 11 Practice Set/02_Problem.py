class Animals:
    legs = 4


class Pets(Animals):
    isliveinhome = False

class Dog(Pets):
    def bark(self):
        print("Bow Bow")

d1 = Dog()
print(d1.isliveinhome, d1.legs)
d1.bark()