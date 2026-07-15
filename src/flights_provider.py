import os
import requests

def get_prices():
    api_key = os.environ.get("KIWI_API_KEY")
    url = "https://kiwi-com-cheap-flights.p.rapidapi.com/roundtrip"
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "kiwi-com-cheap-flights.p.rapidapi.com"
    }

    def fetch_price(fly_from, fly_to, depart_date, return_date):
        params = {
            "from": fly_from,
            "to": fly_to,
            "depart": depart_date,
            "return": return_date,
            "adults": "3",
            "currency": "USD"
        }
        response = requests.get(url, headers=headers, params=params).json()
        print(f"{fly_from}-{fly_to} response:", response)  # 👈 Depuración
        try:
            price = float(response["price"])
            link = response.get("deep_link", "No disponible")
        except (KeyError, TypeError):
            price, link = -1, "No disponible"
        return {"price": price, "link": link}

    return {
        "MVD-NYC": fetch_price("MVD", "NYC", "2026-08-01", "2026-08-08"),
        "NYC-MIA": fetch_price("NYC", "MIA", "2026-08-09", "2026-08-12"),
        "MIA-MVD": fetch_price("MIA", "MVD", "2026-08-13", "2026-08-20"),
    }
