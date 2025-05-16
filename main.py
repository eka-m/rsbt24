from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    requests.get(url, params=payload)

@app.route('/bitrix', methods=['POST'])
def bitrix_webhook():
    data = request.json

    title = data.get("TITLE", "Без названия")
    contact_name = data.get("CONTACT_NAME", "—")
    contact_phone = data.get("CONTACT_PHONE", "—")
    contact_email = data.get("CONTACT_EMAIL", "—")
    assigned_by = data.get("ASSIGNED_BY", "—")
    link = data.get("PathToEntity", "—")

    message = f"""
📩 Новая сделка!
🧾 Название: {title}
👤 Контакт: {contact_name}
📞 Телефон: {contact_phone}
📧 Email: {contact_email}
📊 Ответственный: {assigned_by}
🔗 Открыть: {link}
"""

    send_telegram_message(message)
    return "OK", 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)