FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

temp_input = input("Enter the temperature to convert: ")
temperature = float(temp_input) # Convert input to float here
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

if unit == "C":
    converted_temp = convert_to_fahrenheit(temperature)
    print(f"{temperature:.1f}°C is {converted_temp:.1f}°F")
elif unit == "F":
    converted_temp = convert_to_celsius(temperature)
    print(f"{temperature:.1f}°F is {converted_temp:.1f}°C")
else:
    raise ValueError("Invalid unit. Please enter 'C' or 'F'.")


    
        # print("Invalid temperature. Please enter a numeric value.")

