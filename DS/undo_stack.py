undo_stack = []
redo_stack = []
while True:
    print("\n--- Undo/Redo System ---")
    print("1. Type")
    print("2. Undo")
    print("3. Redo")
    print("4. Display")
    print("5. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        text = input("Enter text: ")
        undo_stack.append(text)
        redo_stack.clear()
        print("Text added")
    elif choice == 2:
        if undo_stack:
            action = undo_stack.pop()
            redo_stack.append(action)
            print("Undo:", action)
        else:
            print("Nothing to undo")
    elif choice == 3:
        if redo_stack:
            action = redo_stack.pop()
            undo_stack.append(action)
            print("Redo:", action)
        else:
            print("Nothing to redo")
    elif choice == 4:
        print("Undo Stack:", undo_stack)
        print("Redo Stack:", redo_stack)
    elif choice == 5:
        print("Program ended")
        break
    else:
        print("Invalid choice")