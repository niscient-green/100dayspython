# Scratch file to start building a rain alert application
import os

import requests
from twilio.rest import Client

ow_api_key = os.environ.get("OW_API_KEY")
ow_5day_endpoint = "http://api.openweathermap.org/data/2.5/forecast"
account_sid = os.environ.get("OW_ACCOUNT")
auth_token = os.environ.get("OW_AUTH")

MY_LAT = 44.434791
MY_LONG = -72.272297

ow_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": ow_api_key,
    "cnt": 4,
}

ow_response = requests.get(url=ow_5day_endpoint, params=ow_params)
ow_response.raise_for_status()
weather_data = ow_response.json()

# If weather code < 600, bring umbrella
will_rain = False
for forecast in weather_data["list"]:
    for weather_event in forecast["weather"]:
        id = weather_event["id"]
        if id < 600:
            will_rain = True

if will_rain:
    # Send an SMS through Twilio
    client = Client(account_sid, auth_token)

    message = client.messages.create(
      from_="+18888279180",
      body="Bring an umbrella ☔",
      to="+13037473448",
    )

    print(message.sid)