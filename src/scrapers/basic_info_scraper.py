from dataclasses import replace
from src.tools import mal_urls
from bs4 import BeautifulSoup
from lxml import etree

url = mal_urls.get_mal_anime_url()

def get_info(anime_id: str):
    soup = BeautifulSoup(mal_urls.get_html_from_url(f'{url}/{anime_id}'), 'html.parser')
    dom = etree.HTML(str(soup))


    # title_english = dom.xpath('/html/body/div[1]/div[2]/div[4]/div[1]/div/div[1]/div/p')[0].text
    # title_synonym = dom.xpath('/html/body/div[1]/div[2]/div[4]/div[1]/div/div[1]/div/h1/strong')[0].text
    # title_japanese = soup.find_all('div', class_='spaceit_pad')
    # title_japanese = ((title_japanese[1].text).split(' ')[1]).replace('\n', '')

    # mal_score = soup.find('div', class_='score-label').text

    # mal_rank = soup.find('span', class_='ranked').text
    # mal_rank = mal_rank.split('#')[1]

    # mal_popularity = soup.find('span', class_='popularity').text
    # mal_popularity = mal_popularity.split('#')[1]

    # mal_members = soup.find('span', class_='members').text
    # mal_members = mal_members.split(' ')[1]


    #left_side_contents = soup.find('div', class_='leftside')
    #left_side_contents_span = left_side_contents.findChildren('span', class_='spaceit_pad')
    

    #print(left_side_contents_span)


    return 'ok'

    # return {
    #     'title': {
    #         'english': title_english,
    #         'synonym': title_synonym,
    #         'japanese': title_japanese
    #     },
    #     'statistics': {
    #         'score': mal_score,
    #         'rank': mal_rank,
    #         'popularity': mal_popularity,
    #         'members': mal_members
    #     },
    #     'information': {

    #     }

    # }