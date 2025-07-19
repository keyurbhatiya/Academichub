import requests
from dotenv import load_dotenv
load_dotenv()
import os
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_file_to_telegram(file, caption=""):
    try:
        # Read the file and preserve name
        file.seek(0)  # Ensure we're at the beginning
        filename = getattr(file, 'name', 'file.pdf')
        file_data = file.read()

        if not file_data:
            print("❌ File is empty.")
            return False

        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendDocument"
        files = {'document': (filename, file_data)}
        data = {'chat_id': TELEGRAM_CHAT_ID, 'caption': caption}

        response = requests.post(url, files=files, data=data)

        if response.status_code == 200:
            print("✅ File successfully sent to Telegram.")
            return True
        else:
            print(f"❌ Telegram upload failed: {response.status_code} | {response.text}")
            return False

    except Exception as e:
        print(f"🚨 Error sending file to Telegram: {e}")
        return False
