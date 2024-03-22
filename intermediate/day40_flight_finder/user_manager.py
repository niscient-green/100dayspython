from api_keys_secret import *
import requests


class UserManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        # Set API endpoint and headers
        self.sheety_endpoint = "https://api.sheety.co/c988319a87adb183ebf1ec0ecc638410/100DaypyFlightDeals/users"
        self.sheety_headers = {
            'Authorization': SHEETY_TOKEN,
            'Content-Type': 'application/json',
        }

    def get_gsheet(self) -> list:
        # Get all data from GSheet, return list of data from prices worksheet
        sheety_response = requests.get(url=self.sheety_endpoint, headers=self.sheety_headers)
        sheety_response.raise_for_status()
        return sheety_response.json()['prices']

    def new_user(self, ):
        # Ask user for their information
        print("Welcome to Niscient's Flight Club!")
        print("We find the best deals and email you.")
        fname = input("What is your first name? ").title()
        lname = input("What is your last name? ").title()
        email = input("What is your email address? ")
        email_confirm = input("Please confirm your email address: ")

        # Confirm email matches
        if email != email_confirm:
            print("Error: emails do not match.")
            return False

        # Update user sheet
        sheety_endpoint = self.sheety_endpoint
        sheety_params = {
            'user': {
                'firstName': fname,
                'lastName': lname,
                'email': email,
            }
        }

        # Call the API
        sheety_response = requests.post(url=sheety_endpoint, json=sheety_params, headers=self.sheety_headers)
        print(sheety_response.text)
        sheety_response.raise_for_status()

        # Notify user
        print("Welcome to the club.")

user = UserManager()
user.new_user()