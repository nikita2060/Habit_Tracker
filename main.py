import requests
from datetime import datetime
import os


# program written in modular form is more readable and optimum
def create_user(username, token):
    headers = {"X-USER-TOKEN": TOKEN}
    user_params = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }
    create_user_endpoint = "https://pixe.la/v1/users"
    response = requests.post(url=create_user_endpoint, json=user_params, headers=headers)
    print(response.json())


def create_graph(username, token):
    headers = {"X-USER-TOKEN": TOKEN}
    graph_params = {
        "id": "graph1",
        "name": "Coding graph ",
        "unit": "Program",
        "type": "int",
        "color": "ajisai"
    }
    create_graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs"
    response = requests.post(url=create_graph_endpoint, json=graph_params, headers=headers)
    print(response.json())


def create_pixel(username, token, today_date, input_quantity):
    headers = {"X-USER-TOKEN": TOKEN}
    create_pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/graph1"
    pixel_params = {
        "date": today_date,
        "quantity": input_quantity
    }
    response = requests.post(url=create_pixel_endpoint, json=pixel_params, headers=headers)
    print(response.text)


def update_pixel(username, token, today_date, input_quantity):
    headers = {"X-USER-TOKEN": TOKEN}
    update_pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/graph1/{date}"
    pixel_data = {
        "quantity": input_quantity
    }
    response = requests.put(url=update_pixel_endpoint, json=pixel_data, headers=headers)
    print(response.text)


if __name__ == "__main__":
    today = datetime.now()
    date = today.strftime("%Y%m%d")
    USERNAME = os.environ.get("PIXELA_USER")  # using environment variables is appreciated for security reasons
    TOKEN = os.environ.get("PIXELA_TOKEN")
    quantity = input("How many programs did you do today?")   # asking user input for customization

    print(create_user(USERNAME, TOKEN))
    print(create_graph(USERNAME, TOKEN))
    print(create_pixel(USERNAME, TOKEN, date, quantity))
    print(update_pixel(USERNAME, TOKEN, date, quantity))
