import requests
from _datetime import datetime as dt

today = dt.now()


USERNAME = "applyhere"
TOKEN = "applyhere"
GRAPH_ID = "applyhere"

pixela_endpoint = "https://pixe.la/v1/users"

parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=parameters)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Gym Graph",
    "unit": "calory",
    "type": "float",
    "color": "shibafu",
    "publishOptionalData": "true",

}

headers = {
    "X-USER-TOKEN": TOKEN,
}

post_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "380",
}

post_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

# response = requests.post(url=post_endpoint, json=post_config, headers=headers)
# print(response.text)

put_config = {
    "quantity": "150",
}

update_endpoint = f"{post_endpoint}/20230530"

# response = requests.put(url=update_endpoint, json=put_config, headers=headers)
# print(response.text)

delete_endpoint = f"{update_endpoint}"

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
