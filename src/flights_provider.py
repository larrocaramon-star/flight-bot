# flights_provider.py
import os
import requests

def get_prices():
    api_key = os.environ.get("SKYSCANNER_API_KEY")
    url = "https://sky-scrapper.p.rapidapi.com/api/v1/flights/searchFlightsMultiStops"
    headers = {
        "x-rapidapi-key": api_key,
        "x-rapidapi-host": "sky-scrapper.p.rapidapi.com"
    }

    # Multi-stop: MVD → JFK → MIA → MVD
    params = {
        "originSkyId": "MVD",
        "destinationSkyId": "MVD",
        "stops": "JFK,MIA",
        "departureDate": "2027-02-01",
        "returnDate": "2027-02-10",
        "adults": "3",
        "currency": "USD"
    }

    response = requests.get(url, headers=headers, params=params).json()
    print(response)  # 👈 Para ver qué devuelve

    try:
        itinerary = response["data"][0]
        total_price = float(itinerary["price"]["amount"])
        deeplink = itinerary.get("deeplink", "No disponible")
    except (KeyError, IndexError):
        total_price, deeplink = -1, "No disponible"

    return {
        "TOTAL": {"price": total_price, "link": deeplink}
    }
