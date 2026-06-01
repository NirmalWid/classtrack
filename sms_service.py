import requests
import os
from dotenv import load_dotenv

# =========================================
# SMSLENZ CONFIG
# =========================================

load_dotenv()

API_KEY = os.getenv("SMS_API_KEY")

USER_ID = os.getenv("SMS_USER_ID")

SENDER_ID = os.getenv("SMS_SENDER_ID")


# =========================================
# FORMAT PHONE
# =========================================

def format_phone(phone):

    phone = phone.strip()

    if phone.startswith("0"):

        phone = "94" + phone[1:]

    return phone


# =========================================
# SEND SMS
# =========================================

def send_sms(phone, message):

    url = "https://www.smslenz.lk/api/send-sms"

    payload = {

        "api_key": API_KEY,
        "user_id": USER_ID,
        "sender_id": SENDER_ID,

        "contact": format_phone(phone),

        "message": message
    }

    try:
        response = requests.post(url, data=payload)
        print("SMS RESPONSE:", response.text)

    except Exception as e:
        print("SMS ERROR:", e)
