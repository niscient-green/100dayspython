# Send birthday wishes email

# Import packages
import smtplib
import datetime as dt

# # Set constants, globals
# my_email = "testhofmeister@gmail.com"
# my_password = "rntqyjnhuxvsootu"
#
# # Open email connection, send test email
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection
#     connection.starttls()
#     connection.login(user=my_email, password=my_password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="nick@niscient.com",
#         msg="Subject: Hi!"
#             "\n\nJust wishing you a good day.")

now_dtm = dt.datetime.now()
year_int = now_dtm.year
month_int = now_dtm.month
week_day_str = now_dtm.weekday()
date_of_birth_dtm = dt.datetime(year=1978, month=6, day=5)

