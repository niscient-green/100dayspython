import requests
import datetime as dt
from api_keys_secret import *

# Set globals, constants -----------------------------------------------------------------------------------------------
pixela_headers = {
    "X-USER-TOKEN": PIXELA_ID
}
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ID = "graph001"
PIXELA_GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs/{GRAPH_ID}"

# Create new account - one time ----------------------------------------------------------------------------------------
# pixela_params = {
#     "token": PIXELA_ID,
#     "username": PIXELA_USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }
#
# pixela_response = requests.post(url=PIXELA_ENDPOINT, json=pixela_params)
# print(pixela_response.text)


# Create a new graph on Pixela -----------------------------------------------------------------------------------------
# pixela_params = {
#     "id": "graph001",
#     "name": "100 Days Python",
#     "unit": "days",
#     "type": "int",
#     "color": "ajisai",
# }
#
#
# pixela_response = requests.post(url=PIXELA_GRAPH_ENDPOINT, json=pixela_params, headers=pixela_headers)
# print(pixela_response.text)


# Post a pixel ---------------------------------------------------------------------------------------------------------
# today_dt = dt.date.today()
# today_str = today_dt.strftime("%Y%m%d")
# pixela_params = {
#     "date": "20240318",
#     "quantity": "2",
# }
# pixela_response = requests.post(url=PIXELA_GRAPH_ENDPOINT, json=pixela_params, headers=pixela_headers)
# pixela_response.raise_for_status()
# print(pixela_response.text)


# Update a pixel -------------------------------------------------------------------------------------------------------
# PIXELA_UPDATE_ENDPOINT = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs/{GRAPH_ID}/20240318"
#
# pixela_params = {
#     "quantity": "10",
# }
# pixela_response = requests.put(url=PIXELA_UPDATE_ENDPOINT, json=pixela_params, headers=pixela_headers)
# pixela_response.raise_for_status()
# print(pixela_response.text)

# Delete a pixel -------------------------------------------------------------------------------------------------------
PIXELA_DELETE_ENDPOINT = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs/{GRAPH_ID}/20240318"

pixela_params = {
}
pixela_response = requests.delete(url=PIXELA_DELETE_ENDPOINT, json=pixela_params, headers=pixela_headers)
pixela_response.raise_for_status()
print(pixela_response.text)