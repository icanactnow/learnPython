# -*-coding:utf-8-*-
import requests

r = requests.get('http://localhost:5000/client/login')  # 用户向客户端请求登录，客户端返回授权服务器的请求重定向
print r.text
print '======='
print r.history
print '======='
print r.url
print '======='
uri_login = r.url.split('?')[0] + '?user=eric&pw=1234'
r2 = requests.get(uri_login)  # 用户通过客户端返回的重定向地址通过用户名及密码登录，最终返回token
print r2.text
print '======='
r = requests.get('http://127.0.0.1:5000/test1', params={'token': r2.text})  # 客户端通过token向资源服务器索要资源
print r.text
