import random

def scramble_word(word):
    letters = list(word)
    random.shuffle(letters)
    return ''.join(letters)


def play_round():
    words = [
        "python", "computer", "science", "program",
        "keyboard", "internet", "variable",
        "function", "loop", "algorithm"
    ]

    original_word = random.choice(words)
    scrambled = scramble_word(original_word)

    attempts = 3

    print("\nWord Scrambling Game")
    print(f"Scrambled word: {scrambled}")
    print("You have 3 attempts to guess the correct word.\n")

    while attempts > 0:
        guess = input("Your guess: ").lower()

        if guess == original_word:
            print("🎉 Correct! You guessed the word.")
            return 1
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Wrong guess. Attempts left: {attempts}\n")

    print(f" Out of attempts! The correct word was '{original_word}'.")
    return 0


score = 0

while True:
    score += play_round()

    choice = input("\nDo you want to play another round? (yes/no): ").lower()
    if choice != "yes":
        print(f"\n Final Score: {score}")
        print("Thanks for playing! ")
        break
