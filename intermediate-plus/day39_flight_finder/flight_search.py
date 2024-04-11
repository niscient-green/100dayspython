import datetime

import requests
from api_keys_secret import *
import datetime as dt


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def __init__(self):
        self.tequila_endpoint = "https://api.tequila.kiwi.com/"
        self.tequila_headers = {
            'apikey': TEQUILA_KEY,
            'Content-Type': 'application/json',
        }

    def get_iata(self, city: str) -> str:
        # Search for IATA code
        locations_endpoint = self.tequila_endpoint + 'locations/query'
        tequila_params = {
            'term': city
        }
        tequila_response = requests.get(url=locations_endpoint, params=tequila_params, headers=self.tequila_headers)
        tequila_response.raise_for_status()
        return tequila_response.json()['locations'][0]['code']

    def find_flights(self, from_code: str, to_code: str, lowest_price: int) -> list:
        # Find flights from from_code city to to_code city
        tomorrow = dt.date.today() + datetime.timedelta(days=1)
        tomorrow_str = tomorrow.strftime('%d/%m/%Y')
        end_date = dt.date.today() + datetime.timedelta(days=180)
        end_date_str = end_date.strftime('%d/%m/%Y')

        search_endpoint = self.tequila_endpoint + 'v2/search'
        tequila_params = {
            'fly_from': from_code,
            'fly_to': to_code,
            'date_from': tomorrow_str,
            'date_to': end_date_str,
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 28,
            'curr': 'USD',
            'max_stopovers': 0,
            'price_to': lowest_price,
        }
        tequila_response = requests.get(url=search_endpoint, params=tequila_params, headers=self.tequila_headers)
        tequila_response.raise_for_status()
        return tequila_response.json()['data']
