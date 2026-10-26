#unit 1
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