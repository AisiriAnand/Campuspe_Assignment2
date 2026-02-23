# ----------------------------------
# Question 4: Age Calculator
# ----------------------------------

import datetime

try:
    birth_year = int(input("Enter your birth year: "))
    current_year = datetime.datetime.now().year

    age = current_year - birth_year

    if age < 0:
        print("Invalid birth year entered.")
    else:
        print("\nCurrent Age:", age, "years")
        print("Age in months:", age * 12)
        print("Age in days (approx):", age * 365)
        print("Age in hours (approx):", age * 365 * 24)
        print("Age in minutes (approx):", age * 365 * 24 * 60)

        print("Years until 100:", 100 - age)

except ValueError:
    print("Please enter a valid year.")