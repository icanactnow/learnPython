#coding:utf8
from django import forms
import re
__author__ = 'eric'
__date__ = '2017/8/29 18:45'
from operation.models import UserAsk

class UserAskForm(forms.ModelForm):
    class Meta:
        model = UserAsk # 指定forms对应的model
        fields=['name','mobile','course_name'] #指定form要验证的字段

    #验证手机号码有效性，下面函数定义为固定格式
    def clean_mobile(self):
        moblie = self.cleaned_data['mobile']#获取填入的moblie
        #创建正则表达
        REGEX_MOBILE = "^1[358]\d{9}|^147\d{8}$|^176\d{8}$"
        p = re.compile(REGEX_MOBILE)

        if p.match(moblie):#如果匹配成功
            return moblie
        else:
            #下面的错误返回格式也是固定的
            raise forms.ValidationError(u"手机号码非法",code='mobile_invalid')