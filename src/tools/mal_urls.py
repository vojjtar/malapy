import json
import requests


def get_mal_anime_url():
    with open('././url_data.json') as json_file:
        data = json.load(json_file)
        return data['mal_anime_url']

def get_html_from_url(url: str):

    HEADERS = ({'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
                'Accept-Language': 'en-US, en;q=0.5'})

    page = requests.get(url, headers=HEADERS)
    if page.status_code == 200:
        return page.content