import requests

data = {'username': 'alex', 'password': '1234'}

response = requests.post("https://api.example.com/login", json=data)

if response.status_code == 200:
    print("Login successful")
else:
    print(f"Authentication Failed: {response.status_code}")