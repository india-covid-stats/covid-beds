from bs4 import BeautifulSoup
from . import helpers

def get_hospitals_data(html: str) -> list:
    parsed_html = BeautifulSoup(html,'lxml')
    return parsed_html.find("tbody").find_all("tr")

def scrape():
    url = 'https://stopcorona.tn.gov.in/beds.php'
    hospitals_data = get_hospitals_data(helpers.get_site_text(url))
    
    data = []
    for hospital_data in  hospitals_data:
        fields = [ field.text for field in hospital_data.find_all("td")]
        data.append( {
        "Region":    fields[0],
        "Hospital":  fields[1],
        "Total":     fields[2],
        "Occupied":  fields[3],
        "Vacant":    fields[4],
        "Update":    fields[-3],
        })

    return { 'data' : data }

if __name__ == '__main__':
    print(scrape())
