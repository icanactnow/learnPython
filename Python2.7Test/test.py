#coding:utf8
import  re
qq = input()
if re.match(r'.+@qq.com',str(qq)):
    print('是qq邮箱')
else:
    print('不是qq邮箱')