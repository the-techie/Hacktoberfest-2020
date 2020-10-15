import urllib.request
import json

ulr = 'http://py4e-data.dr-chuck.net/comments_42.json'

data = urllib.request.urlopen(ulr)

data = data.read().decode()

data = json.loads(data)
data = data['comments']
total = 0
for i in data:
    total += i['count']
print(total)