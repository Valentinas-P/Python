import requests
from datetime import datetime
import os


today = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

ask = input("Tell me which exercises you did: ")

parameters = {
    "query": f"{ask}",
    "gender": "male",
    "weight_kg": "70",
    "height_cm": "180",
    "age": "23",
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

response = requests.post(f"{exercise_endpoint}", headers=headers, json=parameters)
data = response.json()
print(data)

sheety_exercise_endpoint = os.environ.get("sheety_exercise_endpoint")

workout_header = {
    "method": "GET",
    "headers": headers,
}

USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")

for workout in data["exercises"]:
    print(workout)
    sheet_data = {
        "workout": {
            "date": today,
            "time": now_time,
            "exercise": workout["name"].title(),
            "duration": workout["duration_min"],
            "calories": workout["nf_calories"],
        }
    }

    get_data = requests.post(sheety_exercise_endpoint, json=sheet_data, auth=(USERNAME, PASSWORD))
    print(get_data.text)
