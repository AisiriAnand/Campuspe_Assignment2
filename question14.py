# ----------------------------------
# Question 14: Factorial Calculator
# ----------------------------------

try:
    number = int(input("Enter a number: "))

    if number < 0:
        print("Factorial not defined for negative numbers.")
    elif number == 0:
        print("0! = 1")
    else:
        factorial = 1
        expression = ""

        for i in range(number, 0, -1):
            factorial *= i
            expression += str(i)
            if i != 1:
                expression += " × "

        print(number, "! =", expression, "=", factorial)

except ValueError:
    print("Invalid input.")