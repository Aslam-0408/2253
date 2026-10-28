SIZE = 10
table = [None] * SIZE
def hash_function(key):
    return key % SIZE
def insert(key):
    index = hash_function(key)
    for i in range(SIZE):
        pos = (index + i) % SIZE
        if table[pos] is None or table[pos] == "DELETED":
            table[pos] = key
            print("Inserted at index", pos)
            return
    print("Hash table is full")
def search(key):
    index = hash_function(key)
    for i in range(SIZE):
        pos = (index + i) % SIZE
        if table[pos] is None:
            return -1
        if table[pos] == key:
            return pos
    return -1
def delete(key):
    pos = search(key)
    if pos == -1:
        print("Key not found")
    else:
        table[pos] = "DELETED"
        print("Key deleted")
def display():
    for i in range(SIZE):
        print(i, ":", table[i])
while True:
    print("\n--- Hash Table using Linear Probing ---")
    print("1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        key = int(input("Enter key: "))
        insert(key)
    elif choice == 2:
        key = int(input("Enter key: "))
        pos = search(key)
        if pos != -1:
            print("Key found at index", pos)
        else:
            print("Key not found")
    elif choice == 3:
        key = int(input("Enter key: "))
        delete(key)
    elif choice == 4:
        display()
    elif choice == 5:
        print("Program ended")
        break
    else:
        print("Invalid choice")
