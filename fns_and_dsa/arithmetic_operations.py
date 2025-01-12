def perform_operation(num1, num2, operation):
  """
  Performs basic arithmetic operations based on the provided parameters.

  Args:
      num1 (float): The first number.
      num2 (float): The second number.
      operation (str): The arithmetic operation to perform ('add', 'subtract', 'multiply', or 'divide').

  Returns:
      float: The result of the operation or a message for division by zero.
  """
  if operation == 'add':
    return num1 + num2
  elif operation == 'subtract':
    return num1 - num2
  elif operation == 'multiply':
    return num1 * num2
  elif operation == 'divide':
    if num2 == 0:  # Handle division by zero
      return "Error: Cannot divide by zero"
    else:
      return num1 / num2
  else:
    return "Invalid operation. Please enter 'add', 'subtract', 'multiply', or 'divide'."

# Example usage (optional, not required for the script):
# result = perform_operation(5, 2, 'add')
# print(result)  # Output: 7.0