#coding:utf8
# from StdSuites import date
from datetime import date
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#返回字符串
from blog.models import Article


def hello(request):
    name = 'eric'
    return HttpResponse('hello'+name)
#返回HTML页面以及参数
def index(request):
    d = date.today()
    articles = Article.objects.all()
    n = range(10)
    return render(request,'index.html',locals())
