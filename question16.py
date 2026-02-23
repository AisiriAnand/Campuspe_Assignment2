# ----------------------------------
# Question 16: Number Guessing Game
# ----------------------------------

import random

best_score = None

while True:
    secret_number = random.randint(1, 100)
    attempts = 7
    used_attempts = 0

    print("\nGuess the number between 1 and 100")

    while attempts > 0:
        try:
            guess = int(input("Enter your guess: "))
            used_attempts += 1
            attempts -= 1

            if guess == secret_number:
                print("Correct! You guessed in", used_attempts, "attempts.")
                
                if best_score is None or used_attempts < best_score:
                    best_score = used_attempts
                    print("New best score:", best_score)

                break

            elif guess < secret_number:
                print("Too low!")
            else:
                print("Too high!")

            if abs(guess - secret_number) <= 5:
                print("Hint: You are very close!")

            print("Attempts remaining:", attempts)

        except ValueError:
            print("Invalid input.")

    if attempts == 0:
        print("You lost! The number was", secret_number)

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break