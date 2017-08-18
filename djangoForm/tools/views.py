# from django import HttpResponse, request
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from tools.forms import AddForm


def index(request):
    if request.method =='POST':
        form = AddForm(request.POST)#获取提交的表单数据,以字典的形式

        #判断数据是否合法
        if form.is_valid():
            # 从字典里面取出值
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a)+int(b)))

    else:#如果浏览器不是post提交数据
        form = AddForm()
    return render(request,'index.html',{'form':form})