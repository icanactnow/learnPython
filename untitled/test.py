import re

code = 'xxixx232xxlovexx324xxyouxx'
b =re.findall('xx(.*?)xx',code)
print(b)