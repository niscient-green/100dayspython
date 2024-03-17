# Send motivational quote email on certain day
import os
# Import packages
import smtplib
import datetime as dt
import random

# Set constants, globals
MY_EMAIL = "testhofmeister@gmail.com"
MY_PASSWORD = os.environ.get("GMAIL_TEST_PWD")
SEND_DAY_INT = 2

# Get current day of the week
now_dtm = dt.datetime.now()
week_day_int = now_dtm.weekday()

# Check if today is the day for sending email
if week_day_int == SEND_DAY_INT:
    # Create list of [quotes, author]
    with open("quotes.txt", mode="r") as quote_fil:
        quote_lst = quote_fil.readlines()

    # Pull a random quote
    quote_str = random.choice(quote_lst)

    # Open email connection, send test email
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="testhofmeister@gmail.com",
            msg="Subject: Motivation"
                f"\n\n{quote_str}")
