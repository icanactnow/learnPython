#coding:utf8
from django.contrib import admin
from blog.models import *

# Register your models here.

admin.site.register(Author)#注册在migrations中映射过的表，映射完后通过migrate 在数据库中建立表。
admin.site.register(Article)
