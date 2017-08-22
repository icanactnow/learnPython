#coding:utf8
import django
import os
os.environ.update({"DJANGO_SETTINGS_MODULE": "DataImport.settings"})#注意输入对象的项目名称，非应用名称
if django.VERSON >= (1,7):
    django.setup()
from blog.models import  Blogs

Blogs.objects.create(title= "the first blog",content = "hahahhah")
blog2  = Blogs(title="blog1",content="当你要修改创建的数据时，使用这种方式，记得save()")
blog2.title = "blog2"
blog2.save()
