# ----------------------------------
# Question 11: Number Pattern Printer
# ----------------------------------

choice = int(input("Choose pattern (1-4): "))
height = int(input("Enter height: "))

if choice == 1:
    for i in range(1, height + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

elif choice == 2:
    for i in range(1, height + 1):
        for j in range(i):
            print(i, end=" ")
        print()

elif choice == 3:
    for i in range(height, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

elif choice == 4:
    for i in range(1, height + 1):
        for j in range(1, i + 1):
            print(j, end="")
        for j in range(i - 1, 0, -1):
            print(j, end="")
        print()

else:
    print("Invalid choice.")