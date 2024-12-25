def main():
    """
    Prints a square pattern of asterisks based on user input,
    with input validation using a while loop.
    """
    while True:  # Input validation loop
        try:
            size = int(input("Enter the size of the pattern (positive integer): "))
            if size > 0:
                break  # Exit loop if input is valid
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Draw the pattern using nested for loops
    for _ in range(size):
        for _ in range(size):
            print("*", end="")
        print()

if __name__ == "__main__":
    main()
