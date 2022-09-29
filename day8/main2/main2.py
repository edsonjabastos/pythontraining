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

    if drt == "decode":
        shift *= -1

    new_text = ""
    for char in txt:
        if char in alphabet:
            letter_index = alphabet.index(char)
            letter_new_index = letter_index + shift
            new_text += alphabet[letter_new_index % len(alphabet)]
        else:
            new_text += char

    print(f"The {drt}d text is {new_text}.")


caesar_is_on = True

while caesar_is_on:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift_input = int(input("Type the shift number:\n"))

    caesar(drt=direction, txt=text, shift=shift_input)

    want_to_leave = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if want_to_leave == "no":
        caesar_is_on = False

print("Bye! Finishing > Caesar Cipher < ...")

import os

os.system("pause")
