from api_keys_secret import *
import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        # Set API endpoint and headers
        self.sheety_prices_endpoint = ("https://api.sheety.co/c988319a87adb183ebf1ec0ecc638410/100DaypyFlightDeals/"
                                       "prices")
        self.sheety_users_endpoint = ("https://api.sheety.co/c988319a87adb183ebf1ec0ecc638410/100DaypyFlightDeals/"
                                      "users")
        self.sheety_headers = {
            'Authorization': SHEETY_TOKEN,
        }

    def get_prices(self) -> list:
        # Get all price data from GSheet, return list of data from prices worksheet
        sheety_response = requests.get(url=self.sheety_prices_endpoint, headers=self.sheety_headers)
        sheety_response.raise_for_status()
        return sheety_response.json()['prices']

    def update_prices(self, row: dict):
        # Update one row in GSheet
        sheety_put_endpoint = self.sheety_prices_endpoint + '/' + str(row['id'])
        sheety_params = {
            'price': row
        }

        # Call the API
        sheety_response = requests.put(url=sheety_put_endpoint, json=sheety_params, headers=self.sheety_headers)
        print(sheety_response.text)
        sheety_response.raise_for_status()

    def get_users(self) -> list:
        # Get all user data from GSheet, return list of users
        sheety_response = requests.get(url=self.sheety_users_endpoint, headers=self.sheety_headers)
        sheety_response.raise_for_status()
        return sheety_response.json()['users']