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
    print(response)  # 👈 Para ver qué campos trae

    try:
        price1 = float(response["data"][0]["price"]["amount"])
        link1 = response["data"][0].get("deeplink", "No disponible")
    except (KeyError, IndexError):
        price1 = -1
        link1 = "No disponible"

    # Por ahora valores de prueba para los otros tramos
    price2 = 180
    link2 = "No disponible"
    price3 = 650
    link3 = "No disponible"

    return {
        "MVD-JFK": {"price": price1, "link": link1},
        "JFK-MIA": {"price": price2, "link": link2},
        "MIA-MVD": {"price": price3, "link": link3}
    }
