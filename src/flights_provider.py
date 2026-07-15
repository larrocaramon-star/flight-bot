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

    params = {
        "originSkyId": "MVD",
        "destinationSkyId": "JFK",
        "departureDate": "2027-02-01",
        "adults": "3",
        "currency": "USD"
    }

    response = requests.get(url, headers=headers, params=params).json()
    print(response)  # 👈 Esto mostrará la respuesta completa en los logs

    try:
        price1 = float(response["data"][0]["price"]["amount"])
    except (KeyError, IndexError):
        price1 = -1  # Valor de error si no hay datos

    # Valores de prueba para los otros tramos
    price2 = 180
    price3 = 650

    return {
        "MVD-JFK": price1,
        "JFK-MIA": price2,
        "MIA-MVD": price3
    }
