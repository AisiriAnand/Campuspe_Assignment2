# ----------------------------------
# Question 20: Number System Functions
# ----------------------------------

def factorial(n):
    if n < 0:
        return "Not defined"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci(n):
    if n <= 0:
        return "Invalid"
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    a = 0
    b = 1
    for i in range(3, n + 1):
        c = a + b
        a = b
        b = c
    return b

def sum_of_digits(n):
    total = 0
    for digit in str(abs(n)):
        total += int(digit)
    return total

def reverse_number(n):
    return int(str(n)[::-1])

def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    total = 0
    for digit in digits:
        total += int(digit) ** power
    return total == n

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

def is_perfect_number(n):
    if n < 1:
        return False
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total == n

def math_menu():
    while True:
        print("\nMath Menu")
        print("1. Factorial")
        print("2. Prime Check")
        print("3. Fibonacci")
        print("4. Sum of Digits")
        print("5. Reverse Number")
        print("6. Armstrong Check")
        print("7. GCD")
        print("8. LCM")
        print("9. Perfect Number")
        print("10. Exit")

        choice = input("Enter choice: ")

        if choice == "10":
            break

        try:
            if choice == "1":
                n = int(input("Enter number: "))
                print("Result:", factorial(n))

            elif choice == "2":
                n = int(input("Enter number: "))
                print("Prime:", is_prime(n))

            elif choice == "3":
                n = int(input("Enter position: "))
                print("Fibonacci:", fibonacci(n))

            elif choice == "4":
                n = int(input("Enter number: "))
                print("Sum of digits:", sum_of_digits(n))

            elif choice == "5":
                n = int(input("Enter number: "))
                print("Reversed:", reverse_number(n))

            elif choice == "6":
                n = int(input("Enter number: "))
                print("Armstrong:", is_armstrong(n))

            elif choice == "7":
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                print("GCD:", gcd(a, b))

            elif choice == "8":
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                print("LCM:", lcm(a, b))

            elif choice == "9":
                n = int(input("Enter number: "))
                print("Perfect Number:", is_perfect_number(n))

            else:
                print("Invalid choice.")

        except ValueError:
            print("Invalid input.")

math_menu()