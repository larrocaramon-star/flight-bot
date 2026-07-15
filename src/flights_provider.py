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

    # Ejemplo: Montevideo → Nueva York
    params = {
        "originSkyId": "MVD",
        "destinationSkyId": "JFK",
        "departureDate": "2027-02-01",
        "adults": "3",
        "currency": "USD"
    }

    response = requests.get(url, headers=headers, params=params).json()
    price1 = float(response["data"][0]["price"]["amount"])

    # Por ahora dejamos valores de prueba para los otros tramos
    price2 = 180
    price3 = 650

    return {
        "MVD-JFK": price1,
        "JFK-MIA": price2,
        "MIA-MVD": price3
    }
