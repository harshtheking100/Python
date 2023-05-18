import requests
from bs4 import BeautifulSoup
#import pandas as pd


url = "https://www.passiton.com/inspirational-quotes"

req = requests.get(url)
# print(req.content)

sp = BeautifulSoup(req.content, 'html5lib')
# print(sp.prettify())


table = sp.find('div', attrs={'id': 'all_quotes'})
# print(table)


rows = table.findAll('div', attrs={'class': 'col-6 col-lg-4 text-center margin-30px-bottom sm-margin-30px-top'})


'''
for row in rows:
    #print(row)
    #print(row.img['alt'])
    print(row.img['alt'].split('#')[0])
    print('-------------------')
'''


d = {}
cnt = 0
for row in rows:
    cnt = cnt + 1
    d[cnt] = row.img['alt'].split('#')[0]

# print(d)

for k, v in d.items():
    print(k, ". ", v, end="\n\n")

'''df = pd.DataFrame(d, index=[x for x in range(1,len(rows))])
print(df)'''
