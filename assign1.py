import urllib.request
from bs4 import BeautifulSoup

def get_link(pos, lnk):
    link = lnk



    data = urllib.request.urlopen(link).read()

    soup = BeautifulSoup(data, 'html.parser')

    tags = soup('a')

    i = tags[pos-1]

    return(i.get('href', None))

link = 'http://py4e-data.dr-chuck.net/known_by_Eren.html'

for i in range(8):
    print(link)
    link = get_link(18,link )