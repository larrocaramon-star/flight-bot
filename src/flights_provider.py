# flights_provider.py
import os
import requests

def get_prices():
    api_key = os.environ.get("KIWI_API_KEY")
    url = "https://api.tequila.kiwi.com/v2/search"
    headers = {"apikey": api_key}

    # Tramo 1: Montevideo → Nueva York (agosto 2026)
    params1 = {
        "fly_from": "MVD",
        "fly_to": "NYC",  # NYC agrupa todos los aeropuertos de Nueva York
        "date_from": "01/08/2026",
        "date_to": "01/08/2026",
        "adults": 3,
        "curr": "USD"
    }
    response1 = requests.get(url, headers=headers, params=params1).json()
    print("MVD-NYC:", response1)
    try:
        price1 = float(response1["data"][0]["price"])
        link1 = response1["data"][0].get("deep_link", "No disponible")
    except (KeyError, IndexError):
        price1, link1 = -1, "No disponible"

    # Tramo 2: Nueva York → Miami (agosto 2026)
    params2 = {
        "fly_from": "NYC",
        "fly_to": "MIA",
        "date_from": "05/08/2026",
        "date_to": "05/08/2026",
        "adults": 3,
        "curr": "USD"
    }
    response2 = requests.get(url, headers=headers, params=params2).json()
    print("NYC-MIA:", response2)
    try:
        price2 = float(response2["data"][0]["price"])
        link2 = response2["data"][0].get("deep_link", "No disponible")
    except (KeyError, IndexError):
        price2, link2 = -1, "No disponible"

    # Tramo 3: Miami → Montevideo (agosto 2026)
    params3 = {
        "fly_from": "MIA",
        "fly_to": "MVD",
        "date_from": "10/08/2026",
        "date_to": "10/08/2026",
        "adults": 3,
        "curr": "USD"
    }
    response3 = requests.get(url, headers=headers, params=params3).json()
    print("MIA-MVD:", response3)
    try:
        price3 = float(response3["data"][0]["price"])
        link3 = response3["data"][0].get("deep_link", "No disponible")
    except (KeyError, IndexError):
        price3, link3 = -1, "No disponible"

    return {
        "MVD-NYC": {"price": price1, "link": link1},
        "NYC-MIA": {"price": price2, "link": link2},
        "MIA-MVD": {"price": price3, "link": link3}
    }
