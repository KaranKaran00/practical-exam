#unit 2
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