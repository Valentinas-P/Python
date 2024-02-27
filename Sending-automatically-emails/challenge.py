import pandas
import smtplib
import random
import datetime as dt
##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

data = pandas.read_csv("birthdays.csv")
month_data = data["month"]
mom_name = data["name"][0]
day_data_mom = data["day"][0]
month_data_mom = data["month"][0]
brother_name = data["name"][1]
day_data_brother = data["day"][1]
month_data_brother = data["month"][1]


# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
current_day = now.day
current_month = now.month


with open("letter_templates/letter_1.txt") as first_letter:
    letter_a = first_letter.read()
with open("letter_templates/letter_2.txt") as second_letter:
    letter_b = second_letter.read()
with open("letter_templates/letter_3.txt") as third_letter:
    letter_c = third_letter.read()

all_letters = [letter_a, letter_b, letter_c]
random_letter = random.choice(all_letters)

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv


def send_email(person):
    person = random_letter.replace("[NAME]", person)

    MY_EMAIL = "example@gmail.com"
    PASSWORD = "notrealcode"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="example@gmail.com",
            msg=f"Subject: Happy birthday by your favourite person!\n\n{person}")
        connection.close()


if current_day == day_data_mom and current_month == month_data_mom:
    send_email(mom_name)

if current_day == day_data_brother and current_month == month_data_brother:
    send_email(brother_name)

