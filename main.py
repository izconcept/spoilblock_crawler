from bs4 import BeautifulSoup

import requests

url = "http://awoiaf.westeros.org/index.php/Main_Page"

r = requests.get(url)

soup = BeautifulSoup(r.text)

word_bank = set()

for link in soup.find_all('a'):
    print(link)
    word_bank.add(link.get('title'))

print(word_bank)