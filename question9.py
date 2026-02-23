# ----------------------------------
# Question 9: Ticket Pricing System
# ----------------------------------

try:
    age = int(input("Enter age: "))
    day = input("Enter day of week: ").lower()
    tickets = int(input("Number of tickets: "))

    # Age-based pricing
    if age < 3:
        base_price = 0
        category = "Free"
    elif age <= 12:
        base_price = 150
        category = "Child"
    elif age <= 59:
        base_price = 300
        category = "Adult"
    else:
        base_price = 200
        category = "Senior"

    total_price = base_price * tickets

    # Day-based discount
    if day in ["friday", "saturday", "sunday"]:
        discount = total_price * 0.20
    else:
        discount = 0

    final_amount = total_price - discount

    print("\nBase price per ticket: ₹", base_price, "(", category, ")")
    print("Total before discount: ₹", total_price)
    print("Discount: ₹", round(discount, 2))
    print("Final Amount: ₹", round(final_amount, 2))

except ValueError:
    print("Invalid input.")