import json
import urllib.parse
import urllib.request
from time import sleep

import requests
from bs4 import BeautifulSoup as bs

URL_TEMPLATE = f'https://api.litres.ru'
headers = {
    "Content-Type": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    # NOQA E501
}

session = requests.Session()


def parse(search, url=URL_TEMPLATE):
    search_parse = urllib.parse.quote(search.encode('utf8'))
    r = requests.get(url + f'/foundation/api/search?limit=12&q={search_parse}&types=text_book')
    url_book = json.loads(r.text)['payload']['data'][0]['instance']['url']

    r = requests.get('https://litres.ru' + url_book)
    result_list = {'href': [], 'title': [], 'description': [], 'year': [], 'image_link': [], 'ISBN': [],
                   'number_page': [], 'genre': [], 'tags': []}
    sleep(0.1)
    soup = bs(r.content, "html.parser")

    result_list['href'].append('https://litres.ru' + url_book)
    result_list['title'].append(search)
    pages, genre, tags = [], [], []
    a = soup.find('div', class_='biblio_book_info')
    for i in soup.find('div', class_='biblio_book_info'):
        pages = i.contents[0].text.split()
        genre = i.contents[1].text.split()
        tags = i.contents[2].text.split()

    result_list['number_page'].append(pages[1])
    result_list['genre'].append(' '.join(genre[1::]))
    result_list['tags'].append(' '.join(tags[1::]))
    result_list['year'].append(soup.find('div', class_='biblio_book_info_detailed_left').contents[3].contents[1].text)
    result_list['ISBN'].append(soup.find('div', class_='biblio_book_info_detailed_right').contents[0].contents[1].text)
    Soup = bs(urllib.request.urlopen('https://litres.ru' + url_book).read())
    rawJ = Soup.find_all('script')
    result_list['image_link'].append(str(rawJ[5]).split('var img_path = \'')[1].split('\';\n\t\t\t\t\t\t\tif')[0])
    result_list['description'].append(soup.find('div', itemprop="description").text)
    return result_list


print(parse("ход королевasdasы"))
