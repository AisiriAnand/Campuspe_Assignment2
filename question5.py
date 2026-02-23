# ----------------------------------
# Question 5: Bill Splitter
# ----------------------------------

try:
    total_bill = float(input("Enter total bill: "))
    people = int(input("Number of people: "))
    tax_percent = float(input("Tax percentage: "))
    tip_percent = float(input("Tip percentage: "))

    if people <= 0:
        print("Number of people must be greater than 0.")
    else:
        tax_amount = total_bill * tax_percent / 100
        after_tax = total_bill + tax_amount

        tip_amount = after_tax * tip_percent / 100
        final_total = after_tax + tip_amount

        per_person = final_total / people

        print("\n=== BILL BREAKDOWN ===")
        print("Subtotal: ₹", round(total_bill, 2))
        print("Tax:", round(tax_amount, 2))
        print("After tax: ₹", round(after_tax, 2))
        print("Tip:", round(tip_amount, 2))
        print("Total: ₹", round(final_total, 2))
        print("Per person: ₹", round(per_person, 2))

except ValueError:
    print("Invalid input. Please enter correct values.")