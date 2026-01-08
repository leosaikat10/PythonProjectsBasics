import random

number = random.randint(1, 10)
attempts = 3

while attempts > 0:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == number:
        print("You guessed it right!")
        break
    else:
        attempts -= 1
        print("Wrong guess. Attempts left:", attempts)

if attempts == 0:
    print("Game over! The number was:", number)
