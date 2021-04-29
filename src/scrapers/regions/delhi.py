#!/bin/python3
import json
from . import helpers


def _get_json_data(data: str) -> list[dict]:
    # obtains the json as a dictionary from the data
    json_data = data.replace("var gnctd_covid_data = ","",1).rstrip(";")
    dict_data = json.loads(json_data)
    return list(dict_data['beds'].items())[:-1]



def scrape():
    data = []
    url = "https://coronabeds.jantasamvad.org/covid-info.js"
    for hospital,info in _get_json_data(helpers.get_site_text(url)):
        hospital_data = {
                "Hospital"  : hospital,
                "Type"      : info['type'],
                "Vacant"    : info['vacant'],
                "Occupied"  : info['occupied'],
                "Total"     : info['total'],
                "Update"    : info['last_updated_at'],
                }
        data.append(hospital_data)

    return {'data' : data }

if __name__ == '__main__':
    print(scrape())
