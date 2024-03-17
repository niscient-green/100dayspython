import os
import time
import requests
from datetime import datetime
import smtplib

# Determine if the ISS is visible. Send email if so.

MY_LAT = 44.434791
MY_LONG = -72.272297
SENDER_EMAIL = "testhofmeister@gmail.com"
SENDER_PASSWORD = os.environ.get("GMAIL_TEST_PWD")
RECIPIENT_EMAIL = "testhofmeister@gmail.com"


# Determine location ------------------------------------------------------------------------------
def get_iss_position():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()

    iss_data_jsn = iss_response.json()

    iss_longitude_flt = float(iss_data_jsn["iss_position"]["longitude"])
    iss_latitude_flt = float(iss_data_jsn["iss_position"]["latitude"])

    return iss_latitude_flt, iss_longitude_flt


def is_iss_near(iss_position):
    if (iss_position[0] - 5) <= MY_LAT <= (iss_position[0] + 5) and (iss_position[1] - 5) <= MY_LONG <= (
            iss_position[1] + 5):
        return True
    else:
        return False


# Determine whether it is dark --------------------------------------------------------------------
def is_dark():
    # Get sunrise and sunset times
    dark_param_dct = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    dark_response = requests.get(url="https://api.sunrise-sunset.org/json", params=dark_param_dct)
    dark_response.raise_for_status()
    dark_jsn = dark_response.json()

    # Get sunrise hour
    sunrise_str = dark_jsn["results"]["sunrise"]
    sunrise_lst = sunrise_str.split("T")[1].split(":")
    sunrise_hour_int = int(sunrise_lst[0])

    # Get sunset hour
    sunset_str = dark_jsn["results"]["sunrise"]
    sunset_lst = sunset_str.split("T")[1].split(":")
    sunset_hour_int = int(sunset_lst[0])

    # See if it is currently dark
    now_hour_int = datetime.now().hour
    if now_hour_int >= sunset_hour_int or now_hour_int <= sunrise_hour_int:
        return True
    else:
        return False


# Send email --------------------------------------------------------------------------------------
def send_email(iss_position_tup):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL, password=SENDER_PASSWORD)
        connection.sendmail(
            from_addr=SENDER_EMAIL,
            to_addrs=RECIPIENT_EMAIL,
            msg="Subject: Look up! ISS above."
                f"\n\nThe ISS is currently above your position at\nlatitude: {iss_position_tup[0]}\nlongitude: "
                f"{iss_position_tup[1]}")


# Main program loop -------------------------------------------------------------------------------
while True:
    iss_position_tup = get_iss_position()
    if is_iss_near(iss_position_tup) and is_dark():
        send_email(iss_position_tup)
        print("Sent email!")
    else:
        print("ISS not near or it is day time.")
    time.sleep(60)
