import sys

import requests
from bs4 import BeautifulSoup


def fetch_soup(url):
    res = requests.get(url)

    if res.status_code != 200:
        print(f'Could not download the page, code: {res.status_code}')
        sys.exit(1)

    return BeautifulSoup(res.text, 'lxml')


base_url = 'https://pl.wiktionary.org'
index_url = base_url + '/wiki/Indeks:Polski_-_Zwi%C4%85zki_frazeologiczne'


for link in fetch_soup(index_url).select('.mw-parser-output ul li a'):
    print(link.text)
