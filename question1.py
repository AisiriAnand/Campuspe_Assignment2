# ==============================
# QUESTION 1: Personal Bio Card
# ==============================

# Storing personal details in variables
student_name = "Aisiri Anand"
student_age = 21
course_name = "Gen AI"
college_name = "DBIT"
email_address = "aisirianand03@gmail.com"

# Printing formatted bio card
print("╔══════════════════════════════════════╗")
print("║            STUDENT BIO CARD          ║")
print("╠══════════════════════════════════════╣")
print(f"║ Name    : {student_name:<26} ║")
print(f"║ Age     : {student_age} years{' ' * 19}║")
print(f"║ Course  : {course_name:<26} ║")
print(f"║ College : {college_name:<26} ║")
print(f"║ Email   : {email_address:<26} ║")
print("╚══════════════════════════════════════╝")