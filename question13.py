# ----------------------------------
# Question 13: Sum and Average Calculator
# ----------------------------------

try:
    count = int(input("How many numbers? "))

    total = 0
    numbers = []

    for i in range(count):
        num = float(input("Enter number " + str(i+1) + ": "))
        numbers.append(num)
        total += num

    average = total / count
    maximum = max(numbers)
    minimum = min(numbers)

    print("\nSum:", total)
    print("Average:", average)
    print("Maximum:", maximum)
    print("Minimum:", minimum)

except ValueError:
    print("Invalid input.")