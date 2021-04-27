#!/bin/python3

import re
import requests
from bs4 import BeautifulSoup

def get_page(page_url: str) -> str:
    page = requests.get(page_url)
    if not (200 <=  page.status_code < 300):
        raise Exception("Get request no successful")
    return page.text

html_text = get_page('https://durg.gov.in/covidbedsdurg/')

soup = BeautifulSoup(html_text,'lxml')

google_docs_url = soup.iframe['src']
sheet_url = google_docs_url.split('?')[0] + "/sheet?headers=false&"  + re.findall(r"gid=[^\&]*", google_docs_url)[0]

sheet_url = re.sub("/d/e/","/u/0/d/e/", sheet_url, count= 1)

html_text = get_page(sheet_url)

soup = BeautifulSoup(html_text,'lxml')

for tr in soup.tbody('tr'):
    print( [ tr.text for tr in tr('td')])

