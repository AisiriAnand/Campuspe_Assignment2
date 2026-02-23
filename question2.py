# ------------------------------
# Question 2: Simple Calculator
# ------------------------------

# Taking two numbers from user
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("\nResults:")

    # Addition
    print(num1, "+", num2, "=", num1 + num2)

    # Subtraction
    print(num1, "-", num2, "=", num1 - num2)

    # Multiplication
    print(num1, "*", num2, "=", num1 * num2)

    # Division (checking division by zero)
    if num2 != 0:
        print(num1, "/", num2, "=", round(num1 / num2, 2))
    else:
        print("Division not possible because second number is zero")

    # Modulus (also check zero)
    if num2 != 0:
        print(num1, "%", num2, "=", num1 % num2)
    else:
        print("Modulus not possible because second number is zero")

    # Exponent
    print(num1, "^", num2, "=", num1 ** num2)

except ValueError:
    print("Invalid input. Please enter numbers only.")