import random

def play_game():
    print("\nWelcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")
    print("Try to guess it!\n")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess > secret_number:
            print("Too high! Try again.\n")
        elif guess < secret_number:
            print("Too low! Try again.\n")
        else:
            print("Correct!")
            print(f"You guessed the number in {attempts} attempts.")
            break


while True:
    play_game()

    choice = input("\nDo you want to play again? (yes/no): ").lower()
    if choice != "yes":
        print("\nThanks for playing!")
        break