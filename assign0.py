import urllib.request
from bs4 import BeautifulSoup

link = 'http://py4e-data.dr-chuck.net/comments_836356.html'

data = urllib.request.urlopen(link).read()

soup = BeautifulSoup(data, 'html.parser')

tags = soup('span')

total = 0

for i in tags:
    total += float(i.contents[0])

print(total)