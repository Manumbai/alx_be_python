def main():
  """
  Performs basic mathematical operations based on user input using Match Case.
  """
  # Get user input for first number
  num1 = float(input("Enter the first number: "))

  # Get user input for second number
  num2 = float(input("Enter the second number: "))

  # Get user input for operation
  operation = input("Choose the operation (+, -, *, /): ")

  # Perform calculation using Match Case
  match operation:
    case "+":
      result = num1 + num2
      print(f"The result is {result:.2f}.")  # Format with 2 decimal places
    case "-":
      result = num1 - num2
      print(f"The result is {result:.2f}.")
    case "*":
      result = num1 * num2
      print(f"The result is {result:.2f}.")
    case "/":
      if num2 == 0:
        print("Cannot divide by zero.")
      else:
        result = num1 / num2
        print(f"The result is {result:.2f}.")
    case _:
      print("Invalid operation. Please choose +, -, *, or /.")

if __name__ == "__main__":
  main()

