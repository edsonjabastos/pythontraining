import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# FileNotFound
# with open("data.txt") as file:
#     file.read()

# KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]

# IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text + 5)

# try:
#     file = open("nothing.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("nothing.txt", "w")
#     file.write("Something")
#     print("There was an error FileNotFoundError.")
# except KeyError as error_message:
#     content = file.read()
#     print(content, "KeyError")
# finally:
#     # raise TypeError("Ta tirando, né?!")
#     file.close()
#     print("File was closed.")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")
