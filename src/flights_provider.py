import os
import requests

def get_prices():
    api_key = os.environ.get("KIWI_API_KEY")  # tu secreto en GitHub
    url = "https://kayak.p.rapidapi.com/flights"
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "kayak.p.rapidapi.com"
    }

    def fetch_price(origin, destination, depart_date, return_date):
        params = {
            "origin": origin,
            "destination": destination,
            "depart_date": depart_date,
            "return_date": return_date,
            "adults": "3",
            "currency": "USD"
        }
        response = requests.get(url, headers=headers, params=params).json()
        print(f"{origin}-{destination} response:", response)  # 👈 Depuración
        try:
            price = float(response.get("price", -1))
            link = response.get("deep_link", "No disponible")
        except (KeyError, TypeError, ValueError):
            price, link = -1, "No disponible"
        return {"price": price, "link": link}

    return {
        "MVD-NYC": fetch_price("MVD", "NYC", "2026-08-01", "2026-08-08"),
        "NYC-MIA": fetch_price("NYC", "MIA", "2026-08-09", "2026-08-12"),
        "MIA-MVD": fetch_price("MIA", "MVD", "2026-08-13", "2026-08-20"),
    }
