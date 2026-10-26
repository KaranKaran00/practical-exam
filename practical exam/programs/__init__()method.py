#unit 2
#10. WAP for __init__() method 
class Details:

    def __init__(self, no, name):
        self.no = no
        self.name = name

obj1 = Details(1, "Dog")

print(obj1.no, "belongs to the", obj1.name, "group.")