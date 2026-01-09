import random

def play_game():
    number = random.randint(1, 10)
    attempts = 3

    print("\nI'm thinking of a number between 1 and 10")

    while attempts > 0:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number")
            continue

        if guess == number:
            print(" You guessed it right!")
            return
        elif guess > number:
            print("Too high!")
        else:
            print("Too low!")

        attempts -= 1
        print("Attempts left:", attempts)

    print("Game over! The number was:", number)

while True:
    play_game()
    again = input("Play again? (y/n): ").lower()
    if again != "y":
        print("Thanks for playing!")
        break
