import re

import requests as requests

source = open('source.txt', 'r')
html = source.read()
linkList = re.findall('img src="(.*?)" class="lessonimg"', html, re.S)
i = 1
for link in linkList:
    print('downloding the %s picture' % i)
    downing = requests.get(link)
    fp = open('pic//' + str(i) + '.jpg', 'wb')
    fp.write(downing.content)
    fp.close()
    i += 1
