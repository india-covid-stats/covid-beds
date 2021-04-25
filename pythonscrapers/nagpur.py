#!/bin/python3
import requests
from bs4 import BeautifulSoup

def get_main_site():
    site_data = requests.get("https://nsscdcl.org/covidbeds/AvailableHospitals.jsp")
    if not ( 200 <= site_data.status_code < 300 ):
        raise Exception('Failed to get successfull response')
    return site_data.text

def get_hospitals_data(html_text):
    soup = BeautifulSoup(html_text, 'lxml' )
    records = soup.find('tbody').find_all('tr')
    return [ record.find_all('td') for record in records if record.text != '\n' ]

for hospital_data in get_hospitals_data(get_main_site()):
    print("Hospital:", hospital_data[1].text)
    print("O2:", hospital_data[2].text)
    print("ICU:", hospital_data[3].text)
    print("Ventilator:", hospital_data[4].text)
    print("")
