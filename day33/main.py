import requests
import smtplib
import time
from datetime import datetime

MY_LAT = -19.6201
MY_LONG = -44.0438
MY_EMAIL = "edsonjabastosx@gmail.com"
MY_PASS = "????"


def is_iss_overhead():

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG-5:
        print("ISS is near!")
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }
    response = requests.get(
        url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    now = datetime.now()
    hour = now.hour
    if hour >= sunset or hour <= sunrise:
        print("!s night!")
        return True


while True:
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASS)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="edsonjabastos@hotmail.com",
                msg="Subject:ISS is near!\n\nLook up to see ISS 🛰️.",
            )
    time.sleep(60)
