import urllib.request
import xml.etree.ElementTree as et

data = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_836358.xml').read()

xml_data = et.fromstring(data)

lst = xml_data.findall('.//count')

total = 0

# for i in lst:
#     total += float(i.find('count').text)
for i in lst:
    total += float(i.text)
print(total)
