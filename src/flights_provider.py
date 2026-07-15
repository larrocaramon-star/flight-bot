params_test = {
    "fly_from": "MVD",
    "fly_to": "GRU",
    "date_from": "01/08/2026",
    "date_to": "01/08/2026",
    "adults": 1,
    "curr": "USD"
}
response_test = requests.get(url, headers=headers, params=params_test).json()
print("Test response:", response_test)
