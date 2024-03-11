import smtplib
import datetime as df
import pandas
import random

my_email = "#################"
password = "#################"

now = df.datetime.now()
year = now.year
month = now.month
day = now.day
current_fully_date = month, day

data = pandas.read_csv("birthdays.csv")

# 1. Update the birthdays.csv

birthdays_dict = {(row.month, row.day): f"{row['name']},{row['email']},{row['year']}," \
                                        f"{row['month']},{row['day']}" for (_, row) in data.iterrows()}

# 2. Check if today matches a birthday in the birthdays.csv
if current_fully_date in birthdays_dict:
    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's
    # actual name from birthdays.csv
    birthday_person = birthdays_dict[current_fully_date]
    name = birthday_person.split(',')[0]
    letter_picked = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(letter_picked) as letter_file:
        contents = letter_file.read()
        completed_letter = contents.replace("[NAME]", name)
    # 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="###########",
            msg=f"Subject:Birthday wish to {name} from ####\n\n{completed_letter}"
        )
    print("Sent")
