# flights_provider.py
import os
import requests

def get_prices():
    api_key = os.environ.get("KIWI_API_KEY")
    url = "https://api.tequila.kiwi.com/v2/search"
    headers = {"apikey": api_key}

    # Tramo 1: Montevideo → Nueva York
    params1 = {
        "fly_from": "MVD",
        "fly_to": "JFK",
        "date_from": "01/02/2027",
        "date_to": "01/02/2027",
        "adults": 3,
        "curr": "USD"
    }
    response1 = requests.get(url, headers=headers, params=params1).json()
    print("MVD-JFK:", response1)
    try:
        price1 = float(response1["data"][0]["price"])
        link1 = response1["data"][0].get("deep_link", "No disponible")
    except (KeyError, IndexError):
        price1, link1 = -1, "No disponible"

    # Tramo 2: Nueva York → Miami
    params2 = {
        "fly_from": "JFK",
        "fly_to": "MIA",
        "date_from": "05/02/2027",
        "date_to": "05/02/2027",
        "adults": 3,
        "curr": "USD"
    }
    response2 = requests.get(url, headers=headers, params=params2).json()
    print("JFK-MIA:", response2)
    try:
        price2 = float(response2["data"][0]["price"])
        link2 = response2["data"][0].get("deep_link", "No disponible")
    except (KeyError, IndexError):
        price2, link2 = -1, "No disponible"

    # Tramo 3: Miami → Montevideo
    params3 = {
        "fly_from": "MIA",
        "fly_to": "MVD",
        "date_from": "10/02/2027",
        "date_to": "10/02/2027",
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
        "MVD-JFK": {"price": price1, "link": link1},
        "JFK-MIA": {"price": price2, "link": link2},
        "MIA-MVD": {"price": price3, "link": link3}
    }
