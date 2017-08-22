# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def add(request):
    a = request.GET['a']
    b = request.GET['b']
    return HttpResponse(int(a)+int(b))
def add2(request,a,b):
    return HttpResponse(int(a)+int(b))
def home(request):
    return  render(request,'home.html')