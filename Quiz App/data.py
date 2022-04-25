import requests

parameters = {
    "ammount": 10,
    "type": "boolean"
}

response = requests.get("https://opentdb.com/api.php?amount=10&category=15&difficulty=medium&type=boolean", params=parameters)
response.raise_for_status()
data = response.json()

question_data = data["results"]