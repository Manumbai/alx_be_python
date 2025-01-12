from datetime import datetime, timedelta

def display_current_datetime():
    """Gets and displays the current date and time in YYYY-MM-DD HH:MM:SS format."""
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

def calculate_future_date(number_of_days):
    """Calculates the future date by adding the specified number of days to the current date."""
    current_date = datetime.now()
    future_date = current_date + timedelta(days=number_of_days)
    formatted_date = future_date.strftime("%Y-%m-%d")
    print(f"Enter the number of days to add to the current date: {number_of_days}")
    print(f"Future date: {formatted_date}")

if __name__ == "__main__":
    display_current_datetime()
    while True:
        try:
            number_of_days = int(input("Enter the number of days to add (or 0 to exit): "))
            if number_of_days == 0:
                break
            calculate_future_date(number_of_days)
        except ValueError:
            print("Invalid input. Please enter an integer.")

