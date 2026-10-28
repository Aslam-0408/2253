
queue = []
while True:
    print("\n--- Call Center Queue ---")
    print("1. Add Customer")
    print("2. Serve Customer")
    print("3. Display Queue")
    print("4. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        name = input("Enter customer name: ")
        queue.append(name)
        print("Customer added")
    elif choice == 2:
        if queue:
            customer = queue.pop(0)
            print("Serving:", customer)
        else:
            print("Queue is empty")
    elif choice == 3:
        print("Waiting customers:", queue)
    elif choice == 4:
        print("Program ended")
        break
    else:
        print("Invalid choice")
