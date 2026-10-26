#unit 1
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