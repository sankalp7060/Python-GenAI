import requests
import json

try:
    response = requests.get("https://api.example.com/data")
    data = response.json()
except json.decoder.JSONDecodeError:
    print("Error: Invalid JSON response")