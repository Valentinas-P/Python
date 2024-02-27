import requests
from twilio.rest import Client


LATITUDE = 51.507351
LONGITUDE = -0.127758
API_KEY = ""
account_sid = ""
auth_token = ""

parameters = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": API_KEY,
    "exclude": "current,minutely,daily,alerts"
}

response = requests.get("https://api.openweathermap.org/data/2.8/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
print(weather_data)
next_12_hour_condition = weather_data["hourly"][0:12]
print(next_12_hour_condition)

list_conditions = [each_id["weather"][0]["id"] for each_id in next_12_hour_condition]

results = [cast for cast in list_conditions if cast < 700]
if results:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☂️",
        from_="yournumber",
        to="yournumber"
    )
    print(message.status)



