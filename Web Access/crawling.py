import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSl certificate
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# get url data
url = 'http://data.pr4e.org/romeo.txt'  # this can be any website.
data = urllib.request.urlopen(url).read()
soup = BeautifulSoup(data, 'html.parser')

# Retrieving all html anchor tags
tags = soup('a')
for tag in tags:
    tag = tag.get('href', ' ')
    if not re.search('^http.*', tag): continue  # remove tag that doesn't start with http
    print(tag)

# Exercise 1
url = 'http://py4e-data.dr-chuck.net/comments_1187245.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('span')
# keys
# print('TAG:', tag)
# print('URL:', tag.get('href', None))
# print('Contents:', tag.ontents[0])
# print('Attrs:', tag.attrs)

total = 0
for tag in tags:
    numbers = int(tag.contents[0])
    total += numbers
print(total)

# Exercise 2
try:
    count = int(input('Enter count: '))
    postion = int(input('Enter postion: '))
except:
    print('Invalid Parameters')
    quit()

url = 'http://py4e-data.dr-chuck.net/known_by_Franco.html'
counter = 0
while True:
    if counter == count + 1: break
    # opening url
    print('Retrieving: ',url)
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')

    # get new url
    tagcounter = 0
    for tag in tags:
        temp = tag.get('href', None)
        tagcounter += 1
        if tagcounter == postion: break
    url = temp
    counter += 1
