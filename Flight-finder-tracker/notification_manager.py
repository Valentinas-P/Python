from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client

account_sid = "ACc16fe1101846aaff1c15906b464d7cbd"
auth_token = "b9d3a6cd27771df61559db6e88233b87"


class NotificationManager:

    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_message(self, message):
        try:
            message = self.client.messages.create(
                body=message,
                from_="+13159291951",
                to="+4407798720644"
            )
            print("SMS send successfully")
            print("Message SID: ", message.sid)
        except TwilioRestException as e:
            print("Failed to send SMS:", e.msg)
        except Exception as e:
            print("Failed to send SMS: ".str(e))
