# flights_provider.py
import os
import requests

def get_prices():
    api_key = os.environ.get("KIWI_API_KEY")
    url = "https://travelpayouts-travelpayouts-flight-data-v1.p.rapidapi.com/v2/prices/nearest-places-matrix"
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "travelpayouts-travelpayouts-flight-data-v1.p.rapidapi.com"
    }

    def fetch_price(origin, destination, depart_date):
        params = {
            "origin": origin,
            "destination": destination,
            "currency": "USD",
            "flexibility": 0,
            "limit": 1,
            "distance": 100,
            "depart_date": depart_date
        }
        r = requests.get(url, headers=headers, params=params)
        print(f"{origin}-{destination} raw response:", r.text)  # 👈 Depuración

        try:
            response = r.json()
            # Travelpayouts devuelve lista de tickets en "data"
            ticket = response.get("data", [{}])[0]
            price = float(ticket.get("price", -1))
            link = ticket.get("link", "No disponible")
        except Exception:
            price, link = -1, "No disponible"

        return {"price": price, "link": link}

    return {
        "MVD-NYC": fetch_price("MVD", "NYC", "2026-08-01"),
        "NYC-MIA": fetch_price("NYC", "MIA", "2026-08-09"),
        "MIA-MVD": fetch_price("MIA", "MVD", "2026-08-13"),
    }
