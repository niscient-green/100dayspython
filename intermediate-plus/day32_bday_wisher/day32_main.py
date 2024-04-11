# Send birthday wishes email
import os
# Import packages ---------------------------------------------------------------------------------
import smtplib
import datetime as dt
import pandas as pd
import random

# Set constants, globals --------------------------------------------------------------------------
MY_EMAIL = TESTEMAIL
MY_PASSWORD = os.environ.get("GMAIL_TEST_PWD")
PLACEHOLDER = "[NAME]"


# Handle email ------------------------------------------------------------------------------------
def send_email(named_letter_lst, match_dct):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=match_dct["email"],
            msg="Subject: Happy birthday!"
                f"\n\n{''.join(named_letter_lst)}")


# Handle dates ------------------------------------------------------------------------------------
def get_today():
    now_dtm = dt.datetime.now()
    month_int = now_dtm.month
    day_int = now_dtm.day
    return month_int, day_int


def compare_dates(today_tup, birthdays_dct):
    match_dct = {}
    for row in birthdays_dct:
        if today_tup[0] == birthdays_dct[row]["month"] and today_tup[1] == birthdays_dct[row]["day"]:
            match_dct = birthdays_dct[row]
    return match_dct


# Handle files  -----------------------------------------------------------------------------------
def get_letter():
    which_letter_str = str(random.randint(1, 3))
    with open(f"letter_templates/letter_{which_letter_str}.txt") as letter_fil:
        letter_lst = letter_fil.readlines()
    return letter_lst


def get_birthdays():
    birthdays_dfr = pd.read_csv("birthdays.csv")
    birthdays_dct = birthdays_dfr.to_dict(orient="index")
    return birthdays_dct


def update_letter(letter_lst, match_dct):
    letter_lst[0] = letter_lst[0].replace(PLACEHOLDER, match_dct["name"])
    return letter_lst


# Main loop  --------------------------------------------------------------------------------------

# Look for birthdays that are today
today_tup = get_today()
birthdays_dct = get_birthdays()
match_dct = compare_dates(today_tup=today_tup, birthdays_dct=birthdays_dct)

# If a matching birthday found, get a random letter, modify it, send it. Otherwise, do nothing.
if match_dct != {}:
    letter_lst = get_letter()
    named_letter_lst = update_letter(letter_lst, match_dct)
    send_email(named_letter_lst=named_letter_lst, match_dct=match_dct)
    print("INFO: Sent birthday email.")
else:
    print("INFO: Found no matching birthday.")
