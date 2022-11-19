from random import randint
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts = 0
if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5
random_number = randint(1, 100)
print(random_number)
while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == random_number:
        print(f"You got it! The answer was {random_number}")
        attempts = 0
    elif guess > random_number:
        print("Too high.")
        attempts -= 1
        if attempts == 0:
            print("You've run out of guesses, you lose.")
        print("Guess again.")
    elif guess < random_number:
        print("Too low.")
        attempts -= 1
        if attempts == 0:
            print("You've run out of guesses, you lose.")
        print("Guess again.")
