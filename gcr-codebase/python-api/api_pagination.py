import requests

def fetch_all():
    page = 1
    total_pages = 3
    
    while page <= total_pages:
        requests.get(f"https://api.example.com/data?page={page}")
        page += 1
    
    print("Fetched all pages successfully.")

fetch_all()