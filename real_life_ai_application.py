import random

print("Welcome to Guess the Number!")
number = random.randint(1, 10)
attempts = 0

while True:
    guess = int(input("Guess a number between 1 and 10: "))
    attempts += 1
    if guess == number:
        print(f"Congratulations! You guessed it in {attempts} attempts.")
        break
    elif guess < number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
