import smtplib
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

my_email = "edsonjabastosx@gmail.com"
password = "Guglin0#"
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(
    from_addr=my_email,
    to_addrs="edsonjabastos@hotmail.com",
    msg="Hello!",
)
connection.close()
