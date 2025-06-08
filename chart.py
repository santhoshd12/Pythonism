import requests

api_key = "9mfjuyfpn27jbjvuzsm6uvwp"
url = "https://ieeexploreapi.ieee.org/api/v1/search/articles"
params = {
    "apikey": api_key,
    "format": "json",
    "querytext": "drone",  # keep it simple
    "max_records": 1
}

response = requests.get(url, params=params)
print(response.status_code)
print(response.text)
