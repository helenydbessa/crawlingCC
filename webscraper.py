from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
from webcrawler import linkList

#print(linkList)
for link in linkList:
    try:
        html = urlopen(link)
    except HTTPError as e:
        print(e)
    bs = BeautifulSoup(html.read(), 'html.parser')
    print(bs.h1)
    if bs.find('div', {'class':'wp-block-column is-vertically-aligned-top'}) == None:
        print(bs.find('div', {'class':'card-body'}).find_all('td'))
    else:
        print(bs.find('div', {'class':'wp-block-column is-vertically-aligned-top'}))