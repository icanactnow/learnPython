import django
import os
os.environ.update({"DJANGO_SETTINGS_MODULE": "djangoForm.settings"})#注意输入对象的项目名称，非应用名称
django.setup()
from django import forms


class AddForm(forms.Form):#表单里面有两项数据
    a = forms.IntegerField()
    b = forms.IntegerField()
