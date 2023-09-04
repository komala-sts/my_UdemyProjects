import requests

parameters = {
    "amount": 10,
    "type": "boolean",
}
#https://opentdb.com/api_config.php
#https://opentdb.com/api.php?amount=15&category=27&difficulty=easy&type=boolean
response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]
