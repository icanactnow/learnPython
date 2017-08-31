# coding:utf8
from captcha.fields import CaptchaField
from django import forms

__author__ = 'eric'
__date__ = '2017/8/24 22:32'


class LoginForm(forms.Form):
    # 这里面的字段必须和前端form表单里面的字段一致，否则起不到验证效果
    username = forms.CharField(required=True)  # 必填
    password = forms.CharField(min_length=3)  # 最小长度为3


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(min_length=3)  # 最小长度为3
    captcha = CaptchaField()
class ForgetPwdForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField()

class ModifyForm(forms.Form):
    password1 = forms.CharField(min_length=3)  # 最小长度为3
    password2 = forms.CharField(min_length=3)  # 最小长度为3
