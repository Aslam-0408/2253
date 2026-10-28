class Node:
    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def add_student(self, roll_no, name):
        new_node = Node(roll_no, name)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
    def display(self):
        if self.head is None:
            print("No records")
            return
        temp = self.head
        while temp is not None:
            print("Roll No:", temp.roll_no, "Name:", temp.name)
            temp = temp.next
students = LinkedList()
while True:
    print("\n--- Student Record Management ---")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        roll = int(input("Enter roll number: "))
        name = input("Enter student name: ")
        students.add_student(roll, name)
    elif choice == 2:
        students.display()
    elif choice == 3:
        print("Program ended")
        break
    else:
        print("Invalid choice")
