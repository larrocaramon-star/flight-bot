# main.py
# Punto de entrada del bot

from telegram_bot import send_daily_report
from flights_provider import get_prices
from analysis import analyze_prices
import utils

def main():
    # Obtener precios
    prices = get_prices()
    # Analizar variaciones
    report = analyze_prices(prices)
    # Enviar informe por Telegram
    send_daily_report(report)

if __name__ == "__main__":
    main()
    
