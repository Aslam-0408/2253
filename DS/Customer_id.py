def linear_search(ids, key):
    for i in range(len(ids)):
        if ids[i] == key:
            return i
    return -1
def binary_search(ids, key):
    low = 0
    high = len(ids) - 1
    while low <= high:
        mid = (low + high) // 2
        if ids[mid] == key:
            return mid
        elif ids[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1
ids = [105, 203, 156, 301, 178]
key = int(input("Enter customer ID: "))
print("Linear Search:")
pos = linear_search(ids, key)
if pos != -1:
    print("ID found at position", pos)
else:
    print("ID not found")
ids.sort()
print("Sorted IDs:", ids)
print("Binary Search:")
pos = binary_search(ids, key)
if pos != -1:
    print("ID found at position", pos)
else:
    print("ID not found")