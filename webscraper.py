from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
from webcrawler import linkList

#print(linkList)
charExcludedSpace = ["BTS (방탄소년단) – ", ":", "$"]
for link in linkList:
    try:
        html = urlopen(link)
    except HTTPError as e:
        print(e)
    bs = BeautifulSoup(html.read(), 'html.parser')
    name = bs.h1.text
    for c in charExcludedSpace:
        name = name.replace(c, "")
    if bs.find('div', {'class':'wp-block-column is-vertically-aligned-top'}) == None:
        print(bs.find('div', {'class':'card-body'}).find_all('td'))
        text = open(f"{name}.txt", "w")
        text.write(bs.find('div', {'class':'card-body'}).find_all('td'))
        text.close()
    else:
        print(bs.find('div', {'cl""ass':'wp-block-column is-vertically-aligned-top'}))