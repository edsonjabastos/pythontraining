import requests
import datetime

USERNAME = "???"
TOKEN = "???"
GRAPHID = "???"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Create account
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": GRAPHID,
    "name": "Code activity",
    "unit": "minutes",
    "type": "int",
    "color": "kuro"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# Create graph
# response = requests.post(
#     url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

post_pixel_endpoint = f"{graph_endpoint}/{GRAPHID}"
# today = str(datetime.date.today()).replace("-", "")
today = datetime.datetime.now()
yesterday = (today - datetime.timedelta(days=1)).strftime("%Y%m%d")
post_pixel_params = {
    "date": yesterday,
    "quantity": "120"
}

# Post pixel
# response = requests.post(url=post_pixel_endpoint,
#                          json=post_pixel_params, headers=headers)
# print(response.text)
# print(today, yesterday)

update_pixel_endpoint = f"{post_pixel_endpoint}/{yesterday}"

update_pixel_params = {
    "quantity": "150"
}
# Update pixel
# response = requests.put(url=update_pixel_endpoint,
#                         json=update_pixel_params, headers=headers)
# print(response.text)
# print(update_pixel_endpoint)

# Delete pixel
response = requests.delete(url=update_pixel_endpoint, headers=headers)
