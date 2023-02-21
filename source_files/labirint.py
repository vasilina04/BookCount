import requests
from bs4 import BeautifulSoup as bs

URL_TEMPLATE = f'https://www.labirint.ru'

headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"  # NOQA E501
}


def parse(search, url=URL_TEMPLATE):
    r = requests.get(url + f'/search/{search}/?stype=0', headers=headers)
    soup = bs(r.content, "html.parser")
    if soup.find_all('a', class_='product-title-link') is None:
        return
    href = soup.find_all('a', class_='product-title-link')[0]['href']

    result_list = {'href': [], 'title': [], 'description': [], 'year': [], 'image_link': [], 'ISBN': [],
                   'number_page': [], 'genre': [], 'tags': []}
    r = requests.get(url + href, headers=headers)
    soup = bs(r.content, "html.parser")

    result_list['href'].append(url + href)
    result_list['title'].append(soup.find('div', id='product-title').h1.text)
    if soup.find('div', id='fullannotation') is None:
        result_list['description'].append(soup.find('div', id='product-about').p.text)
    else:
        result_list['description'].append(soup.find('div', id='fullannotation').text)
    result_list['year'].append(soup.find('div', class_='publisher').contents[2][2:7])
    result_list['image_link'].append(soup.find('div', id='product-image').img['data-src'])
    result_list['ISBN'].append(soup.find('div', class_="isbn").text[6::])
    if soup.find('div', class_="pages2") is not None:
        result_list['number_page'].append(soup.find('div', class_="pages2").text.split()[1])
    result_list['genre'].append(soup.find('div', id="product-info")['data-maingenre-name'])
    return result_list
