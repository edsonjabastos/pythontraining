from twilio.rest import Client
import os
import requests
MY_LAT = -19.6201
MY_LONG = -44.0438
# Download the helper library from https://www.twilio.com/docs/python/install
# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "???"
auth_token = "???"
api_key = os.environ.get("OWM_API_KEY")
# parameters = {
#     # "lat": MY_LAT,
#     # "lon": MY_LONG,
#     "q": "Belo Horizonte,BR",
#     "appid": "????"
# }

# response = requests.get(
#     url="https://api.openweathermap.org/data/2.5/weather", params=parameters)
# response.raise_for_status()
# data = response.json()
# print(data)

parameters = {
    "lat": -33.3339,
    "lon": -60.2108,
    # "q": "Belo Horizonte,BR",
    # "exclude": "alerts",
    "appid": api_key,
    "exclude": "current,minutely,daily"
}
response = requests.get(
    url="https://api.openweathermap.org/data/2.8/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    print("bring an umbrella.")
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Vai chover rapaz, fica esperto ☂️ 🌂 ☔ 🫠😵‍💫 🕳️ 👁️‍🗨️ 💢 💥 💫 💫 💫 👻 👽  ",
        from_="+14066413323",
        to="+5531984592603"
    )
    print(message.status)
# for i in range(0,13):
#     if data0["hourly"][i]["weather"][0]["id"] < 700:
#         print("Vai chover negadis!")
#         print(i)
