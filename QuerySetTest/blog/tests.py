#coding:utf8
import django
from django.test import TestCase
import os
os.environ.update({"DJANGO_SETTINGS_MODULE": "QuerySetTest.settings"})#注意输入对象的项目名称，非应用名称
django.setup()
# Create your tests here.
from blog.models import Article, Author, Tag
#输出sql语句
print(Author.objects.filter(name__regex='z'))
#以元组的形式输出结果
print(Author.objects.values_list('name','qq'))#以元组方式显示字段匹配结果
print(Author.objects.values_list('name',flat = True))#对于需要一个字段信息的查询以list形式输出
print(Author.objects.filter(name__regex='zh').values_list())#以元组形式输出过滤结果
print(Author.objects.filter(name__regex='^zhen$').values_list('qq',flat=True))#输出zhen作者的qq

# 获取字典形式的结果
print('==================================================')
print(Article.objects.values('title','tags'))#以字典形式输出字段匹配结果
print(Article.objects.values('title'))
print(Article.objects.filter(Author__name='twz915').values('title'))

# extra练习
print('==================================================')
print(Tag.objects.extra(select={'tag_name':'name'}).query)#SELECT (name) AS "tag_name", "blog_tag"."id", "blog_tag"."name" FROM "blog_tag"
print(Tag.objects.all().extra(select={'tag_name': 'name'}).defer('name').query)#SELECT (name) AS "tag_name", "blog_tag"."id" FROM "blog_tag"