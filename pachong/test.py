import re

f = open('text.txt', 'r')
html = f.read()
f.close()
title = re.search('<title>(.*?)</title>', html, re.S).group(1)#search 找到即停止，findall会遍历所有文件内容
print(title)
