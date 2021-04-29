import json
import re
from . import helpers


def _get_api_url(site_text: str) -> str:
    api_key = re.compile('apiKey:"[^"]*').findall(site_text)[0].split('"')[1]
    spread_id = re.compile('spreadsheetId:"[^"]*').findall(site_text)[0].split('"')[1]
    return "https://content-sheets.googleapis.com/v4/spreadsheets/"+spread_id+"/values/Covid%20Care%20Center!A3%3AJ?key="+api_key

def scrape() -> dict:
    
    main_site_url = "https://www.gujaratcovidsupport.org/static/js/main.5ff25e0a.chunk.js"
    main_site_text = helpers.get_site_text(main_site_url)
    api_url = _get_api_url(main_site_text)
    api_text = helpers.get_site_text(api_url)

    hospitals_data = json.loads(api_text)['values']

    data = []
    for hospital_data in hospitals_data:
        if len(hospital_data) <= 8:
            continue
        data.append( {
        "Region"    : hospital_data[1],
        "Name"      : hospital_data[2],
        "Address"   : hospital_data[3],
        "Doctors"   : hospital_data[4],
        "PhoneNo"   : hospital_data[5],
        "Remarks"   : hospital_data[6],
        "Status"    : hospital_data[7],
        "Vacant"    : 1 if hospital_data[7] == "Available" else 0,
        })

    return { 'data' : data }

if __name__ == '__main__':
    print(scrape())
