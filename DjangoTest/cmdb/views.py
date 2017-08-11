from django.shortcuts import render

# Create your views here.
# 创建用户信息列表
from cmdb import models

# user_list = [
#     {'user': 'jack', 'pwd': 'abc'},
#     {'user': 'tom', 'pwd': 'ABC'},
# ]


def hello(request):
    # return HttpResponse('hello django! i am eric')
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        temp = {'user': username, 'pwd': password}
        # user_list.append(temp)

        # 将数据保存到数据库中
        models.userInfo.objects.create(user = username,pwd=password)
    #从数据库中将数据读出
    user_list = models.userInfo.objects.all()
    return render(request, 'index.html', {'data': user_list})#最后一个参数返回给浏览器
