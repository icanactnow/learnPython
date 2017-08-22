#coding:utf8
from django.http import HttpResponse, Http404
from django.shortcuts import render
import datetime
# Create your views here.
def show(request):
    time = datetime.datetime.now()
    html = '<h1>now is %s</h1>' %time
    return HttpResponse(html)
def showNumber(request,num):#num是匹配值
    try:
        NUM = int(num)
    except ValueError:
        raise Http404()
    assert False
    return  HttpResponse('number is %d' %NUM)
