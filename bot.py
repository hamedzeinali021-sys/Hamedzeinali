
import os
import requests

TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]
ALANCHAND_TOKEN = os.environ["ALANCHAND_TOKEN"]
CHANNEL = "@YOUR_CHANNEL_USERNAME"

url = "https://api.alanchand.com/"
headers = {
    "Authorization": f"Bearer {ALANCHAND_TOKEN}"
}
params = {
    "type": "gold"
}

response = requests.get(
    url,
    headers=headers,
    params=params,
    timeout=20
)

response.raise_for_status()
data = response.json()

print("API RESPONSE:", data)

gold = data["18ayar"]
price = gold["price"]

price_toman = f"{price:,}"

message = (
    "🪙 قیمت طلای ۱۸ عیار\n\n"
    f"هر گرم: {price_toman} تومان\n\n"
    "گالری طلا زینلی"
)

telegram_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

requests.post(
    telegram_url,
    json={
        "chat_id": CHANNEL,
        "text": message
    },
    timeout=20
)
