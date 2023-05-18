
#step1:Installation of requests , bs4, html5lib
#pip install requests
#pip install bs4
#pip install html5lib

#step2:
    
import requests
from bs4 import BeautifulSoup
import html5lib


#Step3:
url="https://www.passiton.com/inspirational-quotes"

req = requests.get(url) 
#print(req.content) 

sp= BeautifulSoup(req.content,'html5lib') 
#print(sp.prettify())

table=sp.find('div',attrs={'id':'all_quotes'})
#print(table)

rows= table.findAll('div',attrs={'class':'col-6 col-lg-4 text-center margin-30px-bottom sm-margin-30px-top'})


#print(len(rows),type(rows))
'''
for row in rows:
    #print(row)
    #print(row.img["alt"])
    print(row.img["alt"].split("#")[0])
    print("@@"*23)
    
'''    
d={}  
cnt=0
for row in rows:
    cnt=cnt+1
    d[cnt]=row.img["alt"].split("#")[0]
      

for k,v in d.items():
    print(k,". ",v,end="\n\n")