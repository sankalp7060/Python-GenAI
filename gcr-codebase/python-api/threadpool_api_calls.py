import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

endpoints = ["/users", "/products", "/orders"]
base_url = "https://api.example.com"

def fetch(endpoint):
    return requests.get(base_url + endpoint)

with ThreadPoolExecutor() as executor:
    futures = [executor.submit(fetch, ep) for ep in endpoints]
    for f in as_completed(futures):
        f.result()

print("Fetched 3 APIs in parallel.")