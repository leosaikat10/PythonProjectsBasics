import random

number = random.randint(1, 10)
attempts = 3

while attempts > 0:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == number:
        print("Congratulations ! You guessed the number ")
    elif guess > number:
        print("Too high ! try again ")
    else:
        print("Too Low ! try again ")

    attempts -= 1
    print(f"You have {attempts} attempts left.")
    
           
if attempts == 0:
    print("Game over! The number was:", number)
