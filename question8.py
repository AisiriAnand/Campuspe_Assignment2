# ----------------------------------
# Question 8: Leap Year Checker
# ----------------------------------

try:
    year = int(input("Enter a year: "))

    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print(year, "is a Leap Year.")
        print("Reason: It satisfies leap year conditions.")
    else:
        print(year, "is NOT a Leap Year.")
        print("Reason: It does not satisfy leap year conditions.")

except ValueError:
    print("Please enter a valid year.")