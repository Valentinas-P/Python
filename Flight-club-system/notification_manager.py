from twilio.rest import Client
import smtplib

TWILIO_SID = "ACc16fe1101846aaff1c15906b464d7cbd"
TWILIO_AUTH_TOKEN = "b9d3a6cd27771df61559db6e88233b87"
TWILIO_VIRTUAL_NUMBER = "+13159291951"
TWILIO_VERIFIED_NUMBER = "+4407798720644"
MY_EMAIL = "pythonchr@gmail.com"
PASSWORD = "znpqhmtvbrbnucnz"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self, emails, message):
        with smtplib.SMTP("smpt.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )

