import requests
from bs4 import BeautifulSoup

url = "https://xhamster.com/pornstars"

req = requests.get(url)

sp = BeautifulSoup(req.content, 'html5lib')

table = sp.find('div', attrs={'data-role': 'pornstar-thumbs-container'})

rows = table.findAll('div', attrs={'class': 'pornstar-thumb-container__info-title'})

rows1 = table.findAll('div', attrs={'class': 'metric-container views'})

l1 = []
l2 = []

for row in rows:
    l1.append(row.a.get_text())

for row1 in rows1:
    l2.append(row1.get_text())

d = dict(zip(l1, l2))

cnt = 0

for k, v in d.items():
    cnt = cnt + 1
    print(cnt, k, "-", v)
