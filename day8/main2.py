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


def caesar(drt, txt, shift):

    print(drt)
    print(shift)
    if drt == "decode":
        # alphabet.reverse()
        shift *= -1
    print(shift)
    print(txt)
    print(alphabet)

    def encrypt_or_decrypt(tx, sft):
        new_text = ""
        for letter in tx:
            letter_index = alphabet.index(letter)
            letter_new_index = letter_index + sft
            new_text += alphabet[letter_new_index % len(alphabet)]
            print(new_text)
            print(letter)
            print(sft)
            print(letter_index)
            print(alphabet[letter_new_index % len(alphabet)])
        print(f"The encode test is {new_text}.")

    encrypt_or_decrypt(tx=txt, sft=shift)


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift_input = int(input("Type the shift number:\n"))

caesar(drt=direction, txt=text, shift=shift_input)
