import  re

import requests
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:54.0) Gecko/20100101 Firefox/54.0'}
html = requests.post('http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E5%93%88%E5%A3%AB%E5%A5%87/pageName=2',headers=headers)
print(html.headers)
file = open('test.txt','wb')
file.write(html.content)
# 获取图片地址

picUrl = re.findall('"objURL":"(.*?)"',html.text,re.S)
i = 0
for each in picUrl:
    i += 1
    if not (i ==16 or  i==22 or i==24):
        picFile = open('dogPic//'+str(i)+'.jpg','wb')
        picContent = requests.get(each)
        #经获取的图片数据写入文件
        picFile.write(picContent.content)
        print('第%d张图片爬取完成'%(i))
    else:
        pass
