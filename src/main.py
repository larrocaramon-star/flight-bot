import os
import requests
from flights_provider import get_prices
from analysis import analyze_prices

def main():
    prices = get_prices()
    report = analyze_prices(prices)

    token = os.environ.get("TELEGRAM_TOKEN")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID")
    url = f"https://api.telegram.org/bot{token}/sendMessage"

    payload = {"chat_id": chat_id, "text": report}
    r = requests.post(url, data=payload)
    print("Telegram response:", r.json())  # 👈 Depuración

if __name__ == "__main__":
    main()
