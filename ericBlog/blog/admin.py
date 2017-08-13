#coding:utf8
from django.contrib import admin

# Register your models here.
# 着这里注册模型，以便建立映射
from blog.models import Article, Author

admin.site.register(Author)
admin.site.register(Article)