from art import logo, vs
from data import data
from random import randint
import os

print(logo)


def random_pick(data_array):
    random_choice = randint(0, len(data) - 1)
    return data_array[random_choice]


def game():
    score = 0
    player_lost = False
    a_pick = random_pick(data)
    last_pick = 0
    while not player_lost:
        b_pick = random_pick(data)

        while a_pick == b_pick:
            b_pick = random_pick(data)

        print(
            f"Compare A: {a_pick['name']}, a {a_pick['description']}, from  {a_pick['country']}"
        )
        print(vs)
        print(
            f"Against B: {b_pick['name']}, a {b_pick['description']}, from  {b_pick['country']}"
        )
        guess = input("Who has more followers?: Type 'A' or 'B': ").upper()

        if guess == "A":
            if a_pick["follower_count"] > b_pick["follower_count"]:
                score += 1
                os.system("cls")
                print(logo)
                print(f"You're right! Current score: {score}.")
                a_pick = b_pick
            else:
                player_lost = True
                os.system("cls")
                print(logo)
                print(f"Sorry, that's wrong. Final Score: {score}")

        elif guess == "B":
            if b_pick["follower_count"] > a_pick["follower_count"]:
                score += 1
                os.system("cls")
                print(logo)
                print(f"You're right! Current score: {score}.")
                a_pick = b_pick

            else:
                player_lost = True
                os.system("cls")
                print(logo)
                print(f"Sorry, that's wrong. Final Score: {score}")
        else:
            return


game()
os.system("pause")
