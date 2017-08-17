# coding:utf8
from django.db import models

# Create your models here.
from django.utils.encoding import python_2_unicode_compatible


# 编写兼容python2的代码
@python_2_unicode_compatible
class Author(models.Model):
    name = models.CharField(max_length=50)
    qq = models.CharField(max_length=10)
    addr = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Article(models.Model):
    title = models.CharField(max_length=50)
    Author = models.ForeignKey(Author)
    content = models.TextField()
    score = models.IntegerField()
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
