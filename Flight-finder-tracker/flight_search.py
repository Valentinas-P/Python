import requests
from flight_data import FlightData
from datetime import datetime

TEQUILA_API_KEY = "##############################"
TEQUILA_ENDPOINT = "############################"


class FlightSearch:

    def get_iata_code(self, city):
        location_endpoint = f"{TEQUILA_ENDPOINT}"
        flight_params = {
            'term': city,
            'location_types': "city",
        }

        headers = {
            'apikey': TEQUILA_API_KEY,
        }

        response = requests.get(url=location_endpoint, params=flight_params, headers=headers)
        results = response.json()['locations']
        iata_code = results[0]['code']
        return iata_code

    def check_flights(self, origin, destination, date_from, date_to):

        headers = {
            'apikey': TEQUILA_API_KEY,
            'Content-Type': 'application/json',
        }

        date_from_obj = datetime.strptime(date_from, "%d-%m-%Y")
        date_to_obj = datetime.strptime(date_to, "%d-%m-%Y")

        query = {
            'fly_from': origin,
            'fly_to': destination,
            'date_from': date_from_obj.strftime("%Y-%m-%d"),
            'date_to': date_to_obj.strftime("%Y-%m-%d"),
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 28,
            'one_for_city': 1,
            'flight_type': 'round',
            "curr": "GBP",
        }

        response = requests.get(f"{TEQUILA_ENDPOINT}/v2/search", params=query, headers=headers)

        try:
            data = response.json()['data'][0]
        except IndexError:
            print(f"No flights found for {destination}")
            return None

        flight_data = FlightData(
            price=data['price'],
            origin_city=data['route'][0]['cityFrom'],
            origin_airport=data['route'][0]['flyFrom'],
            destination_city=data['route'][0]['cityTo'],
            destination_airport=data['route'][0]['flyTo'],
            out_date=data['route'][0]['local_departure'].split("T")[0],
            return_date=data['route'][1]['local_departure'].split("T")[0],
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data
