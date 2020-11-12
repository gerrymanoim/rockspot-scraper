import re
from datetime import datetime
from pprint import pprint

from typing import Any, Dict

import gspread
import requests

from bs4 import BeautifulSoup
import google.auth

URL = "https://portal.rockgympro.com/portal/public/7a2ec613bb982d4ba91785c2cdb45902/occupancy?&iframeid=occupancyCounter&fId=1325"
DATA_PATTERN = re.compile("var data =(.*?);", re.DOTALL)
TIME_PATTERN = re.compile("\(.*\)")
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    'https://www.googleapis.com/auth/drive',
]
SHEET_ID = "1vpa1DXR4zAlEcrd7Vgfk7IeSwm_umDYABiEh-u1Ky9Q"

credentials, _ = google.auth.default(scopes=SCOPES)
client = gspread.authorize(credentials)

sheet = client.open_by_key(SHEET_ID).get_worksheet(0)

def process_data(event, context):
    """
    Triggered from a Cloud Pub/Sub Topic
    """
    data = get_data()
    values = [
        [loc, a['capacity'], a['count'], str(datetime.now())] for loc,a in data.items()
    ]
    sheet.append_rows(values)

def get_data() -> Dict[str, Dict[str, Any]]:
    """
    {'BOS': {'capacity': 50,
    'count': 6,
    'subLabel': 'Current climber count',
    'lastUpdate': 'Last updated:&nbspnow  (2:35 PM)'},
    """
    r = requests.get(URL)
    s = BeautifulSoup(r.text)
    for script in s.find_all('script'):
        data = DATA_PATTERN.search(str(script))
        if data:
            return eval(data.groups()[0])
