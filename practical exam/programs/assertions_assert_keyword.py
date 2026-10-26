#unit 2
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