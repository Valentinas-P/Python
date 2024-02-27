import smtplib

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day = now.day
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=2000, month=2, day=14)
# print(date_of_birth)

import random
import datetime as dt

with open("quotes.txt") as file:
    data = file.readlines()

randomise_quotes = random.choice(data)

day = dt.datetime.now()
current_day = day.weekday()

if current_day == 0:
    MY_EMAIL = "fakeemail@gmail.com"
    PASSWORD = "znpqhmtvbr"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="youremail@gmail.com",
            msg=f"Subject: Monday motivational quotes by Val:)\n\n{randomise_quotes}")
        connection.close()






