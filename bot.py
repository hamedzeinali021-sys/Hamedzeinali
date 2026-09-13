import os
import requests
from datetime import datetime

TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]
ALANCHAND_TOKEN = os.environ["ALANCHAND_TOKEN"]
CHANNEL = "@YOUR_CHANNEL_USERNAME"

url = f"https://api.alanchand.com/?type=golds&token={ALANCHAND_TOKEN}"

response = requests.get(url, timeout=20)
data = response.json()

gold = data["18ayar"]
price = gold["price"]

price_toman = f"{price:,}"

message = (
    "🪙 قیمت طلای ۱۸ عیار\n\n"
    f"هر گرم: {price_toman} تومان\n\n"
    f"🕐 بروزرسانی: {gold['updated_at']}\n"
    "گالری طلا زینلی"
)

telegram_url = (
    f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
)

requests.post(
    telegram_url,
    json={
        "chat_id": CHANNEL,
        "text": message
    },
    timeout=20
)
