from api_keys_secret import *
from twilio.rest import Client
from flight_data import FlightData


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self, lowest_flight: FlightData):
        self.lowest_flight = lowest_flight
        self.send_sms()

    def send_sms(self):
        # Send SMS for lowest flight
        client = Client(TWILIO_ID, TWILIO_KEY)
        message = client.messages.create(
            from_="+18888279180",
            body=f"Low price alert! Only ${self.lowest_flight.price} to fly from {self.lowest_flight.from_city} to "
                 f"{self.lowest_flight.to_city}, from {self.lowest_flight.depart} for {self.lowest_flight.nights} "
                 f"nights.",
            to=TWILIO_MYPHONE,
        )

        print(message.sid)
