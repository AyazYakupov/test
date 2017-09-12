#!/usr/bin/python
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup 
import re

url = 'http://py4e-data.dr-chuck.net/known_by_Majka.html'

for i in range(7):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    count = 0
    a = soup.find_all('a')
    for i in a:
        link = i.get('href')
        count = count + 1
        if count == 18:
            print(link)
            url = link
            break
