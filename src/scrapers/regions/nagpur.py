from bs4 import BeautifulSoup
from . import helpers


def get_hospitals_data(html_text: str) -> list:
    soup = BeautifulSoup(html_text, 'lxml' )
    records = soup.find('tbody').find_all('tr')
    return [ record.find_all('td') for record in records if record.text != '\n' ]

def scrape() -> dict:
    url = "https://nsscdcl.org/covidbeds/AvailableHospitals.jsp"
    hospitals_data = get_hospitals_data(helpers.get_site_text(url))
    data = []
    for hospital_data in hospitals_data:
        data.append( {
        "Hospital"  : hospital_data[1].text,
        "O2"        : hospital_data[2].text,
        "ICU"       : hospital_data[3].text,
        "Ventilator": hospital_data[4].text,
        })

    return { 'data' : data }

if __name__ == '__main__':
    print(scrape())

