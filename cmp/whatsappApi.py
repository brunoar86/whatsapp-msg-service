import requests
from flask import current_app as app

def send_whatsapp_message(num, message):
    version = 'v18.0'
    phone_number_id = app.config['PHONE_NUMBER_ID']
    url = f"https://graph.facebook.com/{version}/{phone_number_id}/messages"
  
    payload = {
        "messaging_product": "whatsapp",
        "to": num,
        "text": {"body": message},
    }

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {app.config["BEARER_TOKEN"]}'
    }

    response = requests.post(url, headers=headers, json=payload)
    print(response.text)

def send_msg_to_all(message):
    with open('whatsAppNumbers.txt', 'r') as file:
        numbers = file.readlines()
    for num in numbers:
        send_whatsapp_message(num.strip(), message)
