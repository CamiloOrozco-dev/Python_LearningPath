# Calculator Program

# Input: Get two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Input: Get the user's choice for the operation
option = int(
    input(
        "Select the operation (1. Addition, 2. Subtraction, 3. Multiplication, 4. Division): "
    )
)

# Check if the option is valid (between 1 and 4)
if option < 1 or option > 4:
    print("Invalid option")
else:
    # Perform the selected operation
    if option == 1:
        result = num1 + num2
        print("The result of addition is:", result)
    elif option == 2:
        result = num1 - num2
        print("The result of subtraction is:", result)
    elif option == 3:
        result = num1 * num2
        print("The result of multiplication is:", result)
    elif option == 4:
        result = num1 / num2
        print("The result of division is:", result)
# Unit Conversion Menu

# Display conversion options
print("1. Celsius to Fahrenheit")
print("2. Kilometers to Miles")
print("3. Celsius to Kelvin")
print("4. Centimeters to Meters")
print("5. Millimeters to Meters")

# Get user's choice
option = int(input("Please choose an option (1-5): "))

# Perform the selected conversion
if option == 1:
    celsius = float(input("Enter the temperature in Celsius: "))
    print("The temperature in Fahrenheit is:", (celsius * 9 / 5) + 32)
elif option == 2:
    kilometers = float(input("Enter the distance in kilometers: "))
    print("The distance in miles is:", kilometers * 0.621371)
elif option == 3:
    celsius = float(input("Enter the temperature in Celsius: "))
    print("The temperature in Kelvin is:", celsius + 273.15)
elif option == 4:
    centimeters = float(input("Enter the length in centimeters: "))
    print("The length in meters is:", centimeters / 100)
elif option == 5:
    millimeters = float(input("Enter the length in millimeters: "))
    print("The length in meters is:", millimeters / 1000)
else:
    print("Invalid option. Please choose a valid option (1-5).")
