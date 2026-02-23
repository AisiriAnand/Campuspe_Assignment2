# ----------------------------------
# Question 15: Prime Number Checker
# ----------------------------------

# Part 1: Check single number

try:
    number = int(input("Enter a number: "))

    if number < 2:
        print(number, "is NOT a prime number")
    elif number == 2:
        print("2 is a PRIME number")
    else:
        is_prime = True
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime = False
                break

        if is_prime:
            print(number, "is a PRIME number")
        else:
            print(number, "is NOT a prime number")

    # Part 2: Prime numbers in range
    start = int(input("Enter start range: "))
    end = int(input("Enter end range: "))

    print("Prime numbers:", end=" ")

    for num in range(start, end + 1):
        if num >= 2:
            prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    prime = False
                    break
            if prime:
                print(num, end=" ")

except ValueError:
    print("Invalid input.")