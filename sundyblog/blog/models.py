#coding:utf8
from django.db import models

# Create your models here.
#这里创建类以映射数据库中的表
class Author(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=18)

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(Author)
