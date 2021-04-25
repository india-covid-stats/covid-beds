#!/bin/python3
import requests
import json

def get_main_site():
    url = "https://coronabeds.jantasamvad.org/covid-info.js"
    main_site = requests.get(url)
    if not (200 <= main_site.status_code < 300):
        raise Exception("Main site didn't send a successful response")
    return main_site.text

def get_json_data(data):
    json_data = data.replace("var gnctd_covid_data = ","",1).rstrip(";")
    dict_data = json.loads(json_data)
    return list(dict_data['beds'].items())[:-1]

for hospital,info in get_json_data(get_main_site()):
    print("Hospital:",hospital)
    print("Type:",info['type'])
    print("Vacant:",info['vacant'])
    print("Occupied:",info['occupied'])
    print("Total:",info['total'])
    print("Update:",info['last_updated_at'])
    print("")
