import requests
from dotenv import load_dotenv

import os

load_dotenv()
webhook_id = os.getenv("WEBHOOK_ID")
webhook_token = os.getenv("WEBHOOK_TOKEN")
webhook_url = f"https://discord.com/api/webhooks/{webhook_id}/{webhook_token}"


def send_message():
    content = f"Error getting modules using comx! Empty list returned."
    payload = {
        "content": content,
        "username": "AIM stats commune"
    }

    print(content)
    response = requests.post(webhook_url, json=payload)
    if response.status_code == 204:
        print("Message sent successfully!")
    else:
        print(f"Failed to send message. Status code: {response.status_code}")
        print(f"Response: {response.text}")
