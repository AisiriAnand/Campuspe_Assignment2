# ----------------------------------
# Question 10: ATM Simulator
# ----------------------------------

balance = 10000

while True:
    print("\nATM SIMULATOR")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Current Balance: ₹", balance)

    elif choice == "2":
        try:
            amount = float(input("Enter amount to deposit: "))
            if amount > 0:
                balance += amount
                print("Deposit successful!")
                print("New balance: ₹", balance)
            else:
                print("Invalid deposit amount.")
        except ValueError:
            print("Invalid input.")

    elif choice == "3":
        try:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= 0:
                print("Invalid amount.")
            elif amount > balance:
                print("Insufficient balance.")
            elif balance - amount < 500:
                print("Minimum balance of ₹500 must remain.")
            else:
                balance -= amount
                print("Withdrawal successful!")
                print("New balance: ₹", balance)
        except ValueError:
            print("Invalid input.")

    elif choice == "4":
        print("Thank you for using ATM.")
        break

    else:
        print("Invalid choice.")