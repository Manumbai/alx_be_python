def main():
  """
  Prints a square pattern of asterisks based on user input.
  """
  # Ask user for pattern size
  while True:
    try:
      size = int(input("Enter the size of the pattern (positive integer): "))
      if size > 0:
        break
      else:
        print("Please enter a positive integer.")
    except ValueError:
      print("Invalid input. Please enter a number.")

  # Draw the pattern using nested loops
  for _ in range(size):
    for _ in range(size):
      print("*", end="")
    print()  # Move to next line

if __name__ == "__main__":
  main()
