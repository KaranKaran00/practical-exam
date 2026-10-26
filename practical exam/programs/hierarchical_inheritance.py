#unit 2
#7. WAP for hierarchical inheritance
class Animal:
    def eat(self):
        print("Eating")

class  Dog (Animal):
    def bark(self):
        print("Bow Bow")

class  Fish (Animal):
    def swim(self):
        print("Swimming")

Dog = Dog()
Dog.eat()
Dog.bark()

Fish = Fish()
Fish.eat()
Fish.swim()