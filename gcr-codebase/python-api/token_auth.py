import requests

token = "abc123"

headers = {"Authorization": f"Bearer {token}"}

response = requests.get("https://api.example.com/data", headers=headers)

if response.status_code == 200:
    print("Request Authorized")