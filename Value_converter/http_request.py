import requests

def get_response():
    url = "https://openexchangerates.org/api/latest.json?app_id=190c3439a38d490ba111ea275683228b"

    headers = {"accept": "application/json"}

    response = requests.get(url, headers=headers)
    response = response.text

    return response
