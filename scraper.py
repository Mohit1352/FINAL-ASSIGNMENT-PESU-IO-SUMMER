import csv
import urllib.request as ur
from bs4 import BeautifulSoup
soup=BeautifulSoup(ur.urlopen("https://karki23.github.io/Weather-Data/assignment.html").read(),"html.parser")
links=[]
for link in soup.find_all('a'):
    links.append("https://karki23.github.io/Weather-Data/"+link.get('href'))

for link in links:
    bsoup=BeautifulSoup(ur.urlopen(link).read(),"html.parser")
    entries=bsoup.find_all('td')
    nrows=len(bsoup.find_all('tr'))
    ncols=24#len(entries)//nrows
    name=entries[1]
    with open('.\dataset\Scraps\{f}.csv'.format(f=str(name)[4:-5]), mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)     
        for i in range(nrows-1):
            col=[]
            for j in range(ncols):
                col.append(str(entries[(ncols*i)+j])[4:-5])
            writer.writerow(col)
        print("DONE")
