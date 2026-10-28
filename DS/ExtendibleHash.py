BUCKET_SIZE = 2
class Bucket:
    def __init__(self, depth):
        self.depth = depth
        self.items = {}
class ExtendibleHash:
    def __init__(self):
        self.global_depth = 1
        self.directory = [Bucket(1), Bucket(1)]
    def index(self, key):
        mask = (1 << self.global_depth) - 1
        return key & mask
    def double_directory(self):
        self.directory = self.directory + self.directory
        self.global_depth += 1
    def split_bucket(self, index):
        old = self.directory[index]
        if old.depth == self.global_depth:
            self.double_directory()
        new_depth = old.depth + 1
        new_bucket = Bucket(new_depth)
        old.depth = new_depth
        for i in range(len(self.directory)):
            if (self.directory[i] is old and
                    ((i >> (new_depth - 1)) & 1)):
                self.directory[i] = new_bucket
        old_items = list(old.items.items())
        old.items.clear()
        for key, value in old_items:
            self.insert(key, value)
    def insert(self, key, value):
        index = self.index(key)
        bucket = self.directory[index]
        if key in bucket.items:
            bucket.items[key] = value
            return
        if len(bucket.items) < BUCKET_SIZE:
            bucket.items[key] = value
        else:
            self.split_bucket(index)
            self.insert(key, value)
    def search(self, key):
        bucket = self.directory[self.index(key)]
        return bucket.items.get(key, None)
    def delete(self, key):
        bucket = self.directory[self.index(key)]
        if key in bucket.items:
            del bucket.items[key]
            return True
        return False
h = ExtendibleHash()
while True:
    print("\n--- Extendible Hashing ---")
    print("1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        key = int(input("Enter key: "))
        value = input("Enter value: ")
        h.insert(key, value)
        print("Inserted")
    elif choice == 2:
        key = int(input("Enter key: "))
        value = h.search(key)
        if value is not None:
            print("Value:", value)
        else:
            print("Key not found")
    elif choice == 3:
        key = int(input("Enter key: "))
        if h.delete(key):
            print("Deleted")
        else:
            print("Key not found")
    elif choice == 4:
        print("Program ended")
        break
    else:
        print("Invalid choice")
