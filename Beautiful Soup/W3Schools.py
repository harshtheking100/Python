import requests
from bs4 import BeautifulSoup

url = "https://www.w3schools.com/"

req = requests.get(url)
#print(req.content)

sp = BeautifulSoup(req.content, 'html5lib')
#print(sp.prettify())

table = sp.find('div', attrs={"class": "w3-row-padding w3-bar-block"})
#print(table)

rows = table.findAll('h3', attrs={"class": "w3-margin-top"})

for row in rows:
    print(row.get_text())