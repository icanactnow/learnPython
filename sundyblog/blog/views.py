#coding:utf8
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import *
from datetime import date

# Create your views here.

def hello(request):
    name = 'eric'
    age = 18
    return render(request,'hello.html',locals())#locals()以为将上面参数以字典形式发送给html


def index(request):
    d = date.today()
    articles = Article.objects.all()
    n = range(10)
    return render(request,'index.html',locals())


def article(request,pid):
    article = Article.objects.get(id=pid)
    return render(request,'article.html',locals())

def go(request):
    goValue = request.GET['search-text']
    #return HttpResponse('<h1>goValue</h1>')
    d = date.today()
    articles = Article.objects.all()
    return render(request,'index.html',locals())
