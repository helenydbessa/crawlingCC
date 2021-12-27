from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://colorcodedlyrics.com/2014/01/bts-lyrics-index')
bs = BeautifulSoup(html.read(), 'html.parser')
nameList = bs.find('figure', {'class':'wp-block-table'}).find_all('a')
# for song in nameList:
#     #print(song)
#     if('href' in song.attrs):
#         #print(song.attrs['href'])
#         print("yay")

linkList = []
nameList2 = bs.findChildren('figure', {'class':'wp-block-table'})
for song in nameList2:
    for link in song.find_all('a'):
        if('href' in link.attrs):
            linkList.append(link.attrs['href'])
            #print(link.attrs['href'])

print(linkList)