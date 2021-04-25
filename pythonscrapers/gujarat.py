#!/bin/python3
import json
import requests
import re

def get_main_site():
    main_site_url = "https://www.gujaratcovidsupport.org/static/js/main.5ff25e0a.chunk.js"
    main_site = requests.get(main_site_url)
    if not (200 <= main_site.status_code < 300):
        raise Exception("Main site didn't send a successful response")
    return main_site.text

def get_api_url(site_text):
    api_key = re.compile('apiKey:"[^"]*').findall(site_text)[0].split('"')[1]
    spread_id = re.compile('spreadsheetId:"[^"]*').findall(site_text)[0].split('"')[1]
    return "https://content-sheets.googleapis.com/v4/spreadsheets/"+spread_id+"/values/Covid%20Care%20Center!A3%3AJ?key="+api_key

def get_dict_api(api_url):
    api_respose = requests.get(api_url)
    if not (200 <= api_respose.status_code < 300):
        raise Exception("Api didn't send a successful response")
    return json.loads(api_respose.text)

def print_data(hospitals_data):
    print("Region:",hospital_data[1].replace("\n","\n+"))
    print("Name:",hospital_data[2].replace("\n","\n+"))
    print("Address:",hospital_data[3].replace("\n","\n+"))
    print("Doctors:",hospital_data[4].replace("\n","\n+"))
    print("PhoneNo:",hospital_data[5].replace("\n","\n+"))
    print("Remarks:",hospital_data[6].replace("\n","\n+"))
    print("Status:",hospital_data[7].replace("\n","\n+"))
    if hospital_data[7] == "Available":
        print("Vacant:",1)
    else:
        print("Vacant:",0)
    print("Update:",hospital_data[9].replace("\n","\n+"))
    print("")

hospitals_data = get_dict_api(get_api_url(get_main_site()))['values']

for hospital_data in hospitals_data:
    try:
        print_data(hospital_data)
    except:
        pass
