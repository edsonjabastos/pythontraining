import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second
day_of_the_week = now.weekday()
# print(year, month, day, hour, minute, second, day_of_the_week)
print(day_of_the_week)
# print(type(year), year, type(now), now)

date_of_birth = dt.datetime(
    year=1994,
    month=6,
    day=10,
    hour=3,
)
# print(date_of_birth)
import smtplib
import os
from random import choice

os.chdir(os.path.dirname(os.path.abspath(__file__)))

my_email = "edsonjabastosx@gmail.com"
password = "password"
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(
    from_addr=my_email,
    to_addrs="edsonjabastos@hotmail.com",
    msg="Hello!",
)
connection.close()
password = ""
with open("quotes.txt", "r") as quotes_file:
    quotes = quotes_file.readlines()
    quotes = [item.strip() for item in quotes]
    # print(quotes)
random_quote = choice(quotes)
# print(random_quote)
message = f"""Subject:Hello!\n\n{random_quote}"""
print(message)
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="edsonjabastos@hotmail.com",
        msg=message,
    )
