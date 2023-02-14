# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

PLACE_HOLDER = "[name]"

with open("Input/Names/invited_names.txt") as f1:
    content1 = f1.readlines()
with open("Input/Letters/starting_letter.txt") as f2:
    # print(name)
    content2 = f2.read()
    # print(content2)
    # print(content1)
for name in content1:
    name = name.strip()
    with open(f"Output/ReadyToSend/{name}_letter", "w") as f3:
        f3.write(content2.replace(PLACE_HOLDER, f"{name}"))
