from api_keys_secret import *
from twilio.rest import Client
from flight_data import FlightData
import smtplib


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self, lowest_flight: FlightData, max_stops: int, via_city: str):
        self.lowest_flight = lowest_flight
        self.client = Client(TWILIO_ID, TWILIO_KEY)
        self.max_stops = max_stops
        self.via_city = via_city

    def send_sms(self):
        # Create message notification body
        message_body = (f"Low price alert! Only ${self.lowest_flight.price} to fly from {self.lowest_flight.from_city} "
                        f"to {self.lowest_flight.to_city}, from {self.lowest_flight.depart} for "
                        f"{self.lowest_flight.nights} nights.")
        # If there are stopovers, add a note
        if self.max_stops != 0:
            message_body += f"\n\nFlight has {self.max_stops} stop over, via {self.via_city}."

        # Send the SMS
        message = self.client.messages.create(
            from_="+18888279180",
            body=message_body,
            to=TWILIO_MYPHONE,
        )

        print(message.sid)

    def send_emails(self, users: list):
        # Create email notification body
        message_body = (f"Low price alert! Only ${self.lowest_flight.price} to fly from {self.lowest_flight.from_city} "
                        f"to {self.lowest_flight.to_city}, from {self.lowest_flight.depart} for "
                        f"{self.lowest_flight.nights} nights.")
        # If there are stopovers, add a note
        if self.max_stops != 0:
            message_body += f"\n\nFlight has {self.max_stops} stop over, via {self.via_city}."

        for user in users:
            recipient_email = user['email']
            try:
                with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                    connection.starttls()
                    connection.login(user=SENDER_EMAIL, password=SENDER_PASSWORD)
                    connection.sendmail(
                        from_addr=SENDER_EMAIL,
                        to_addrs=recipient_email,
                        msg="Subject: Niscient's Flight Club Alert"
                            f"{message_body}"
                    )
            except smtplib.SMTPRecipientsRefused:
                print("Error: recipient address not valid")
