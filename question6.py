# ----------------------------------
# Question 6: Grade Calculator
# ----------------------------------

try:
    marks1 = float(input("Enter marks for Subject 1: "))
    marks2 = float(input("Enter marks for Subject 2: "))
    marks3 = float(input("Enter marks for Subject 3: "))
    marks4 = float(input("Enter marks for Subject 4: "))
    marks5 = float(input("Enter marks for Subject 5: "))

    total = marks1 + marks2 + marks3 + marks4 + marks5
    percentage = total / 5

    print("\nTotal Marks:", total, "/ 500")
    print("Percentage:", round(percentage, 2), "%")

    # Grade calculation
    if percentage >= 90:
        grade = "A+ (Outstanding)"
    elif percentage >= 80:
        grade = "A (Excellent)"
    elif percentage >= 70:
        grade = "B (Good)"
    elif percentage >= 60:
        grade = "C (Average)"
    elif percentage >= 50:
        grade = "D (Pass)"
    else:
        grade = "F (Fail)"

    # Pass or fail (each subject >= 40)
    if marks1 >= 40 and marks2 >= 40 and marks3 >= 40 and marks4 >= 40 and marks5 >= 40:
        result = "Pass"
    else:
        result = "Fail"

    print("Grade:", grade)
    print("Result:", result)

except ValueError:
    print("Please enter valid marks.")