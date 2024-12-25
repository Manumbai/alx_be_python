def main():
    """Provides a customized reminder."""

    task = input("Enter your task: ")

    while True:
        priority = input("Priority (high/medium/low): ").lower()
        if priority in ("high", "medium", "low"):
            break
        else:
            print("Invalid priority. Please enter high, medium, or low.")

    time_bound = input("Is it time-bound? (yes/no): ").lower()

    reminder = ""  # Initialize an empty string

    match priority:
        case "high":
            reminder = f"Reminder: '{task}' is a high priority task"
            if time_bound == "yes":
                reminder += " that requires immediate attention today!"
        case "medium":
            reminder = f"Consider completing '{task}' when you have some time."
        case "low":
            reminder = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."

    print(reminder) # Make sure this is the only print statement for the reminder

if __name__ == "__main__":
    main()
