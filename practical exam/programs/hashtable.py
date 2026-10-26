#unit 2
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