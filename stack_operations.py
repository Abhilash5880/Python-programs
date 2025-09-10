# This program demonstrates a menu-driven implementation of a stack
# using a Python list. A stack is a Last-In, First-Out (LIFO) data structure.

# A Python list can be used to represent a stack.
# The `append()` method adds an item to the top of the stack (push).
# The `pop()` method removes and returns the item from the top of the stack (pop).

stack = []

def push_element(item):
    """Adds an element to the top of the stack."""
    stack.append(item)
    print(f"'{item}' pushed onto the stack.")

def pop_element():
    """Removes and returns the top element from the stack."""
    if not stack:
        print("Error: The stack is empty. Cannot perform pop operation.")
        return None
    else:
        popped_item = stack.pop()
        print(f"'{popped_item}' popped from the stack.")
        return popped_item

def display_stack():
    """Displays all elements in the stack from top to bottom."""
    if not stack:
        print("The stack is currently empty.")
    else:
        print("Stack (Top to Bottom):")
        # Displaying the stack in reverse order to show the top element first
        for item in reversed(stack):
            print(f"-> {item}")
        print("-" * 20)

def main():
    """Main function to run the menu-driven stack program."""
    while True:
        print("\n--- Stack Operations Menu ---")
        print("1. Push an element")
        print("2. Pop an element")
        print("3. Display the stack")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            item_to_push = input("Enter the element to push: ")
            push_element(item_to_push)
        elif choice == '2':
            pop_element()
        elif choice == '3':
            display_stack()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
