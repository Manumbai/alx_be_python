def main():
  """
  Prints the multiplication table for a user-provided number.
  """
  # Ask user for a number
  number = int(input("Enter a number to see its multiplication table: "))

  # Print the multiplication table header
  print(f"Multiplication table for {number}:\n")

  # Use a for loop to iterate from 1 to 10
  for i in range(1, 11):
    # Calculate the product
    product = number * i
    # Print each line of the table
    print(f"{number} * {i} = {product}")

if __name__ == "__main__":
  main()
