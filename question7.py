# ----------------------------------
# Question 7: Temperature Converter
# ----------------------------------

while True:
    print("\nTemperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "7":
        print("Exiting program...")
        break

    try:
        temp = float(input("Enter temperature value: "))

        if choice == "1":
            result = (temp * 9/5) + 32
            print("Result:", round(result, 2), "°F")

        elif choice == "2":
            result = (temp - 32) * 5/9
            print("Result:", round(result, 2), "°C")

        elif choice == "3":
            result = temp + 273.15
            print("Result:", round(result, 2), "K")

        elif choice == "4":
            result = temp - 273.15
            print("Result:", round(result, 2), "°C")

        elif choice == "5":
            result = (temp - 32) * 5/9 + 273.15
            print("Result:", round(result, 2), "K")

        elif choice == "6":
            result = (temp - 273.15) * 9/5 + 32
            print("Result:", round(result, 2), "°F")

        else:
            print("Invalid choice.")

    except ValueError:
        print("Please enter valid numeric temperature.")