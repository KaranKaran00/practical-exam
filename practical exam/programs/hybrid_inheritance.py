#unit 2
#8. WAP for hybrid inheritance
class Animal:
    def eat(self):
        print("Eating")

class  Mammal (Animal):
    def walk(self):
        print("Walking")

class  Bird (Animal):
    def fly(self):
        print("Flying")

class Bat(Mammal, Bird):
    pass

Bat = Bat()
Bat.eat()
Bat.walk()
Bat.fly()