# This module provides a simple calculator application.

# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    # Check for division by zero to prevent errors
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y

# Main function to run the calculator program
def main():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        # Take input from the user for the desired operation
        choice = input("Enter choice(1/2/3/4): ")

        # Check if the choice is one of the valid operations
        if choice in ('1', '2', '3', '4'):
            try:
                # Get numbers from the user, converting them to float
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                # Handle cases where non-numeric input is provided
                print("Invalid input. Please enter numbers only.")
                continue # Continue to the next iteration of the loop

            # Perform the chosen operation and print the result
            if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))
            elif choice == '2':
                print(num1, "-", num2, "=", subtract(num1, num2))
            elif choice == '3':
                print(num1, "*", num2, "=", multiply(num1, num2))
            elif choice == '4':
                print(num1, "/", num2, "=", divide(num1, num2))
            
            # Ask user if they want to perform another calculation
            next_calculation = input("Let's do next calculation? (yes/no): ")
            # If the user types 'no', exit the loop
            if next_calculation.lower() == "no":
                break
        else:
            # Inform the user about invalid operation input
            print("Invalid Input")

# Ensure main() function runs only when the script is executed directly (not imported as a module)
if __name__ == "__main__":
    main()