import requests
from bs4 import BeautifulSoup as bs

URL_TEMPLATE = "https://igraslov.store/shop/?products-per-page=100"
FILE_NAME = "test.csv"


def parse(url=URL_TEMPLATE):
    result_list = {'href': [], 'title': []}
    r = requests.get(url)
    soup = bs(r.text, "html.parser")
    all_books = soup.find_all('li', class_='title')
    for book in all_books:
        result_list['href'].append(book.a['href'])
        result_list['title'].append(book.text)
    return result_list
