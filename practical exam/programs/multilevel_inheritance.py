#unit 2
#6. WAP for multilevel inheritance
class Animal:
    def speak(self):
        print("Animal Speaking")


class Dog(Animal):
    def bark(self):
        print("Dog Barking")


class DogChild(Dog):
    def eat(self):
        print("Eating Bread...")

d = DogChild()

d.bark()
d.speak()
d.eat()