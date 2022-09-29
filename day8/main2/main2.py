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

    print(drt)
    print(shift)
    if drt == "decode":
        # alphabet.reverse()
        shift *= -1
    print(shift)
    print(txt)
    print(alphabet)

    new_text = ""
    for letter in txt:
        letter_index = alphabet.index(letter)
        letter_new_index = letter_index + shift
        new_text += alphabet[letter_new_index % len(alphabet)]
        print(new_text)
        print(letter)
        print(shift)
        print(letter_index)
        print(alphabet[letter_new_index % len(alphabet)])
    print(f"The {drt}d text is {new_text}.")

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift_input = int(input("Type the shift number:\n"))

caesar(drt=direction, txt=text, shift=shift_input)
import os
os.system('pause')
