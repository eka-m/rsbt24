from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "8090658375:AAFf9me2H75VancI4nSYIIv07Pmq5EE4uBk"
CHAT_ID = "498183851"

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

if name == '__main__':
    app.run(host='0.0.0.0', port=5000)