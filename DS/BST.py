class Node:
    def __init__(self, city, population):
        self.city = city
        self.population = population
        self.left = None
        self.right = None
class BST:
    def insert(self, root, city, population):
        if root is None:
            return Node(city, population)
        if city < root.city:
            root.left = self.insert(root.left, city, population)
        elif city > root.city:
            root.right = self.insert(root.right, city, population)
        else:
            root.population = population
        return root
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.city, root.population)
            self.inorder(root.right)
    def reverse_inorder(self, root):
        if root:
            self.reverse_inorder(root.right)
            print(root.city, root.population)
            self.reverse_inorder(root.left)
    def search(self, root, city, comparisons=0):
        if root is None:
            return None, comparisons
        comparisons += 1
        if city == root.city:
            return root, comparisons
        elif city < root.city:
            return self.search(root.left, city, comparisons)
        else:
            return self.search(root.right, city, comparisons)
    def min_node(self, root):
        current = root
        while current.left:
            current = current.left
        return current
    def delete(self, root, city):
        if root is None:
            return None
        if city < root.city:
            root.left = self.delete(root.left, city)
        elif city > root.city:
            root.right = self.delete(root.right, city)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            successor = self.min_node(root.right)
            root.city = successor.city
            root.population = successor.population
            root.right = self.delete(root.right, successor.city)
        return root
bst = BST()
root = None
data = [
    ("Pune", 7000000),
    ("Mumbai", 20000000),

    ("Delhi", 32000000),
    ("Nagpur", 3000000),
    ("Nashik", 2000000)]
for city, population in data:
    root = bst.insert(root, city, population)
print("Ascending order:")
bst.inorder(root)
print("\nDescending order:")
bst.reverse_inorder(root)
city = input("\nEnter city to search: ")
node, comparisons = bst.search(root, city)
if node:
    print("Population:", node.population)
    print("Comparisons:", comparisons)
else:
    print("City not found")