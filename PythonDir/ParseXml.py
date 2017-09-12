import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = 'http://py4e-data.dr-chuck.net/comments_22652.xml'

xml = urllib.request.urlopen(url).read()

tree = ET.fromstring(xml)

lst = tree.findall('comments/comment')

sumofint = 0
for i in lst:

    j = i.find('count').text
    sumofint = sumofint + int(j)

print(sumofint)
