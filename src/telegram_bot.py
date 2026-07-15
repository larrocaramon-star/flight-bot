# telegram_bot.py
# Lógica para enviar mensajes a Telegram

import os
import requests

def send_daily_report(report_text: str):
    token = os.environ.get("TELEGRAM_TOKEN")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID")
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {"chat_id": chat_id, "text": report_text}
    requests.post(url, data=data)
