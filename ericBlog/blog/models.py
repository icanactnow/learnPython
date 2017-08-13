#coding:utf8
from django.db import models

# Create your models here.
#创建两个映射类，一张存储作者信息，一张存储文章信息
class Author(models.Model):
    name = models.CharField(max_length=32)#定义表字段
    age = models.IntegerField()
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(Author)