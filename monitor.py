import os

import requests
from dotenv import load_dotenv

load_dotenv()

bot_token = os.getenv("TELEGRAM_TOKEN")
url = os.getenv("TARGET_URL")


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
