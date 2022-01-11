from datetime import datetime

import gspread
import requests

URL = "https://display.safespace.io/value/live/a7796f34"
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    'https://www.googleapis.com/auth/drive',
]
SHEET_ID = "1QKn9DVrufNj0XUu3_bIH8CabJnxElhtLN1NYAT2YYck"

client = gspread.service_account(filename='/config/get-vital-data-creds')

sheet = client.open_by_key(SHEET_ID).get_worksheet(0)

def process_data(event, context):
    """
    Triggered from a Cloud Pub/Sub Topic
    """
    data = get_data()
    values = [
        [data, str(datetime.now())]
    ]
    sheet.append_rows(values)

def get_data() -> str:
    """
    "74"
    """
    r = requests.get(URL)
    return r.text
