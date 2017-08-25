#coding:utf8
import time

__author__ = 'eric'
__date__ = '2017/8/25 17:23'
import django
import os
os.environ.update({"DJANGO_SETTINGS_MODULE": "moocOnline.settings"})#注意输入对象的项目名称，非应用名称
django.setup()
from utils.email_send import send_register_email
for i in range(100):
    send_register_email('210618439@qq.com')