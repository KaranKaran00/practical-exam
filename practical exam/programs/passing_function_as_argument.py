#unit 1
#21. WAP for passing function as argument
def apply_operation(addfunc, x, y):
    return addfunc(x, y)

def add(a, b):
    return a + b

result = apply_operation(add, 5, 3)

print(result)