import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re
url = "http://py4e-data.dr-chuck.net/comments_22650.html"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
ali = int()
sp = r'\d+'
it = soup.findAll(text=re.compile(sp))
for i in it:
    try: 
        ali = ali + int(i)
    except:
        continue
print(ali)
