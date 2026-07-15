import os
import requests

def get_prices():
    api_key = os.environ.get("KIWI_API_KEY")
    print("API KEY:", api_key)  # 👈 Verifica que no sea None

    url = "https://api.tequila.kiwi.com/v2/search"
    headers = {"apikey": api_key}

    params = {
        "fly_from": "MVD",
        "fly_to": "NYC",
        "date_from": "01/08/2026",
        "date_to": "01/08/2026",
        "adults": 1,
        "curr": "USD"
    }

    response = requests.get(url, headers=headers, params=params).json()
    print("Response:", response)

    try:
        price = float(response["data"][0]["price"])
        link = response["data"][0].get("deep_link", "No disponible")
    except (KeyError, IndexError):
        price, link = -1, "No disponible"

    return {"MVD-NYC": {"price": price, "link": link}}
