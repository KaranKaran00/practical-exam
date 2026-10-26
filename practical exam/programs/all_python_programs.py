#unit 1 
#1. WAP to print 'HELLO WORLD!!'
print("Hello")
print('Hello')


#2. WAP to assign string to a variable
a = "Hello"
print(a)


#3. WAP for slicing
b = "Hello, World!"
print(b[2:5])


#4. WAP to modify string
# 1. Upper Case
a = "Hello, World!"
print(a.upper())

# 2. Lower Case
a = "Hello, World!"
print(a.lower())

# 3. Remove Whitespace
a = "Hello, World!"
print(a.strip()) # returns "Hello,World!

# 4. Replace String
a = "Hello, World!"
print(a.replace("H", "J"))


#5. WAP for String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)

#6. WAP for If statement
a = 33
b = 200

if b > a:
    print("b is greater than a")


#7. WAP for if...elif statement
a = 33
b = 33

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")


#8. WAP for if...elif...else statement
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")


#9. WAP for short hand If statement
p = 83
q = 67
if p > q:print("p is greater than q")


#10. WAP for short hand If...else statement
a = 23
b = 33
print("A") if a > b else print("B")


#11. WAP for nested if statement
x = 41

if x > 10:
    print("Above ten,")

    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")


#12. WAP for operators
#And keyword
a = 200
b = 33
c = 500

if a > b and c > a:
    print("Both conditions are True")

#Or keyword
a = 200
b = 33
c = 500

if a > b or a > c:
    print("At least one of the conditions is True")

#Not keyword
a = 33
b = 200

if not a > b:
    print("a is NOT greater than b")


#13. WAP for match case
day = 4

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case _:
        print("Sunday")


#14. WAP for while loop
i = 1

while i < 6:
    print(i)
    i += 1

#while loop with break
i = 1

while i < 6:
    print(i)

    if i == 3:
        break

    i += 1

#while loop with continue
i = 0

while i < 6:
    i += 1

    if i == 3:
        continue

    print(i)


#15. WAP for for loop
fruits = ["apple", "banana", "cherry"]

for x in fruits:
    print(x)

#for loop using range
for x in range(6):
    print(x)


#16. WAP for function
def printMe(text):
    print(text)
    return

printMe("Hello Students")


#17. WAP for recursion
def factorial_recursive(n):

    if n == 1:
        print(n, end=" = ")
        return 1

    else:
        print(n, end=" x ")
        return n * factorial_recursive(n - 1)

i = int(input("Enter Any Number: "))

print(factorial_recursive(i))


#18. WAP for module
#mymodule.py
#def myAdd(fVal, sVal):
#    return fVal + sVal

#testfile.py
#import mymodule as add

#print(add.myAdd(50, 6))#


#19. WAP for file handling
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("Hello\n")
    f.write("czmg\n")
    f.write("Students\n")


#20. WAP for list and mutability
#list is mutable
myList = [10, 20, 30, 40, 50]

print(myList)

myList[0] = 5

print(myList)

#tuple is immutable
myTuple = (10, 20, 30, 40, 50)

print(myTuple)

myTuple[0] = 5


#21. WAP for function as object
def greet(name):
    return f"Hello, {name}!"

my_function = greet

print(my_function("Students"))


#22. WAP for passing function as argument
def apply_operation(addfunc, x, y):
    return addfunc(x, y)

def add(a, b):
    return a + b

result = apply_operation(add, 5, 3)

print(result)




#unit 2
#1. WAP for ZeroDivisionError
marks = 10000

a = marks / 0

print(a)


#2. WAP for try and except
a = [1, 2, 3]

try:
    print("Second element = %d" % (a[1]))
    print("Fourth element = %d" % (a[3]))

except:
    print("An error occurred")


#3. WAP for catching specification exception
def fun(a):
    if a < 4:
        b = a / (a - 3)
        print("Value of b =", b)

try:
    fun(3)
    fun(5)

except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")

except NameError:
    print("NameError Occurred and Handled")


#4. WAP for finally keyword
try:
    k = 5 / 0
    print(k)

except ZeroDivisionError:
    print("Can't divide by zero")

finally:
    print("This is always executed")


#5. WAP for Assertions(assert keyword)
a = 4
b = 2

print("The value of a / b is :")

assert b != 0, "Zero Division Error"

print(a / b)

#assertion for data types
a = "hello"
b = 42

assert type(a) == str
assert type(b) == int

print("a =", a)
print("b =", b)


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


#9. WAP for self method
class Details:
    name = "Rajvi"
    age = 20

    def desc(self):
        print("My name is", self.name, "and I'm", self.age, "years old.")

obj1 = Details()
obj1.desc()


#10. WAP for __init__() method 
class Details:

    def __init__(self, no, name):
        self.no = no
        self.name = name

obj1 = Details(1, "Dog")

print(obj1.no, "belongs to the", obj1.name, "group.")


#11. WAP for linear search
def search(arr, N, x):

    for i in range(0, N):

        if arr[i] == x:
            return i

    return -1

arr = [2, 3, 4, 10, 40]
x = 4
N = len(arr)

result = search(arr, N, x)

if result == -1:
    print("Element is not present in array")
else:
    print("Element is present at index", result)


#12. WAP for binary search
def binarySearch(arr, low, high, x):

    while low <= high:

        mid = low + (high - low) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return -1

arr = [2, 3, 4, 10, 40]
x = 10

result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")


#13. WAP for selection sort
def selectionSort(array, size):

    for s in range(size):
        min_idx = s

        for i in range(s + 1, size):

            if array[i] < array[min_idx]:
                min_idx = i

        array[s], array[min_idx] = array[min_idx], array[s]


data = [7, 2, 1, 6]
selectionSort(data, len(data))

print("Sorted Array in Ascending Order is:")
print(data)



#14. WAP for merge sort
def merge_sort(arr):

    if len(arr) > 1:
        # Step 1: Divide
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Step 2: Recursively sort each half
        merge_sort(left_half)
        merge_sort(right_half)

        # Step 3: Merge the sorted halves
        i = j = k = 0

        # Compare and merge
        while i < len(left_half) and j < len(right_half):

            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Remaining elements of left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Remaining elements of right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
print("Original array:", arr)
merge_sort(arr)
print("Sorted array:", arr)


#15. WAP for hashtable (Dictionary)
student = {
    "name": "Rajvi",
    "age": 20,
    "course": "BCA"
}

print("Original Hashtable:", student)
print("Hash Value is:", hash("course"))

if "name" in student:
    print("Name exists in the hashtable.")