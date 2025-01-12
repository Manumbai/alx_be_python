def display_menu():
    """Displays the menu options to the user."""
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """Manages the shopping list functionality."""
    shopping_list = []  # Create an empty shopping list
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Logic to add an item (replace with actual implementation)
            item_to_add = input("Enter item name: ")
            shopping_list.append(item_to_add)  # Example: Simple appending
            print(f"{item_to_add} added to the list.")

        elif choice == '2':
            # Logic to remove an item (replace with actual implementation)
            item_to_remove = input("Enter item name to remove: ")
            if item_to_remove in shopping_list:
                shopping_list.remove(item_to_remove)
                print(f"{item_to_remove} removed from the list.")
            else:
                print(f"Item '{item_to_remove}' not found in the list.")

        elif choice == '3':
            # Logic to display the shopping list (replace with actual implementation)
            if shopping_list:
                print("Shopping List:")
                for item in shopping_list:
                    print(f"- {item}")
            else:
                print("The shopping list is empty.")

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
