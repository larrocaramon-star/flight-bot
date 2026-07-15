import os
import requests

def get_prices():
    api_key = os.environ.get("KIWI_API_KEY")
    url = "https://api.tequila.kiwi.com/v2/search"
    headers = {"apikey": api_key}

    def fetch_price(fly_from, fly_to, date):
        params = {
            "fly_from": fly_from,
            "fly_to": fly_to,
            "date_from": date,
            "date_to": date,
            "adults": 3,
            "curr": "USD"
        }
        response = requests.get(url, headers=headers, params=params).json()
        print(f"{fly_from}-{fly_to} response:", response)  # 👈 Depuración
        try:
            price = float(response["data"][0]["price"])
            link = response["data"][0].get("deep_link", "No disponible")
        except (KeyError, IndexError):
            price, link = -1, "No disponible"
        return {"price": price, "link": link}

    return {
        "MVD-NYC": fetch_price("MVD", "NYC", "01/08/2026"),
        "NYC-MIA": fetch_price("NYC", "MIA", "05/08/2026"),
        "MIA-MVD": fetch_price("MIA", "MVD", "10/08/2026"),
    }
