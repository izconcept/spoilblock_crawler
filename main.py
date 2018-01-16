from bs4 import BeautifulSoup

import requests

url = "http://awoiaf.westeros.org/index.php/Main_Page"

r = requests.get(url)

soup = BeautifulSoup(r.text)

for link in soup.find_all('a'):
    print(link.get('href'))
