import re
from . import helpers
from bs4 import BeautifulSoup

# not completed, TODO: need to categorize data

def scrape():

    # scrape he main website to get the google sheet url
    html_text = helpers.get_site_text('https://durg.gov.in/covidbedsdurg/')
    soup = BeautifulSoup(html_text,'lxml')
    google_docs_url = soup.iframe['src']

    sheet_url = ( google_docs_url.split('?')[0] 
        + "/sheet?headers=false&"  
        + re.findall(r"gid=[^\&]*", google_docs_url)[0]
        )
    
    sheet_url = re.sub("/d/e/","/u/0/d/e/", sheet_url, count= 1)
    
    # scrape the sheet and gather info
    sheet_html = helpers.get_site_text(sheet_url)
    soup = BeautifulSoup(sheet_html,'lxml')
    
    data = []

    for tr in soup.tbody('tr'):
        data.append([ tr.text for tr in tr('td')])
    
    return { 'data' : data }

if __name__ == '__main__':
    print(scrape())
