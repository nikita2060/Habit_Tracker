import requests
from datetime import datetime

today = datetime.now()
date = today.strftime("%Y%m%d")

USERNAME = "nikky"
TOKEN = "qwertyuiop"

user_params = {
    "token": "qwertyuiop",
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
create_user_endpoint = "https://pixe.la/v1/users"


# response = requests.post(url=create_user_endpoint, json=user_params)
# print(response.json())

graph_params = {
    "id": "graph1",
    "name": "Coding graph ",
    "unit": "Program",
    "type": "int",
    "color": "ajisai"
}
create_graph_endpoint = f"{create_user_endpoint}/{USERNAME}/graphs"

headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=create_graph_endpoint, json=graph_params, headers=headers)

create_pixel_endpoint = f"{create_user_endpoint}/{USERNAME}/graphs/graph1"
pixel_params = {
    "date": date,
    "quantity": "1"
}
response = requests.post(url=create_pixel_endpoint, json=pixel_params, headers=headers)
print(response.text)