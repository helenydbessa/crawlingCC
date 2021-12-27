from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
import os
from webcrawler import linkList

#print(linkList)
charExcludedSpace = ["BTS (방탄소년단) – ", ":", "$", "?", "\"", "/", "="]
for link in linkList:
    try:
        html = urlopen(link)
    except HTTPError as e:
        print("ERRO ", e)
    bs = BeautifulSoup(html.read(), 'html.parser')
    name = bs.h1.text
    for c in charExcludedSpace:
        name = name.replace(c, "")
    #presentPath = os.path.dirname(__file__)
    folder = 'lyrics'
    if not os.path.exists(folder):
        os.mkdir(folder)
    folderPath = 'lyrics/'
    fileName = f'{name}.txt'
    wholePath = os.path.join(folderPath, fileName)
    print(wholePath)
    text = open(wholePath, "w", encoding="utf-8")
    if bs.find('div', {'class':'wp-block-column is-vertically-aligned-top'}) == None:
        result = bs.find('div', {'class':'card-body'}).find_all('div', {'class':'entry-content'})
        # print(result)
        for r in result:
            for t in r.find_all('td'):
                text.write(str(t.text))
        #text.write(bs.find('div', {'class':'card-body'}).find_all('td'))
        text.close()
    else:
        print("else")
        print(bs.find('div', {'class':'wp-block-column is-vertically-aligned-top'}))