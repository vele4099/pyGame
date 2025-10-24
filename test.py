def get_input(prompt):
    """Prompt user for a float or 'q' to quit. Returns float or None."""
    while True:
        value = input(prompt)
        value = value.strip()

        # quit check
        if value.lower() == 'q':
            return None

        # number check
        try:
            return float(value)
        except ValueError:
            print("❌ Invalid input. Please enter a number or 'q' to quit.")
    
def add(a, b):
    return a + b

def subtract(a, b):  # fixed spelling
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

# Get user input
CALCisON = True

# Define function to handle user choice
def calculate(a, b, op):
    match op:
        case '+':
            return add(a, b)
        case '-':
            return subtract(a, b)
        case '*':
            return multiply(a, b)
        case '/':
            if b == 0:
                return "Error: Division by zero"
            return divide(a, b)
        case _:
            return "Invalid operation"

while True:
    num1 = get_input("Enter first number (or 'q' to quit): ")
    if num1 is None:
        print("Goodbye!")
        break

    op = input("Enter operation (+, -, *, /): ")

    num2 = get_input("Enter second number (or 'q' to quit): ")
    if num2 is None:
        print("Goodbye!")
        break

    result = calculate(num1, num2, op)
    print("Result:", result)