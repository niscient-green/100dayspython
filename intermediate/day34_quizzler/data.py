# Get 10 new questions using API Open Trivia Database
import requests
otd_params = {
    "amount": 10,
    "type": "boolean",
}
otd_response = requests.get(url="https://opentdb.com/api.php", params=otd_params)
otd_response.raise_for_status()
questions_dtc = otd_response.json()["results"]