import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")

names = names_string.split(", ")

# 🚨 Don't change the code above 👆
# Write your code below this line 👇

people_quantity = len(names)

dice = random.randint(0, people_quantity - 1)

print(f"{names[dice]} is going to buy the meal today!")

# edson, daiane, luiz, andre, matheus, varzea, polvora, minasgerais, brasil, peleopoldo <- example input
