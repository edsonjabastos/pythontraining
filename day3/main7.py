# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# my resolution is ok !

names12_lower = (name1 + name2).lower()

names12_lower_count_t = names12_lower.count("t")
names12_lower_count_r = names12_lower.count("r")
names12_lower_count_u = names12_lower.count("u")
names12_lower_count_e = names12_lower.count("e")
true_in_names_count = (
    names12_lower_count_t
    + names12_lower_count_r
    + names12_lower_count_u
    + names12_lower_count_e
)
names12_lower_count_l = names12_lower.count("l")
names12_lower_count_o = names12_lower.count("o")
names12_lower_count_v = names12_lower.count("v")
names12_lower_count_e = names12_lower.count("e")
love_in_names_count = (
    names12_lower_count_l
    + names12_lower_count_o
    + names12_lower_count_v
    + names12_lower_count_e
)
true_in_names_count_str = str(true_in_names_count)
love_in_names_count_str = str(love_in_names_count)
final_count = int(true_in_names_count_str + love_in_names_count_str)

if final_count < 10 and final_count > 90:
    print(f"Your score is {final_count}, you go together like coke and mentos.")
elif final_count >= 40 and final_count <= 50:
    print(f"Your score is {final_count}, you are alright together.")
else:
    print(f"Your score is {final_count}.")

# teacher resolution

# combined_names = name1 + name2
# lower_names = combined_names.lower()
# t = lower_names.count("t")
# r = lower_names.count("r")
# u = lower_names.count("u")
# e = lower_names.count("e")
# first_digit = t + r + u + e

# l = lower_names.count("l")
# o = lower_names.count("o")
# v = lower_names.count("v")
# e = lower_names.count("e")
# second_digit = l + o + v + e

# score = int(str(first_digit) + str(second_digit))

# if (score < 10) or (score > 90):
#   print(f"Your score is {score}, you go together like coke and mentos.")
# elif (score >= 40) and (score <= 50):
#   print(f"Your score is {score}, you are alright together.")
# else:
#   print(f"Your score is {score}.")