# flights_provider.py
import os
import requests

def get_prices():
    api_key = os.environ.get("SKYSCANNER_API_KEY")
    url = "https://sky-scrapper.p.rapidapi.com/api/v1/flights/searchFlights"
    headers = {
        "x-rapidapi-key": api_key,
        "x-rapidapi-host": "sky-scrapper.p.rapidapi.com"
    }

    # Tramo 1: Montevideo → Nueva York
    params1 = {
        "originSkyId": "MVD",
        "destinationSkyId": "JFK",
        "departureDate": "2027-02-01",
        "adults": "3",
        "currency": "USD"
    }
    response1 = requests.get(url, headers=headers, params=params1).json()
    print("MVD-JFK:", response1)
    try:
        price1 = float(response1["data"][0]["price"]["amount"])
        link1 = response1["data"][0].get("deeplink", "No disponible")
    except (KeyError, IndexError):
        price1, link1 = -1, "No disponible"

    # Tramo 2: Nueva York → Miami
    params2 = {
        "originSkyId": "JFK",
        "destinationSkyId": "MIA",
        "departureDate": "2027-02-05",
        "adults": "3",
        "currency": "USD"
    }
    response2 = requests.get(url, headers=headers, params=params2).json()
    print("JFK-MIA:", response2)
    try:
        price2 = float(response2["data"][0]["price"]["amount"])
        link2 = response2["data"][0].get("deeplink", "No disponible")
    except (KeyError, IndexError):
        price2, link2 = -1, "No disponible"

    # Tramo 3: Miami → Montevideo
    params3 = {
        "originSkyId": "MIA",
        "destinationSkyId": "MVD",
        "departureDate": "2027-02-10",
        "adults": "3",
        "currency": "USD"
    }
    response3 = requests.get(url, headers=headers, params=params3).json()
    print("MIA-MVD:", response3)
    try:
        price3 = float(response3["data"][0]["price"]["amount"])
        link3 = response3["data"][0].get("deeplink", "No disponible")
    except (KeyError, IndexError):
        price3, link3 = -1, "No disponible"

    return {
        "MVD-JFK": {"price": price1, "link": link1},
        "JFK-MIA": {"price": price2, "link": link2},
        "MIA-MVD": {"price": price3, "link": link3}
    }
