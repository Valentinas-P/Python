from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client

account_sid = "#############################"
auth_token = "################################"


class NotificationManager:

    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_message(self, message):
        try:
            message = self.client.messages.create(
                body=message,
                from_="###############",
                to="###############"
            )
            print("SMS send successfully")
            print("Message SID: ", message.sid)
        except TwilioRestException as e:
            print("Failed to send SMS:", e.msg)
        except Exception as e:
            print("Failed to send SMS: ".str(e))
