import requests
from os import environ
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

url_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "Content-Type": "application/json",
    "x-app-id": environ["APP_ID"],
    "x-app-key": environ["APP_KEY"]
}

user_input = input("Tell me which exercises you did: ")
parameters = {
    "query": user_input
}

response = requests.post(url=url_endpoint, json=parameters, headers=headers)
response.raise_for_status()
data = response.json()

url_sheety = environ["SHEET_ENDPOINT"]
header = {
    "Content-Type": "application/json",
    "Authorization": environ["TOKEN"],
}

for elements in data['exercises']:
    to_spreadsheet = { # type: ignore
        "sheet1": {
            "date": datetime.today().strftime("%d/%m/%Y"),
            "time": datetime.today().strftime("%H:%M:%S"),
            "exercise": elements['name'].title(),
            "duration": elements['duration_min'],
            "calories": elements['nf_calories']
        }
    }
    
    sheety_request = requests.post(url=url_sheety, json=to_spreadsheet, headers=header) # pyright: ignore[reportUnknownArgumentType]
    sheety_request.raise_for_status()