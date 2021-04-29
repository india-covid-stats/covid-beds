import requests

def get_site_text(url: str) -> str:
    main_site = requests.get(url)
    if not (200 <= main_site.status_code < 300):
        raise Exception( url + ": didn't send a successful response")
    return main_site.text
