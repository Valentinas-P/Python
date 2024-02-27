#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "LON"

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_iata_code(row['city'])
        data_manager.destination_data = sheet_data
        data_manager.update_sheet_iata_codes()

    now = datetime.now()

    tomorrow = now + timedelta(days=1)
    six_months_from_today = datetime.now() + timedelta(days=(6*30))

    for destination in sheet_data:
        flight = flight_search.check_flights(
            ORIGIN_CITY_IATA,
            destination['iataCode'],
            date_from=tomorrow,
            date_to=six_months_from_today
        )

        lowest_price = row['lowestPrice']

        if flight.price < destination['lowestPrice']:
            notification_manager.send_message(
                message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport}"
                        f" to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date}"
                        f" to {flight.return_date}."
            )