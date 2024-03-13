# Send motivational quote email on certain day

# Import packages
import smtplib
import datetime as dt
import random

# Set constants, globals
my_email = "testhofmeister@gmail.com"
my_password = "rntqyjnhuxvsootu"

# Get current day of the week
now_dtm = dt.datetime.now()
week_day_str = now_dtm.weekday()

# Create list of [quotes, author]
with open("quotes.txt", mode="r") as quote_fil:
    quote_lst = quote_fil.readlines()

# Pull a random quote
quote_str = random.choice(quote_lst)


# Open email connection, send test email
with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail( 
        from_addr=my_email,
        to_addrs="nick@niscient.com",
        msg="Subject: Hi!"
            f"\n\n{quote_str}")
