##################### Extra Hard Starting Project ######################
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

from random import choice, randint
import smtplib
import datetime as dt
import pandas as pd

# 1. Update the birthdays.csv ✔
birthdays = pd.read_csv("birthdays.csv")

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
today = now.day

if today in birthdays.day.tolist():
    with open(f"letter_templates/letter_{randint(1, 3)}.txt") as letter_file:
        letter = letter_file.read()
        letter = letter.replace("[NAME]", birthdays.name[birthdays.day == today][0])
        print(letter)
        # print(birthdays.name[birthdays.day == today][0])
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
my_email = "edsonjabastosx@gmail.com"
password = "????"
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="edsonjabastos@hotmail.com",
        msg=letter,
    )