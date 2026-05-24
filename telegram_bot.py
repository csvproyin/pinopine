import requests

BOT_TOKEN = "8613137726:AAFV1CGIqA984wOHJC3s3mxUd1E0HU1pnTY"
CHAT_ID = 5043686557

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    
    data = {
        "chat_id": CHAT_ID,
        "text": text[:3000]
    }

    requests.post(url, data=data)


def get_updates():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"
    return requests.get(url).json()

def send_photo(photo_path):

    import requests

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"

    files = {
        "photo": open(photo_path, "rb")
    }

    data = {
        "chat_id": CHAT_ID
    }

    requests.post(url, files=files, data=data)