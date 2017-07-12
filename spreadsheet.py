"""
    Google SpreadSheet API handlers
"""
from __future__ import print_function

import os

from datetime import datetime

import httplib2
import pytz

from apiclient import discovery
from bs4 import BeautifulSoup
from oauth2client.file import Storage
from requests import get



def google_spreadsheet_service():
    """Return spreadsheet service object."""
    credentials = Storage(
        os.path.join(os.getcwd(), 'client_secret.json')
    ).get()
    http = credentials.authorize(httplib2.Http())
    discovery_url = (
        'https://sheets.googleapis.com/$discovery/rest?version=v4'
    )
    service = discovery.build(
        'sheets', 'v4', http=http, discoveryServiceUrl=discovery_url
    )
    return service


def add_to_spreadsheet(link):
    """Write link to the spreadsheet"""
    service = google_spreadsheet_service()

    response = get(link)
    html_doc = response.content
    soup = BeautifulSoup(html_doc, 'html.parser')
    timezone = pytz.timezone('Asia/Seoul')
    created_at = datetime.now(timezone).strftime("%Y-%m-%d %H:%M:%S")

    if response.ok:
        title = soup.find('title').text.encode('utf-8')
    else:
        title = "NO TITLE"

    values = [[title, link, created_at]]
    body = {'values': values}
    
    range_name = 'Sheet1!A:E'
    spreadsheet_id = os.environ.get('SPREADSHEET_ID')

    service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id, range=range_name,
        valueInputOption="USER_ENTERED", body=body
    ).execute()
