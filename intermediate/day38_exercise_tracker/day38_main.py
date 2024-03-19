# This app collects exercise data, determines calories burned, stores in Google Sheet
from api_keys_secret import *
import requests
import datetime as dt


# Set globals, constants -----------------------------------------------------------------------------------------------
MY_GENDER = "male"
MY_WEIGHT_KG = 95
MY_HEIGHT_CM = 182
MY_AGE = 45


# Ask user for input ---------------------------------------------------------------------------------------------------
def get_exercise() -> str:
    return input("What exercise did you complete? ")


# Find exercise match, get calories ------------------------------------------------------------------------------------
def get_nix_data() -> dict:
    nix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
    nix_headers = {
        "x-app-id": NIX_APPID,
        "x-app-key": NIX_KEY,
    }
    nix_params = {
        "query": get_exercise(),
        "gender": MY_GENDER,
        "weight_kg": MY_WEIGHT_KG,
        "height_cm": MY_HEIGHT_CM,
        "age": MY_AGE,
    }
    nix_response = requests.post(url=nix_endpoint, data=nix_params, headers=nix_headers)
    print(nix_response.text)
    nix_response.raise_for_status()
    nix_data = nix_response.json()["exercises"][0]
    data = {
        "name": nix_data["name"],
        "duration": str(nix_data["duration_min"]),
        "calories": str(nix_data["nf_calories"]),
    }
    return data


# Store workout in Google Sheet ----------------------------------------------------------------------------------------
def current_datetime() -> (str, str):
    today_str = dt.date.today().strftime("%Y-%m-%d")
    now_str = dt.datetime.now().strftime("%H:%M")
    return today_str, now_str


def write_gsheet_row():
    # Set API endpoint and headers
    sheety_endpoint = "https://api.sheety.co/c988319a87adb183ebf1ec0ecc638410/100DaypyMyWorkouts/workouts"
    sheety_headers = {
        "Authorization": "Bearer fubamorswfyubjmarositemaoriesgaorisemtaroistm",
        "Content-Type": "application/json",
    }

    # Set API params using data from datetime and nix
    data = get_nix_data()
    today_str, now_str = current_datetime()
    sheety_params = {
        "workout": {
            "date": today_str,
            "time": now_str,
            "exercise": data["name"],
            "duration": data["duration"],
            "calories": data["calories"],
        }
    }

    # Call the API
    sheety_response = requests.post(url=sheety_endpoint, json=sheety_params, headers=sheety_headers)
    print(sheety_response.text)
    sheety_response.raise_for_status()


# Main program loop ----------------------------------------------------------------------------------------------------
write_gsheet_row()
