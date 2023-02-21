student_dict = {"student": ["Angela", "James", "Lily"], "score": [56, 76, 98]}
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

import pandas

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
a_df = pandas.read_csv("nato_phonetic_alphabet.csv")
print(a_df)
a_dict = {row.letter: row.code for (index, row) in a_df.iterrows()}
print(a_dict)
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# using = True

# while using:
#     u_input = input("Type a letter to see the code: ").upper()
#     print(u_input)
#     if u_input == "exit":
#         using = False
#     if u_input in a_dict:
#         print(a_dict[u_input])

u_input = input("Type a letter to see the code: ").upper()

output = [a_dict[letter] for letter in u_input]
print(output)
