import requests
from pprint import pprint

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/76a943f9726caa0b45b86552cf1e0030/flightDeal/prices"


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_sheet_iata_codes(self):
        global city
        for city in self.destination_data:
            payload = {
                'price': {
                    'iataCode': city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}", json=payload)
            print(response.text)
