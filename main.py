import json
import sys
import re

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

results = []

for link in fetch_soup(index_url).select('.mw-parser-output ul li a'):
    if link.get('href').endswith('(strona nie istnieje)'):
        continue

    meanings = []
    meanings_soup = fetch_soup(base_url + link.get('href'))

    meaning_section = meanings_soup.select(
        '#mw-content-text .mw-parser-output dl')

    try:
        for meaning in meaning_section[2].find_all('dd'):
            meaning_text = re.sub(r'\(\d+\.\d+\) ', '', meaning.get_text())
            meanings.append(meaning_text)
    except IndexError:
        print(f'Warning - {link.text} has no meanings section')
        continue

    results.append({
        'phrase': link.get_text(),
        'meanings': meanings
    })
