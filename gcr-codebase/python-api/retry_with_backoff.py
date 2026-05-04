import requests
import time

def fetch_with_retry(url, retries=3):
    for i in range(retries):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"Success after {i+1} attempts")
                return response.json()
        except Exception:
            pass
        time.sleep(2 ** i)
    print("Failed after retries")

fetch_with_retry("https://api.example.com/data")