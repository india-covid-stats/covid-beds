#!/bin/python3
from bs4 import BeautifulSoup
import requests

def get_main_site() -> str:
    main_site = requests.get('https://stopcorona.tn.gov.in/beds.php')
    if not ( 200 <= main_site.status_code < 300  ):
        raise Exception('Failed to get successfull response')
    return main_site.text

def get_hospitals_data(html: str) -> list:
    parsed_html = BeautifulSoup(html,'lxml')
    return parsed_html.find("tbody").find_all("tr")

for hospital_data in get_hospitals_data(get_main_site()):
    fields = [ field.text for field in hospital_data.find_all("td")]
    print("Region:",    fields[0])
    print("Hospital:",  fields[1])
    print("Total:",     fields[2])
    print("Occupied:",  fields[3])
    print("Vacant:",    fields[4])
    print("Update:",    fields[-3])
    print()
