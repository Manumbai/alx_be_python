def main():
  """
  Provides a customized reminder based on task priority and time sensitivity.
  """
  # Get user input for task
  task = input("Enter your task: ")

  # Get user input for priority
  while True:
    priority = input("Priority (high/medium/low): ").lower()
    if priority in ("high", "medium", "low"):
      break
    else:
      print("Invalid priority. Please enter high, medium, or low.")

  # Get user input for time sensitivity
  time_bound = input("Is it time-bound? (yes/no): ").lower()

  # Process task and provide reminder
  match priority:
    case "high":
      reminder = f"Reminder: '{task}' is a high priority task"
      if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    case "medium":
      reminder = f"Consider completing '{task}' when you have some time."
    case "low":
      reminder = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."

  print(reminder)

if __name__ == "__main__":
  main()
