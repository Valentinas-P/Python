import requests
from datetime import datetime
import smtplib

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()["iss_position"]
latitude = float(data["latitude"])
longitude = float(data["longitude"])

iss_position = (latitude, longitude)
print(iss_position)

MY_LAT = "#########"
MY_LONG = "########"

sunset_sunrise_params = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=sunset_sunrise_params)
response.raise_for_status()
data = response.json()["results"]
sunrise = int(data["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["sunset"].split("T")[1].split(":")[0])

sunrise_and_sunset = (sunrise, sunset)
print(sunrise_and_sunset)

time_now = datetime.now()

if time_now == sunset and latitude == MY_LAT and longitude == MY_LONG:
    print("yes it worked")
    my_email = "#################"
    password = "#################"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="########",
            msg=f"Subject:Lookup ISS above you!\n\nCurrent location: {latitude}, {longitude}"
        )
