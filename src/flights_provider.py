# flights_provider.py
import os
import requests

def get_prices():
    api_key = os.environ.get("KIWI_API_KEY")
    url = "https://kiwi-com-ultimate-flights.p.rapidapi.com/search"
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "kiwi-com-ultimate-flights.p.rapidapi.com"
    }

    def fetch_price(origin, destination, depart_date):
        params = {
            "fly_from": origin,
            "fly_to": destination,
            "date_from": depart_date,
            "date_to": depart_date,
            "curr": "USD",
            "adults": 3
        }
        r = requests.get(url, headers=headers, params=params)
        print(f"{origin}-{destination} raw response:", r.text)  # 👈 Depuración

        try:
            response = r.json()
            # Kiwi devuelve resultados en "data"
            ticket = response.get("data", [{}])[0]
            price = float(ticket.get("price", -1))
            link = ticket.get("deep_link", "No disponible")
        except Exception:
            price, link = -1, "No disponible"

        return {"price": price, "link": link}

    return {
        "MVD-NYC": fetch_price("MVD", "NYC", "2026-08-01"),
        "NYC-MIA": fetch_price("NYC", "MIA", "2026-08-09"),
        "MIA-MVD": fetch_price("MIA", "MVD", "2026-08-13"),
    }
