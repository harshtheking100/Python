import requests
from bs4 import BeautifulSoup

url = "https://www.w3schools.com/"

req = requests.get(url)
#print(req.content)

sp = BeautifulSoup(req.content, 'html5lib')
#print(sp.prettify())

table = sp.find('div', attrs={"class": "w3-row-padding w3-bar-block"})
#print(table)


#Headers
rows = table.findAll('h3', attrs={"class": "w3-margin-top"})
rw = []
for rw1 in rows:
    rw.append(rw1.get_text())


#subtopics
rows1 = table.findAll('a', attrs={"class": "w3-bar-item ga-top-drop w3-button"})


rows3 = table.findAll('div', attrs={"class": "w3-col l3 m6"})

#rows4 = rows3.findAll()

l2 = []
for i in rows3:
    l2.append(i.get_text())

str1 = ""
for i in l2:
    if l2 == '\n':
        str1 = str1 + " "
    else:
        str1 = str1 + i

#print(str1)


#for k in rw:
l3 = str1.split('\n')
#l3.remove('Next Bootcamp:')


#for j in l3:
#    print(j)
for j in l3:
    if len(j) == 0:
        l3.remove(j)

l3.remove(l3[13])
l3.remove(l3[13])
l3.remove(l3[13])
l3.remove(l3[13])
l3.remove(l3[13])


for i in l3:
    print(i)

#print(l3[13])
#print(len(l3[13]))






'''
for row in rows:
    print(row.get_text())
    rows1 = table.findAll('a', attrs={"class": "w3-bar-item ga-top-drop w3-button"})
    for row1 in rows1:
        print(row1.get_text())
    print('-------------------------------------------------------------')
    print('-------------------------------------------------------------')'''