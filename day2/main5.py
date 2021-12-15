# 🚨 Don't change the code below 👇
age = int(input("What is your current age?\n"))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age_left = 90 - age
age_in_months = age_left * 12
age_in_weeks =  age_left * 52
age_in_days = age_left * 365

# print(age_left, type(age_left))
# print(type(age))

print(f"You have {age_in_days} days, {age_in_weeks} weeks, and {age_in_months} months left.")