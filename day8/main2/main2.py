alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
from art import *

print(logo)


def caesar(drt, txt, shift):

    while drt != "encode" and drt != "decode":
        drt = input("Accept only 'encode' to encrypt, type 'decode' to decrypt:\n")

    # while alphabet.count(txt) > 0:
    #     txt = input("Accept only letters of alphabet.\n")

    # print(drt)
    # print(shift)
    if drt == "decode":
        shift *= -1
    # print(shift)
    # print(txt)
    # print(alphabet)

    new_text = ""
    for letter in txt:
        letter_index = alphabet.index(letter)
        letter_new_index = letter_index + shift
        new_text += alphabet[letter_new_index % len(alphabet)]
        # print(new_text)
        # print(letter)
        # print(shift)
        # print(letter_index)
        # print(alphabet[letter_new_index % len(alphabet)])
    print(f"The {drt}d text is {new_text}.")


game_is_on = True

while game_is_on:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift_input = int(input("Type the shift number:\n"))

    caesar(drt=direction, txt=text, shift=shift_input)

    want_to_leave = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if want_to_leave == "no":
        game_is_on = False

print("Bye! Finishing > Caesar Cipher < ...")
import os

os.system("pause")
