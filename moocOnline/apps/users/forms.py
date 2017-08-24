# coding:utf8
from django import forms

__author__ = 'eric'
__date__ = '2017/8/24 22:32'


class LoginForm(forms.Form):
    # 这里面的字段必须和前端form表单里面的字段一致，否则起不到验证效果
    username = forms.CharField(required=True)#必填
    password = forms.CharField(min_length=3)#最小长度为3