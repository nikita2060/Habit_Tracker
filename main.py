import requests
from datetime import datetime
import os

today = datetime.now()
date = today.strftime("%Y%m%d")

USERNAME = os.environ.get("PIXELA_USER")  # using environment variables is appreciated for security reasons
TOKEN = os.environ.get("PIXELA_TOKEN")
headers = {
    "X-USER-TOKEN": TOKEN
}

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
create_user_endpoint = "https://pixe.la/v1/users"


response = requests.post(url=create_user_endpoint, json=user_params, headers=headers)
print(response.json())

graph_params = {
    "id": "graph1",
    "name": "Coding graph ",
    "unit": "Program",
    "type": "int",
    "color": "ajisai"
}
create_graph_endpoint = f"{create_user_endpoint}/{USERNAME}/graphs"


# response = requests.post(url=create_graph_endpoint, json=graph_params, headers=headers)

create_pixel_endpoint = f"{create_graph_endpoint}/graph1"
# print(create_pixel_endpoint)
pixel_params = {
    "date": date,
    "quantity": "1"
}
# response = requests.post(url=create_pixel_endpoint, json=pixel_params, headers=headers)
# print(response.text)

update_pixel_endpoint = f"{create_pixel_endpoint}/{date}"
pixel_data = {
    "quantity": "2"
}
# response = requests.put(url=update_pixel_endpoint, json=pixel_data, headers=headers)
# print(update_pixel_endpoint)
# print(response.text)