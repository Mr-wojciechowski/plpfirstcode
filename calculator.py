# Simple calculator program

# Get input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

# Perform calculation
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 == 0:
        print("Error: Cannot divide by zero")
    else:
        result = num1 / num2
else:
    print("Invalid operation")
    exit()

# Display result
print(f"{num1} {operation} {num2} = {result}")