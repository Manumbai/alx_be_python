def display_menu():
    """Displays the menu options to the user."""
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """Manages the shopping list functionality."""
    shopping_list = []
    while True:
        display_menu()
        try:  # Use a try-except block for input validation
            choice = int(input("Enter your choice: "))  # Convert input to integer
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue  # Go back to the beginning of the loop

        if choice == 1:  # Compare with integers now
            item_to_add = input("Enter item name: ")
            shopping_list.append(item_to_add)
            print(f"{item_to_add} added to the list.")
        elif choice == 2:
            item_to_remove = input("Enter item name to remove: ")
            if item_to_remove in shopping_list:
                shopping_list.remove(item_to_remove)
                print(f"{item_to_remove} removed from the list.")
            else:
                print(f"Item '{item_to_remove}' not found in the list.")
        elif choice == 3:
            if shopping_list:
                print("Shopping List:")
                for item in shopping_list:
                    print(f"- {item}")
            else:
                print("The shopping list is empty.")
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
