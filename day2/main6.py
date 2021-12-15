# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇

print("Welcome to the tip calculator.\n")
bill_total = float(input("What was the total bill? \n$"))
# print(bill_total)
tip_percentage = int(
    input("What percentage tip would you like to give? 10, 12, or 15?\n")
)
tip_percentage /= 100
# print(tip_percentage)
people_to_pay = int(input("How many people to split the bill?\n"))
# print(people_to_pay)
bill_plus_tip = (tip_percentage + 1) * bill_total
# print(bill_plus_tip)
splited_bill = bill_plus_tip / people_to_pay
# print(splited_bill)
final_amount = round(splited_bill, 2)
final_amount = "{:.2f}".format(splited_bill)
print(f"Each person should pay: ${final_amount}")
