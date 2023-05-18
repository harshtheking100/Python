import requests
from bs4 import BeautifulSoup
#import pandas as pd


url = "https://www.thrillophilia.com/collections/best-of-india-this-summer"

req = requests.get(url)
# print(req.content)

sp = BeautifulSoup(req.content, 'html5lib')
# print(sp.prettify())


table = sp.find('div', attrs={'itemprop': 'articleBody'})
# print(table)


rows = table.findAll('h3', attrs={'class': 'tour-title'})

lr = []
lr1 = []
for row in rows:
    #print(row)
    #print(row.img['alt'])
    #print(row.a['href'].split('/')[2].replace('-',' '))
    #print(row.a)
    #print('-------------------')
    lr.append(row.a.get_text())

rows1 = table.findAll('span', attrs={'class': 'big-size'})

for row1 in rows1:
    #print(row1.span['data-amount'])
    lr1.append(row1.span['data-amount'])

d = dict(zip(lr,lr1))

for k, v in d.items():
    print(k, '-', v, end='\n\n')


'''d = {}
cnt = 0
for row in rows:
    cnt = cnt + 1
    d[cnt] = row.a['href'].split('/')[2].replace('-',' ')

# print(d)

for k, v in d.items():
    print(k, ". ", v, end="\n\n")'''

'''df = pd.DataFrame(d, index=[x for x in range(1,len(rows))])
print(df)'''
