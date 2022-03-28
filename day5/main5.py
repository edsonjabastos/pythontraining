#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
generated_password = ""

for char in range(0, nr_letters):
    generated_password += random.choice(letters)

for symbol in range(0, nr_symbols):
    generated_password += random.choice(symbols)

for number in range(0, nr_numbers):
    generated_password += random.choice(numbers)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

list_to_shuffle = list(generated_password)
random.shuffle(list_to_shuffle)
suffled_password = ''.join(list_to_shuffle)

print(f"Here is your password => {suffled_password}")

a = generated_password.count("a")
z = generated_password.count("Z")
zero = generated_password.count("0")
nine = generated_password.count("9")
exclamation = generated_password.count("!")
plus = generated_password.count("+")

print(a, z, zero, nine, exclamation, plus)