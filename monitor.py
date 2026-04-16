import os
import time

import requests
from dotenv import load_dotenv

load_dotenv()

bot_token = os.getenv("TELEGRAM_TOKEN")
url = os.getenv("TARGET_URL")
chat_id = os.getenv("TELEGRAM_CHAT_ID")
api_url = f"https://api.telegram.org/bot<{bot_token}>/sendMessage"
text = "Сайт впав! 🚨"


def send_telegram_message(token, chat_id, text):
    try:
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": text,
        }
        response = requests.post(url, data=payload)
        return response.json()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False


def check_website(url):
    try:
        response = requests.get(str(url))

        if response.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False


if __name__ == "__main__":
    while True:
        if check_website(url):
            pass
        else:
            send_telegram_message(bot_token, chat_id, text)
        time.sleep(3)
        print("checked")
